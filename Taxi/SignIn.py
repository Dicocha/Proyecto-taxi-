from tkinter import *
from pymysql import *
import pymysql

Signin = Tk()

Signin.title('Inicio de sesion')
Signin.geometry('400x200')
Signin.resizable(width=0, height=0)
Signin.configure(bg = 'beige')

# Hacer un Frame/Panel Para que no se corran los objetos
frame = Frame(Signin)
frame.place(x = 20, y = 30, width=1000, height=1000)
frame.configure(bg = 'beige')

# Insertarle etiquetas a la interfaz
Usuario = Label(Signin, text = "Nombre completo:").place(x = 20, y = 30, width=60, height=30)
Contraseña = Label(Signin, text = "Contraseña:").place(x = 20,y = 60, width=80, height=30)

# Con esta parte se puede insertar datos
Entry(Signin).place(x = 50, y = 50, width=400, height=20)
Entry(Signin, text = 'Cédula').place(x = 50, y = 110, width=400, height=20)

def Confirmarusuario():
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "" 
        )

        # Guardar cambios.
        conn.commit() 
        conn.close()

# Insertarle botones a la interfaz
Button(Signin, text='Exit', command = Confirmarusuario).place(x = 300, y = 120, width=80, height=30)
