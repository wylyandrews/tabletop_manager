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

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS characters""")
cur.execute("""CREATE TABLE IF NOT EXISTS characters (
                name TEXT,
                race TEXT,
                class TEXT,
                level INTEGER
                )""")

initial_character = {
    "name": "John Smith",
    "race": "Elf",
    "class": "Barbarian",
    "level": 1
}

cur.execute("""INSERT INTO characters VALUES ( %(name)s, %(race)s, %(class)s, %(level)s)""", initial_character)

cur.execute("""SELECT * FROM characters""")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()

cur.close()
conn.close()