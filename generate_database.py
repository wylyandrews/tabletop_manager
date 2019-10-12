import psycopg2
from simple_query import make_table, drop_table


def generate_database(db_interface):
    cursor = db_interface.connection.cursor()

    # Input json example
    json = {
        "characters": {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "race": "TEXT",
            "class": "TEXT",
            "level": "INTEGER",
            "background": "TEXT"
        },
        "classes": {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "type": "TEXT"
        }
    }

    drop_commands = list()
    create_commands = list()
    # Parse the json file. Drop and create a table for each top-level dictionary in the json
    for table_name, table_values in json.items():
        drop_commands.append(drop_table(table_name))                  # Drop
        create_commands.append(make_table(table_name, table_values))  # Create
        db_interface.tables.append(table_name)                        # Record

    # Combine all the commands together
    all_commands = drop_commands + create_commands

    # Execute
    db_interface.execute_commands(all_commands)

    # Save and close
    db_interface.connection.commit()
    cursor.close()
