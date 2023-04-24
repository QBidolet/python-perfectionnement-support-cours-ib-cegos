import sqlite3
from contextlib import contextmanager


@contextmanager
def database_connection():
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    yield cursor
    connection.commit()
    connection.close()


def create_tables():
    with database_connection() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user_id INTEGER, text TEXT)")


create_tables()