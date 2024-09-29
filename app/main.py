# main.py

import os
import logging
from functools import lru_cache
from typing import Annotated, List, Optional

import configparser
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.services import ServiceFactory
from app.models.researcher import ResearchProfile

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache()
def get_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'database.ini')
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    config.read(config_path)
    return config

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application...")
    config = get_config()
    service_factory = ServiceFactory(config)
    app.state.service_factory = service_factory
    
    try:
        db_service = service_factory.get_service('ResearcherResourceDataService')
        db_service._get_connection()
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

def get_service_factory():
    return app.state.service_factory

@app.get("/researchers", response_model=List[ResearchProfile])
async def get_all_researchers(service_factory: Annotated[ServiceFactory, Depends(get_service_factory)]):
    researcher_resource = service_factory.get_service('ResearcherResource')
    researchers = researcher_resource.get_all()
    if not researchers:
        raise HTTPException(status_code=404, detail="No researchers found")
    return researchers

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)