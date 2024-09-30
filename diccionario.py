# Crear un Diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
# Accedemos al valor asociado con la clave "ciudad" y lo modificamos
informacion_personal["ciudad"] = "Barcelona"

# Agregamos una nueva clave-valor para representar la profesión de la persona
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar Existencia de Claves
# Comprobamos si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, la agregamos con un número de teléfono ficticio
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar una Clave
# Eliminamos la clave "edad" del diccionario, ya que esa información no es necesaria
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("Información Personal Final:")
print(informacion_personal)
