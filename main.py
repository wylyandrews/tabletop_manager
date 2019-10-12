from database_manager import DatabaseManager


def main():
    db_manager = DatabaseManager()
    db_manager.generate_database()
    db_manager.shutdown()


main()
