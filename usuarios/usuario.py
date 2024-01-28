from datetime import datetime
import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database = "master_python"

)

cursor = database.cursor(buffered=True)#buffered = True permite hacer muchas consultas con el mismo cursor
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, fecha)
        cursor.execute(sql,usuario)
        database.commit()
        return [cursor.rowcount, self]
    def identificar(self):
        return self.nombre

