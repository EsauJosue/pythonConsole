from datetime import datetime
import usuarios.conexion as conexion
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

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
        #Consulta 
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

         # Se encripta la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        #Se ejecuta la consulta
        cursor.execute(sql, usuario)
        resultado = cursor.fetchone()
        return resultado

