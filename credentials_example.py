import os


# Set the environment variable that let's us connect to the database
def set_credentials():
    os.environ["DATABASE_URL"] = \
        "postgres://<user>:<password>@<server>:<??? 4 digits>/<default database (same as user)>"
