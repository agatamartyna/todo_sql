from connection_sqlite import create_connection
import sqlite3


class Todos:

    def all(self):
        cur = create_connection("database.db").cursor()
        cur.execute("SELECT * FROM todos")
        rows = cur.fetchall()

        toddos = [list(row) for row in rows]

        todos_list = []
        for todo in toddos:
            todo_dict = {}
            todo_dict["id"] = todo[0]
            todo_dict["nazwa"] = todo[1]
            todo_dict["deadline"] = todo[2]
            todo_dict["priorytet"] = todo[3]
            todos_list.append(todo_dict)

        return todos_list

    def get(self, id):
        cur = create_connection("database.db").cursor()
        cur.execute("SELECT * FROM todos WHERE id=?", (id,))
        rows = cur.fetchall()
        row = list(rows[0])
        todo = {
            "id": row[0], "nazwa": row[1],
            "deadline": row[2], "priotrytet": row[3]
        }

        return todo

    def create(self, todo):
        conn = create_connection("database.db")
        sql = '''INSERT INTO todos(id, nazwa, deadline, priorytet)
                    VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, todo)
        conn.commit()

    def update(self, id, **kwargs):
        conn = create_connection("database.db")
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id,)

        sql = f''' UPDATE todos
                     SET {parameters}
                     WHERE id = ?'''
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)

    def delete(self, id):
        conn = create_connection("database.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM todos WHERE id=?', (id,))
        conn.commit()


todos = Todos()
