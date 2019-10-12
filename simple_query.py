from psycopg2 import sql

# Returns an SQL query to create a table
# Do not allow user input. This is susceptible to injection
def make_table(name, values):
    if isinstance(values, list):
        return "CREATE TABLE IF NOT EXISTS {0} ({1})".format(name, ", ".join(values))
    if isinstance(values, dict):
        return "CREATE TABLE IF NOT EXISTS {0} ({1})".format(name, ", ".join([" ".join(col) for col in values.items()]))


# Returns an SQL query to drop a table
def drop_table(name):
    return sql.SQL("DROP TABLE IF EXISTS {0}").format(sql.Identifier(name))

def insert_into_table(name, values):
    pass
