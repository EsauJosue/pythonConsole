"""
Proyecto Python y MySql: 
-Abrir asistente
-Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará: crear nota, mostrar notas, borrarlas

"""
from usuarios import acciones

print(
    """
Acciones disponibles:

   - registro
   - login
"""
)
hazEl = acciones.Opciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
   hazEl.registro()
elif accion == "login":
   hazEl.login()
   


