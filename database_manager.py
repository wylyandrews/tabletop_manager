import config
import os
import urllib.parse as up
import psycopg2

from credentials import set_credentials
from database_interface import DatabaseInterface
from utils.json_utils import import_json
from simple_query import make_table, drop_table


class DatabaseManager:
    def __init__(self):
        set_credentials()  # Sets os.environ["DATABASE_URL"]
        self.db_interface = DatabaseManager.initialize_interface()  # Creates the db interface
        self.tables = list()

    @staticmethod
    # Setup a database interface object with the postgres database
    def initialize_interface():
        up.uses_netloc.append("postgres")
        url = up.urlparse(os.environ["DATABASE_URL"])
        conn = psycopg2.connect(database=url.path[1:],
                                user=url.username,
                                password=url.password,
                                host=url.hostname,
                                port=url.port)
        return DatabaseInterface(conn)

    # Executes drop and create commands given information about inputted tables in json format
    def generate_database(self):
        table_json = import_json(config.JSON_CREATE_TABLES_LOCATION)

        drop_commands = list()
        create_commands = list()
        # Parse the json file. Drop and create a table for each top-level dictionary in the json
        for table_name, table_values in table_json.items():
            drop_commands.append(drop_table(table_name))                  # Drop
            create_commands.append(make_table(table_name, table_values))  # Create
            self.tables.append(table_name)                                # Record

        # Execute
        self.db_interface.execute_commands(drop_commands + create_commands)

        # Save and close
        self.db_interface.connection.commit()

    def shutdown(self):
        self.db_interface.end_connection()
