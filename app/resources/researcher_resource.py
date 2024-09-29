from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.researcher import ResearchProfile, Config
from app.services.service_factory import ServiceFactory

class ResearcherResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("ResearcherResourceDataService")
        self.database = "p1_database"
        self.collection = "ResearchProfile"
        self.key_field="organization"

    def get_by_key(self, key: str) -> ResearchProfile:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        result = ResearchProfile(**result)
        
        # result = Config.json_schema_extra['example']

        return result


