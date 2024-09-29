# File: /home/ubuntu/Researcher-Profile/app/resources/researcher_resource.py

from typing import Any
from framework.resources.base_resource import BaseResource
from app.models.researcher import ResearchProfile, Config

class ResearcherResource(BaseResource):
    def __init__(self, config, data_service):
        super().__init__(config)
        self.data_service = data_service
        self.database = "p1_database"
        self.collection = "ResearchProfile"
        self.key_field = "organization"

    def get_by_key(self, key: str) -> ResearchProfile:
        result = self.data_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
        return ResearchProfile(**result)