from framework.services.service_factory import BaseServiceFactory
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
from app.resources.researcher_resource import ResearcherResource

class ServiceFactory(BaseServiceFactory):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.data_service = None

    def get_service(self, service_name: str):
        if service_name == 'ResearcherResource':
            if not self.data_service:
                self.data_service = self.get_db_service()
            return ResearcherResource(config=self.config, data_service=self.data_service)
        elif service_name == 'ResearcherResourceDataService':
            if not self.data_service:
                self.data_service = self.get_db_service()
            return self.data_service
        else:
            return None

    def get_db_service(self):
        mysql_config = self.config['mysql']
        context = {
            'host': mysql_config.get('host', 'localhost'),
            'port': mysql_config.getint('port', 3306),
            'user': mysql_config.get('user'),
            'password': mysql_config.get('password')
        }
        return MySQLRDBDataService(context=context)