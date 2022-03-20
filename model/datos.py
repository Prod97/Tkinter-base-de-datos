from .conexiondb import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexcion = ConexionDB()
    sqlite = """
CREATE TABLE datos(

    ID INTEGER,
    Name VARCHAR(100),
    Last_name VARCHAR(100),
    Dui VARCHAR(100),
    Number_Phone VARCHAR(100),
    Email VARCHAR(100),
    PRIMARY KEY(ID AUTOINCREMENT))
    """

    try:
        conexcion.cursor.execute(sqlite)
        conexcion.cerrar()
        mensaje = "Se creo la tabla"
        messagebox.showinfo("Creacion", mensaje)
    except:
        messagebox.showerror("Error", "La tabla ya esta creada")
            


def borrar_tabla():
    conexcion = ConexionDB()
    sqlite = "DROP TABLE datos"
    try:
        conexcion.cursor.execute(sqlite)
        conexcion.cerrar()
        messagebox.showinfo("Borrar", "La tabla de la base de datos se borro exitosamente")
    except:
        titulo = "Error"
        messagebox.showerror(titulo, "No hay tabla de base de datos que borrar")