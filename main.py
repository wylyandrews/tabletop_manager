from database_manager import DatabaseManager
from simple_query import insert_into_table


def main():
    db_manager = DatabaseManager()
    db_manager.generate_database()
    db_manager.insert_characters()
    db_manager.shutdown()


main()
