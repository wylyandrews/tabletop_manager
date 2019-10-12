

# Provides interface with the database
class DatabaseInterface:
    def __init__(self, connection):
        self.connection = connection

    def test_execute(self):
        cur = self.connection.cursor()
        cur.execute("""DROP TABLE IF EXISTS characters""")
        cur.execute("""CREATE TABLE IF NOT EXISTS characters (
                        name TEXT,
                        race TEXT,
                        class TEXT,
                        level INTEGER
                        )""")

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

    def end_connection(self):
        self.connection.close()
