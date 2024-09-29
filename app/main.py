# Standard library imports
import os
import logging
from functools import lru_cache
from typing import Annotated

# Third-party imports
import configparser
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Local application imports
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
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

def get_db_service(config: configparser.ConfigParser = Depends(get_config)):
    if 'mysql' not in config:
        raise ValueError("MySQL configuration not found in the config file")

    mysql_config = config['mysql']
    context = {
        'host': mysql_config.get('host'),
        'port': mysql_config.getint('port', 3306),
        'user': mysql_config.get('user'),
        'password': mysql_config.get('password')
    }

    if not all(context.values()):
        raise ValueError("Missing required database configuration values")

    return MySQLRDBDataService(context=context)

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
    db = get_db_service(get_config())
    try:
        db._get_connection()
        logger.info("Database connection successful")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# @app.get("/health")
# async def health_check(db: Annotated[MySQLRDBDataService, Depends(get_db_service)]):
#     try:
#         db._get_connection()
#         return {"status": "healthy", "database": "connected"}
#     except Exception as e:
#         logger.error(f"Health check failed: {e}")
#         return {"status": "unhealthy", "database": "disconnected"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)