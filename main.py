import os
import urllib.parse as up
import psycopg2

from credentials import set_credentials

# Set os.environ["DATABASE_URL"]
set_credentials()

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
                        user=url.username,
                        password=url.password,
                        host=url.hostname,
                        port=url.port)
