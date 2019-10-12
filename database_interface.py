from psycopg2 import sql
from simple_query import make_table


# Provides interface with the database
class DatabaseInterface:
    def __init__(self, connection):
        self.connection = connection
        self.tables = list()

    def execute_commands(self, commands):
        cur = self.connection.cursor()
        for command in commands:
            cur.execute(command)
        self.connection.commit()

    def test_execute(self):
        cur = self.connection.cursor()
        cur.execute("""DROP TABLE IF EXISTS characters""")
        cur.execute(sql.SQL("""CREATE TABLE IF NOT EXISTS {} (
                        name TEXT,
                        race TEXT,
                        class TEXT,
                        level INTEGER
                        )""").format(sql.Identifier('characters')))

        initial_character = {
            "name": "Johnson Smith",
            "race": "Elf",
            "class": "Barbarian",
            "level": 1
        }

        cur.execute("""INSERT INTO characters VALUES ( %(name)s, %(race)s, %(class)s, %(level)s)""", initial_character)

        cur.execute("""SELECT * FROM characters""")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        self.connection.commit()
        cur.close()

    def test_execute2(self):
        cur = self.connection.cursor()
        t_name = "classes"
        t_values_dict = {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "type": "TEXT"
        }

        query = make_table(t_name, t_values_dict)
        print(query)
        cur.execute(query)
        self.connection.commit()
        cur.close()

    def end_connection(self):
        self.connection.close()
