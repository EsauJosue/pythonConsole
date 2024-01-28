import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        port="8889",
        user="root",
        password="root",
        database = "master_python"

    )
    cursor = database.cursor(buffered=True)#buffered = True permite hacer muchas consultas con el mismo cursor
    return [database, cursor]