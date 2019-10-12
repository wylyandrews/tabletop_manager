

# Provides interface with the database
class DatabaseInterface:
    def __init__(self, connection):
        self.connection = connection

    def execute_commands(self, commands):
        cur = self.connection.cursor()
        for command in commands:
            cur.execute(command)
        self.connection.commit()

    def end_connection(self):
        self.connection.close()
