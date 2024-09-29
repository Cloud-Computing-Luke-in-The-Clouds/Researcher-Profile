import pymysql
from .BaseDataService import DataDataService

class MySQLRDBDataService(DataDataService):
    def __init__(self, context):
        super().__init__(context)

    def _get_connection(self):
        connection = pymysql.connect(
            host=self.context["host"],
            port=self.context["port"],
            user=self.context["user"],
            passwd=self.context["password"],
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return connection

    def get_data_object(self, database_name: str, collection_name: str, key_field: str, key_value: str):
        connection = None
        result = None
        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name} WHERE {key_field}=%s"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement, [key_value])
            result = cursor.fetchone()
        except Exception as e:
            print(f"Error in get_data_object: {e}")
        finally:
            if connection:
                connection.close()
        return result

    def get_all_data_objects(self, database_name: str, collection_name: str):
        connection = None
        result = None
        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name}"
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute(sql_statement)
            result = cursor.fetchall()
        except Exception as e:
            print(f"Error in get_all_data_objects: {e}")
        finally:
            if connection:
                connection.close()
        return result