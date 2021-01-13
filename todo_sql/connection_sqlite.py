import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


if __name__ == "__main__":
    create_todos_sql = """
    CREATE TABLE IF NOT EXISTS todos (
        id integer PRIMARY KEY,
        nazwa text NOT NULL,
        deadline text NOT NULL,
        priorytet text
        )
        """
    db_file = "database.db"
    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_todos_sql)
