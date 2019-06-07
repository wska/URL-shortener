# William Skagerström - 23-04-2019

import sqlite3
from sqlite3 import OperationalError

# Initializes the URL table in the DB
def initialize_table():
    create_table = """
        CREATE TABLE URL(
        ID INTEGER PRIMARY KEY,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('links.db') as conn: # Also creates said DB is it does not exist
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError as e:
            pass

# Removes all previous entries in the DB
def reset_table():
    reset = """ DROP TABLE URL """
    with sqlite3.connect('links.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(reset)
        except OperationalError as e:
            pass
    initialize_table()


def main():
    initialize_table()
    #reset_table() # Remove comment if you wish to reset the database upon startup. Otherwise the state will persist even if the application is shut down.

if __name__ == "__main__":
    main()
