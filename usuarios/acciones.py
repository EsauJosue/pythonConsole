import usuarios.usuario as modelo
import notas.acciones

class Opciones:
    def registro(self):
        print("\nOk!! Vamos a registrate en el sistema... ")
        nombre = input('¿Cual es tu nombre?: ')
        apellidos = input('¿Cuáles son tus apellidos: ')
        email = input('Cuál es tu email: ')
        password = input('Ingresa una contraseña: ')
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        inscripcion = usuario.registrar()
        
        if inscripcion[0] >= 1:
            print(f"Todo ha salido perfecto, se ha registrado el usuario con el email {email}")
        else: 
            print("Ocurrio un error en el registro")

    
    def login(self):
        print("Vale!! Identifícate en el sistema...")
        try:
            email = input('Cuál es tu email: ')
            password = input('Ingresa una contraseña: ')
            usuario = modelo.Usuario('', '',email,password )
            login = usuario.identificar()
            print(login)
            if email == login[3]:
                print(f"Bienvenido {login[1]} te has registrado el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, intentalo nuevamente")
    
    def proximasAcciones(self, usuario):
        print("""
            Aciones disponibles: 
              - Crear nota (crear)
              - Mostrar tus notas (mostrar)
              - Eliminar nota (eliminar)
              - Salir (salir)

            """)
        accion = input("Que quieres hacer: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            print("Vamos a crear")
            hazEl.crear(usuario)

            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f" Ok {usuario[1]}, hasta pronto")
            exit()

        return None