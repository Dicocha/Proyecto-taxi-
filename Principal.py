from Signin import enUsuario
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pymysql

class App:

    # Modulos Principal
    def Ver_datos(tree):

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "SELECT `Areas`,`Clave`,`Placa`,`Estado`,`Nombre Propietario`,`Nombre Conductor`,`Telefono Propietario`,`Telefono Conductor`,`E-mail Propietario`,`E-mail Conductor`,`Observaciones` FROM `Taxis` WHERE 1" 
        )

        for datos in cursor.fetchall():
            # Insert datos
            tree.insert(parent="", index='end', values=(datos))

        # Guardar cambios.
        conn.commit() 
        conn.close()

    def Cambiar_Area():

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE `Taxis` SET `Areas`= '%d' WHERE `Clave`= '%s'" % (enArea.get(), enClave.get())
        )

        # Guardar cambios.
        conn.commit() 
        conn.close()

    def Borrar_Datos():
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM `Taxis` WHERE `Clave` = '%s'" % (enClave.get())
        )

        # Guardar cambios.
        conn.commit() 
        conn.close()

    def Reflescar():
        for row in tree.get_children():
            tree.delete(row)
        App.Ver_datos(tree)

class Taxi:
        # Interfaz de Taxista
    def TaxistaInterfaz():
        insertT = Toplevel()

        # Declaracion de variables
        global varA, varI, enAreaT, enClaveT, enPlacaT, enEstado, enNomproT, enNomconT, enMarcaT, enModeloT, enTelproT, enTelconT, enCorreoproT, enCorreoconT, enObservacionesT
        enAreaT = StringVar()
        enClaveT = StringVar()
        enPlacaT = StringVar()
        enEstado = StringVar()
        enNomproT = StringVar()
        enNomconT = StringVar()
        enMarcaT = StringVar()
        enModeloT = StringVar()
        enTelproT = StringVar()
        enTelconT = StringVar()
        enCorreoproT = StringVar()
        enCorreoconT = StringVar()
        enObservacionesT = StringVar()
                            
        # Configuracion de la pantalla
        insertT.title('Insertar datos de Taxistas')
        insertT.geometry('1200x1400')
        insertT.configure(bg = 'beige')

        # Hacer un Frame/Panel Para que no se corran los objetos
        frame = Frame(insertT)
        frame.place(x = 0, y = 0, width=2000, height=2000)

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
        Entry(insertT, textvariable= enClaveT).place(x = 50, y = 110, width=400, height=20)
        Entry(insertT, textvariable= enPlacaT).place(x = 50, y = 170, width = 400, height=20)
        Combobox(insertT,textvariable= enEstado, values= ('Activo', 'Inactivo'), state="readonly").place(x=50, y=230,width=400, height=20)
        Entry(insertT, textvariable= enNomproT).place(x = 50, y = 290, width=400, height=20)
        Entry(insertT, textvariable= enNomconT).place(x = 50, y = 350, width=400, height=20)
        Entry(insertT, textvariable= enMarcaT).place(x = 650, y = 50, width=400, height=20)
        Entry(insertT, textvariable= enModeloT).place(x = 650, y = 110, width=400, height=20)
        Entry(insertT, textvariable= enTelproT).place(x = 650, y = 170, width=400, height=20)
        Entry(insertT, textvariable= enTelconT).place(x = 650, y = 230, width=400, height=20)
        Entry(insertT, textvariable= enCorreoproT).place(x = 650, y = 290, width=400, height=20)
        Entry(insertT, textvariable= enCorreoconT).place(x = 650, y = 350, width=400, height=20)
        Entry(insertT, textvariable= enObservacionesT).place(x = 650, y = 410, width=400, height=20)

        # Insertarle botones a la interfaz
        Button(insertT, text='Ingresar', command = Taxi.Insertar_DatosT).place(x = 300, y = 550, width=200, height=40)
        Button(insertT, text='Limpiar', command = Taxi.Limpiar_EntryT).place(x = 550, y = 550, width=200, height=40)
        Button(insertT, text='Regresar', command = insertT.destroy).place(x = 800, y = 550, width=200, height=40)

    # Modulos Taxistas
    def Limpiar_EntryT():
        enAreaT.set('')
        enClaveT.set('')
        enEstado.set('')
        enPlacaT.set('')
        enNomproT.set('')
        enNomconT.set('')
        enMarcaT.set('')
        enModeloT.set('')
        enTelproT.set('')
        enTelconT.set('')
        enCorreoproT.set('')
        enCorreoconT.set('')
        enObservacionesT.set('')

    def Insertar_DatosT():
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Taxis` (`Areas`, `Clave`, `Placa`, `Estado`, `Nombre Propietario`, `Nombre Conductor`, `Marca Radio`, `Modelo Radio`, `Telefono Propietario`, `Telefono Conductor`, `E-mail Propietario`, `E-mail Conductor`, `Observaciones`)\
                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (enAreaT.get(), enClaveT.get(), enPlacaT.get(), enEstado.get(), enNomproT.get(), enNomconT.get(), enMarcaT.get(), enModeloT.get(), enTelproT.get(), enTelconT.get(), enCorreoproT.get(), enCorreoconT.get(), enObservacionesT.get()))
        
        conn.commit()
        conn.close()
        
class Cliente:
    # Interfaz de Clientes
    def ClienteInterfaz():
        insertC = Tk()
        
        # Declaracion de variables
        global enNombreC, enTelCasaC, enTelPerC, enCorreoPerC, enDirecC, enObservacionesC
        enNombreC = StringVar()
        enTelCasaC = IntVar()
        enTelPerC = IntVar()
        enCorreoPerC = StringVar()
        enDirecC = StringVar()
        enObservacionesC = StringVar()

        # Configuracion de la pantalla
        insertC.title('Insertar datos de Clientes')
        insertC.geometry('2000x2000')

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
        treeC = Treeview(insertC, height=10)
        treeC.place(x=500, y=20, width= 700, height= 350)

        treeC['columns'] = ("Clave", "Placa", "Nombre del conductor", "Telefono del conductor")

        # Fomato de las columnas
        treeC.column('#0', width = 0)
        treeC.column('Clave', width = 30, anchor= CENTER)
        treeC.column('Placa', width = 30, anchor= CENTER)
        treeC.column('Nombre del conductor', width = 80, anchor= CENTER)
        treeC.column('Telefono del conductor', width = 80, anchor= CENTER)

        # Create headings
        treeC.heading("#0", text = "", anchor = W)
        treeC.heading('Clave', text= "Clave" , anchor= W)
        treeC.heading('Placa', text= "Placa" , anchor= W)
        treeC.heading('Nombre del conductor', text= "Nom. conductor" , anchor= W)
        treeC.heading('Telefono del conductor', text= "Telefono del conductor" , anchor= W)

        # Modulos
        Cliente.Ver_datosC(treeC)
        Cliente.SeleccionTaxistas(insertC)

        # Insertarle botones a la interfaz
        Button(insertC, text='Ingresar', command = Cliente.Insertar_DatosC).place(x = 300, y = 550, width=200, height=40)
        Button(insertC, text='Limpiar', command = Cliente.Limpiar_EntryC).place(x = 550, y = 550, width=200, height=40)
        Button(insertC, text='Regresar', command = insertC.destroy).place(x = 800, y = 550, width=200, height=40)

    # Modulos de Insertar Clientes
    def Limpiar_EntryC():
        enNombreC.set('')
        enTelCasaC.set('')
        enTelPerC.set('')
        enCorreoPerC.set('')
        enDirecC.set('')
        enObservacionesC.set('')

    def SeleccionTaxistas(insertC):
        global Box
        Box = StringVar()

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")
        curs = conn.cursor()
        curs.execute("SELECT `Clave` FROM `Taxis` WHERE 1")

        results = curs.fetchall()
        curs.close()
        conn.close()

        results_for_combobox = [result[0] for result in results]
        Combobox(insertC, values=results_for_combobox, state="readonly", textvariable= Box).place(x=500, y= 400)

    def Ver_datosC(treeC):
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

    def Insertar_DatosC():
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            
            "INSERT INTO `Cliente` (`Nombre`, `Tel. Casa`, `Tel. Cel`, `Direccion`, `Email`, `Taxista`, `Observaciones`)\
            VALUES ('%s', '%d', '%d', '%s', '%s', '%s', '%s')" % (enNombreC.get(), enTelCasaC.get(), enTelPerC.get(), enDirecC.get(), enCorreoPerC.get(), Box.get() ,enObservacionesC.get())
            )

        conn.commit()
        conn.close()
 
main = Tk()

enClave = StringVar()
enArea = IntVar()

#Formato de la pantalla
main.title('Menu principal')
main.geometry('1200x1400')
main.configure(bg = 'grey')

#Variables
refrescarimg = PhotoImage(file= 'Refresh.gif')

#Frames
frame = LabelFrame(main,text="Opciones de ajuste").place(x=150, y=250, width=1000, height=400)
frame2 = LabelFrame(main,text="Entraste como:").place(x=1150, y=650, width= 200, height= 100)

#Labels
Label(frame, text= 'Area:').place(x=280, y=300, width= 120, height=30)
Label(frame, text= 'Clave:').place(x=500, y=500, width= 130, height=30)
Label(frame2, text= enUsuario.get()).place(x=1160, y=670, width= 130, height=30)

#Entry
Entry(frame, textvariable= enArea).place(x=320, y=305, width=200, height=20)
Entry(frame, textvariable= enClave).place(x = 550, y = 505, width = 200, height=20)

# Declaración y formato del arbol
tree = Treeview(main, height=10)
tree.place(x=0, y=0, width= 300, height= 100)
tree.pack(pady=0)

# Insertar columnas
tree['columns'] = ("Areas","Clave", "Placa", "Estado", "Nombre del propietario", "Nombre del conductor", 
            "Telefono del propietario", "Telefono del conductor", "E-mail Propietario", "E-mail Conductor",
            "Observacion")

# Fomato de las columnas
tree.column('#0', width = 0, minwidth= 25)
tree.column('Areas', width = 60, anchor= CENTER)
tree.column('Clave', width = 60, anchor= CENTER)
tree.column('Placa', width = 60, anchor= W)
tree.column('Estado', width = 60, anchor= W)
tree.column('Nombre del propietario', width = 200, anchor= W)
tree.column('Nombre del conductor', width = 200, anchor= W)
tree.column('Telefono del propietario', width = 125, anchor= W)
tree.column('Telefono del conductor', width = 125, anchor= W)
tree.column('E-mail Propietario', width = 200, anchor= W)
tree.column('E-mail Conductor', width = 200, anchor= W)
tree.column('Observacion', width = 500, anchor= W)

# Create headings
tree.heading("#0", text = "", anchor = W)
tree.heading('Areas', text= "Areas" , anchor= W)
tree.heading('Clave', text= "Clave" , anchor= W)
tree.heading('Placa', text= "Placa" , anchor= W)
tree.heading('Estado', text= "Estado" , anchor= W)
tree.heading('Nombre del propietario', text= "Nom. propietario" , anchor= W)
tree.heading('Nombre del conductor', text= "Nom. conductor" , anchor= W)
tree.heading('Telefono del propietario', text= "Tel. propietario" , anchor= W)
tree.heading('Telefono del conductor', text= "Tel. conductor" , anchor= W)
tree.heading('E-mail Propietario', text= "E-mail Propietario" , anchor= W)
tree.heading('E-mail Conductor', text= "E-mail Conductor" , anchor= W)
tree.heading('Observacion', text= "Observacion" , anchor= W)

App.Ver_datos(tree)

# Scrollbar
scrollY = Scrollbar(main, orient="vertical", command= tree.yview)
scrollY.place(x=2, y=2, width=20, height=220)
scrollY.configure(command=tree.yview)

scrollX = Scrollbar(main, orient="horizontal", command= tree.xview)
scrollX.place(x=20, y=220, width=1270, height=20)
scrollX.configure(command=tree.xview)

# Botones
Button(main, image= refrescarimg, command= App.Reflescar).place(x=1100, y=275, width= 30, height= 30)
Button(main, text= 'Cambiar', command = App.Cambiar_Area).place(x=175, y=300, width=80, height=30)
Button(main, text= 'Eliminar', command = App.Borrar_Datos).place(x=175, y=350, width=80, height=30)
Button(main, text= 'Salir', command = exit).place(x = 300, y = 550, width=200, height=40)
Button(main, text= 'Insertar Taxi', command = Taxi.TaxistaInterfaz).place(x = 550, y = 550, width=200, height=40)
Button(main, text= 'Insertar Cliente', command = Cliente.ClienteInterfaz).place(x = 800, y = 550, width=200, height=40)


main.mainloop()