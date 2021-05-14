from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql

def Centrarlapantalla():
    ancho_ventana = 400
    alto_ventana = 200

    x_ventana = Signin.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = Signin.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    Signin.geometry(posicion)

    Signin.resizable(0,0)

Signin = Tk() 
enUsuario = StringVar()
enContrasena = StringVar()

Signin.title('Inicio de sesion')
Signin.wm_attributes('-type', 'splash')
Centrarlapantalla()
frame = Frame(Signin)
frame.place(x = 0, y = 0, width=2000, height=2000)

# Insertarle etiquetas a la interfaz
Usuario = Label(Signin, text = "Usuario:").place(x = 20, y = 50, width=60, height=30)
Contraseña = Label(Signin, text = "Contraseña:").place(x = 20,y = 100, width=80, height=30)

# Con esta parte se puede insertar datos
Entry(Signin, textvariable=enUsuario).place(x = 120, y = 53, width=200, height=20)
Entry(Signin, textvariable=enContrasena, show= "*").place(x = 120, y = 103, width=200, height=20)

def Confirmarusuario():
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Usuarios WHERE`Usuario` = '%s' AND `Contraseña` = '%s'" % (enUsuario.get(), enContrasena.get()) 
        )
        if cursor.fetchall():
            messagebox.showinfo(title="Bienvenido", message='Credenciales correctas')
            Signin.destroy()

        else:
            messagebox.showinfo(title="Error", message='Las credenciales no son correctas')

        # Guardar cambios.
        conn.commit() 
        conn.close()

# Insertarle botones a la interfaz
Button(Signin, text='Ingresar', command = Confirmarusuario).place(x = 300, y = 150, width=80, height=30)

Signin.mainloop()