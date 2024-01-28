from datetime import datetime
import mysql.connector
import hashlib
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
        
        # Se encripta la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        #Se valida para cachar los errores de integridad en la base de datos
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    
    def identificar(self):
        return self.nombre

