from fastapi import APIRouter

from app.models.researcher import ResearchProfile
from app.resources.researcher_resource import ResearcherResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/researcher_profile/{researcher_id}", tags=["users"])
async def get_researcher(researcher_id: str) -> ResearchProfile:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("ResearcherResource")
    result = res.get_by_key(researcher_id)
    return result

