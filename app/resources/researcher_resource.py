from typing import List, Optional
from framework.resources.base_resource import BaseResource
from app.models.researcher import ResearchProfile

class ResearcherResource(BaseResource):
    def __init__(self, config, data_service):
        super().__init__(config)
        self.data_service = data_service
        self.database = "researcher_database"
        self.table = "ResearchProfile"
        self.key_field = "organization"

    def get_by_key(self, key: str) -> Optional[ResearchProfile]:
        result = self.data_service.get_data_object(
            self.database, self.table, self.key_field, key
        )
        if result:
            return ResearchProfile(**result)
        return None

    def get_all(self) -> List[ResearchProfile]:
        try:
            results = self.data_service.get_all_data_objects(self.database, self.table)
            profiles = [ResearchProfile(**row) for row in results] if results else []
            return profiles
        except Exception as e:
            print(f"Error fetching all ResearchProfiles: {str(e)}")
            return []