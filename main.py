import os
import urllib.parse as up
import psycopg2

from credentials import set_credentials
from database_interface import DatabaseInterface

def main():
    # Set os.environ["DATABASE_URL"]
    set_credentials()
    db_interface = initialize_interface()
    db_interface.test_execute()


def initialize_interface():
    up.uses_netloc.append("postgres")
    url = up.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    return DatabaseInterface(conn)


main()
