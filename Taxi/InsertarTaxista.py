from tkinter.ttk import *
from tkinter import *
import pymysql

def TaxistasIntefaz():

    insertT = Tk()

    # Declaracion de variables
    varA = IntVar()
    varI = IntVar()
    enAreaT = StringVar()
        
    # Configuracion de la pantalla
    insertT.title('Insertar datos de Taxistas')
    insertT.geometry('1200x1400')
    insertT.configure(bg = 'beige')

    # Hacer un Frame/Panel Para que no se corran los objetos
    frame = Frame(insertT)
    frame.place(x = 20, y = 30, width=1000, height=1000)
    frame.configure(bg = 'beige')

    # Insertarle etiquetas a la interfaz
    Label(insertT, text= 'Area').place(x = 10, y = 20, width = 100, height=20)
    Label(insertT, text= 'Clave').place(x = 10, y = 80, width = 100, height=20)
    Label(insertT, text= 'Placa').place(x = 10, y = 140, width = 100, height=20)
    Label(insertT, text= 'Estado').place(x = 10, y = 200, width=200, height=20)# Checklist
    Label(insertT, text= 'Nombre del propietario').place(x = 10, y = 260, width=200, height=20)
    Label(insertT, text= 'Nombre del conductor').place(x = 10, y = 320, width=200, height=20)
    Label(insertT, text= 'Marca del radio').place(x = 600, y = 20, width=200, height=20)
    Label(insertT, text= 'Modelo del radio').place(x = 600, y = 80, width=200, height=20)
    Label(insertT, text= 'Telefono del propietario').place(x = 600, y = 140, width=200, height=20)
    Label(insertT, text= 'Telefono del conductor').place(x = 600, y = 200, width=250, height=20)
    Label(insertT, text= 'Correo electronico del propietario').place(x = 600, y = 260, width=250, height=20)
    Label(insertT, text= 'Correo electronico del conductor').place(x = 600, y = 320, width=250, height=20)
    Label(insertT, text= 'Observaciones').place(x = 600, y = 380, width=200, height=20)

    # Con esta parte se puede insertar datos
    Entry(insertT, textvariable= enAreaT).place(x = 50, y = 50, width=400, height=20)
    Entry(insertT).place(x = 50, y = 110, width=400, height=20)
    Entry(insertT).place(x = 50, y = 170, width = 400, height=20)
    Checkbutton(insertT, text= 'Activo', variable= varA).place(x = 50, y = 230, width=100, height=20)
    Checkbutton(insertT, text= 'Inactivo', variable= varI).place(x = 250, y = 230, width = 100, height=20)
    Entry(insertT).place(x = 50, y = 290, width=400, height=20)
    Entry(insertT).place(x = 50, y = 350, width=400, height=20)
    Entry(insertT).place(x = 650, y = 50, width=400, height=20)
    Entry(insertT).place(x = 650, y = 110, width=400, height=20)
    Entry(insertT).place(x = 650, y = 170, width=400, height=20)
    Entry(insertT).place(x = 650, y = 230, width=400, height=20)
    Entry(insertT).place(x = 650, y = 290, width=400, height=20)
    Entry(insertT).place(x = 650, y = 350, width=400, height=20)
    Entry(insertT).place(x = 650, y = 410, width=400, height=20)

    # Modulos
    def Estadoif():
        if(varA.get() == True) and (varI.get() == False):
            Estado = print('Activo')

        elif(varA.get() == False) and (varI.get() == False): 
            Estado = print('No seleccionó ninguna opción')

        elif(varA.get() == True) and (varI.get() == True): 
            Estado = print('Solo Se puede seleccionar una')

        else:
            Estado = print('Inactivo')

    def Limpiar_EntryT(): #No sirve
        print(enAreaT.get())

    def Insertar_DatosT(): #No sirve

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")
        Query = "INSERT INTO `Taxis` (`Areas`, `Clave`, `Placa`, `Estado`, `Nombre Propietario`, `Nombre Conductor`, `Marca Radio`, `Modelo Radio`, `Telefono Propietario`, `Telefono Conductor`, `E-mail Propietario`, `E-mail Conductor`, `Observaciones`) VALUES (); )"

        cursor = conn.cursor()
        cursor.execute(Query)

        conn.commit()
        conn.close()

    def imprimir():
        print(enAreaT.get())

    # Insertarle botones a la interfaz
    Button(insertT, text='Ingresar', command = imprimir).place(x = 300, y = 550, width=200, height=40)
    Button(insertT, text='Limpiar', command = Limpiar_EntryT).place(x = 550, y = 550, width=200, height=40)
    Button(insertT, text='Regresar', command = insertT.destroy).place(x = 800, y = 550, width=200, height=40)
