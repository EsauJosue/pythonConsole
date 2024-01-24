"""
Proyecto Python y MySql: 
-Abrir asistente
-Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará: crear nota, mostrar notas, borrarlas

"""

print(
    """
Acciones disponibles:

   - registro
   - login
"""
)
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    print("Ok!! Vamos a registrate en el sistema... ")
elif accion == "login":
    print("Vale!! Identifícate en el sistema...")

