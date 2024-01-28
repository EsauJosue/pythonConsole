import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database = "master_python"

)
class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        return self.nombre
    
    def identificar(self):
        return self.nombre

