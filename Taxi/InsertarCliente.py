from tkinter.ttk import *
from tkinter import *
import pymysql

def ClienteInterfaz():
    insertC = Tk()
    
    # Declaracion de variables 
    enNombreC = StringVar()
    enTelCasaC = IntVar()
    enTelPerC = IntVar()
    enCorreoPerC = StringVar()
    enDirecC = StringVar()
    enObservacionesC = StringVar()

    # Configuracion de la pantalla
    insertC.title('Insertar datos de Clientes')
    insertC.geometry('1400x1200')
    insertC.configure(bg = 'beige')

    # Insertarle etiquetas a la interfaz 
    Label(insertC, text= 'Nombre').place(x = 10, y = 20, width = 200, height=20)
    Label(insertC, text= 'Telefono del la casa').place(x = 10, y = 80, width = 200, height=20)
    Label(insertC, text= 'Telefono personal').place(x = 10, y = 140, width = 200, height=20) 
    Label(insertC, text= 'Direccion').place(x = 10, y = 200, width=200, height=20)
    Label(insertC, text= 'Correo electronico').place(x = 10, y = 260, width=200, height=20)
    Label(insertC, text= 'Observaciones').place(x = 10, y = 320, width=200, height=20)

    # Con esta parte se puede insertar datos
    Entry(insertC, textvariable= enNombreC).place(x = 50, y = 50, width=400, height=20)
    Entry(insertC, textvariable= enTelCasaC).place(x = 50, y = 110, width=400, height=20)
    Entry(insertC, textvariable= enTelPerC).place(x = 50, y = 170, width=400, height=20)
    Entry(insertC, textvariable= enDirecC).place(x = 50, y = 230, width=400, height=20)
    Entry(insertC, textvariable= enCorreoPerC).place(x = 50, y = 290, width=400, height=20)
    Entry(insertC, textvariable= enObservacionesC).place(x = 50, y = 350, width=400, height=20)

    # Treview
    treeC = Treeview(insertC, height=100)
    treeC.place(x=500, y=20, width= 700, height= 350)

    treeC['columns'] = ("Clave", "Placa", "Nombre del conductor", "Telefono del conductor")

    # Fomato de las columnas
    treeC.column('#0', width = 0)
    treeC.column('Clave', width = 20, anchor= CENTER)
    treeC.column('Placa', width = 20, anchor= CENTER)
    treeC.column('Nombre del conductor', width = 70, anchor= CENTER)
    treeC.column('Telefono del conductor', width = 70, anchor= CENTER)

    # Create headings
    treeC.heading("#0", text = "", anchor = W)
    treeC.heading('Clave', text= "Clave" , anchor= W)
    treeC.heading('Placa', text= "Placa" , anchor= W)
    treeC.heading('Nombre del conductor', text= "Nom. conductor" , anchor= W)
    treeC.heading('Telefono del conductor', text= "Telefono del conductor" , anchor= W)

    # Modulos
    def Ver_datosC():

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "SELECT `Clave`,`Placa`,`Nombre Conductor`,`Telefono Conductor` FROM `Taxis` WHERE 1" 
        )

        for datos in cursor.fetchall():
            # Un combobox para ver a que taxista quiere insrtarle
            treeC.insert(parent="", index='end', values=(datos))
            
        # Guardar cambios.
        conn.commit() 
        conn.close()

    def Limpiar_EntryC(): #No sirve
        print("Hola")

    def Insertar_DatosC():#No sirve

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Cliente` (`Nombre`, `Tel. Casa`, `Tel. Cel`, `Direccion`, `Email`, `Observaciones`) \
            VALUES ('%s', '%d', '%d', '%s', '%s', '%s')" % (enNombreC.get(), enTelCasaC.get(), enTelPerC.get(), enDirecC.get(), enCorreoPerC.get(), enObservacionesC.get())
        )
        conn.commit()
        conn.close()

    Ver_datosC()

    #Checkbox
    Combobox(insertC, values= treeC.item, state= 'readonly').place(x=500, y=400, width=200, height=20)

    # Insertarle botones a la interfaz
    Button(insertC, text='Ingresar', command = Insertar_DatosC).place(x = 300, y = 550, width=200, height=40)
    Button(insertC, text='Limpiar', command = Limpiar_EntryC).place(x = 550, y = 550, width=200, height=40)
    Button(insertC, text='Regresar', command = insertC.destroy).place(x = 800, y = 550, width=200, height=40)
