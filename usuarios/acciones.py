import usuarios.usuario as modelo

class Opciones:
    def registro(self):
        print("\nOk!! Vamos a registrate en el sistema... ")
        nombre = input('¿Cual es tu nombre?: ')
        apellidos = input('¿Cuáles son tus apellidos: ')
        email = input('Cuál es tu email: ')
        password = input('Ingresa una contraseña: ')
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        inscripcion = usuario.registrar()
        
        if inscripcion:
            print(f"Todo ha salido perfecto, se ha registrado el usuario con el email {email}")
        else: 
            print("Ocurrio un error en el registro")

    
    def login(self):
        print("Vale!! Identifícate en el sistema...")
        email = input('Cuál es tu email: ')
        password = input('Ingresa una contraseña: ')