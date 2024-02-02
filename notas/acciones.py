import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"\n Ok, {usuario[1]}!! Vamos a crear una nueva nota: ... ")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"Perfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
    
    def mostrar(self,usuario):
        print(f"\n Vale {usuario[1]}, aquí tienes tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print(f"Nota : {nota[0]}")
            print(f"Título  : {nota[2]}")
            print(f"Contenido  : {nota[3]}")
            print(f"Fecha  : {nota[4]}")
    def borrar(self, usuario):
        print(f"\n Vale {usuario[1]}, vamos a eliminar notas. ")
        print(f"Estas son las notas existentes: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print(f"Nota : {nota[0]}, {nota[2]}")
        titulo = input("¿Que nota quieres borrar?")
        
        notaAborrar = modelo.Nota(usuario[0], titulo)
        eliminar = notaAborrar.eliminar()
        if(eliminar[0]>= 1):
            print(f"Se ha borrado la nota: {notaAborrar.titulo}")
        else:
            print("No se ha borrado la nota")





