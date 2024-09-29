# File: /home/ubuntu/Researcher-Profile/app/services/service_factory.py

import configparser
from framework.services.service_factory import BaseServiceFactory
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
from app.resources.researcher_resource import ResearcherResource

class ServiceFactory(BaseServiceFactory):
    def __init__(self, config: configparser.ConfigParser):
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
        if 'mysql' not in self.config:
            raise ValueError("MySQL configuration not found in the config file")

        mysql_config = self.config['mysql']
        context = {
            'host': mysql_config.get('host', 'localhost'),
            'port': mysql_config.getint('port', 3306),
            'user': mysql_config.get('user', 'root'),
            'password': mysql_config.get('password', 'dbuserdbuser')
        }

        if not all(context.values()):
            raise ValueError("Missing required database configuration values")

        return MySQLRDBDataService(context=context)