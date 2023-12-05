import sqlite3
import os

# Esta es la funcion para crear la base de datos en la ruta deseada y con el nombre deseado
def conectar():
    ruta_db = "../Hito_2/recursos/supermercado.db"

    # Obtener el directorio del archivo y crearlo si no existe
    directorio = os.path.dirname(ruta_db)
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Conectar a la base de datos
    con = sqlite3.connect(ruta_db)
    return con