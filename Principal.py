from Signin import enUsuario
import tkinter as tk
from tkinter import ttk
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
            tree.insert(parent="", index='end', values=datos)

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
        insertT = tk.Toplevel()

        # Declaracion de variables
        global varA, varI, enAreaT, enClaveT, enPlacaT, enEstado, enNomproT, enNomconT, enMarcaT, enModeloT, enTelproT, enTelconT, enCorreoproT, enCorreoconT, enObservacionesT
        enAreaT = tk.StringVar()
        enClaveT = tk.StringVar()
        enPlacaT = tk.StringVar()
        enEstado = tk.StringVar()
        enNomproT = tk.StringVar()
        enNomconT = tk.StringVar()
        enMarcaT = tk.StringVar()
        enModeloT = tk.StringVar()
        enTelproT = tk.StringVar()
        enTelconT = tk.StringVar()
        enCorreoproT = tk.StringVar()
        enCorreoconT = tk.StringVar()
        enObservacionesT = tk.StringVar()

        # Configuracion de la pantalla
        insertT.title('Insertar datos de Taxistas')
        insertT.geometry('1200x1400')
        insertT.configure(bg='#17202A')

        #Style
        styleT = ttk.Style(insertT)
        styleT.theme_use('alt')   
        styleT.configure("TCombobox", background ='#566573', fieldbackground='#566573', selectbackground= '#566573')
        styleT.map('TCombobox', fieldbackground=[('readonly', '#566573')])
        insertT.option_add( '*TCombobox*Listbox.background', '#566573')

        # Label
        tk.Label(insertT, background= '#566573', text= 'Area').place(x = 10, y = 20, width = 100, height=20)
        tk.Label(insertT, background= '#566573', text= 'Clave').place(x = 10, y = 80, width = 100, height=20)
        tk.Label(insertT, background= '#566573', text= 'Placa').place(x = 10, y = 140, width = 100, height=20)
        tk.Label(insertT, background= '#566573', text= 'Estado').place(x = 10, y = 200, width=200, height=20)# Checklist
        tk.Label(insertT, background= '#566573', text= 'Nombre del propietario').place(x = 10, y = 260, width=200, height=20)
        tk.Label(insertT, background= '#566573', text= 'Nombre del conductor').place(x = 10, y = 320, width=200, height=20)
        tk.Label(insertT, background= '#566573', text= 'Marca del radio').place(x = 600, y = 20, width=200, height=20)
        tk.Label(insertT, background= '#566573', text= 'Modelo del radio').place(x = 600, y = 80, width=200, height=20)
        tk.Label(insertT, background= '#566573', text= 'Telefono del propietario').place(x = 600, y = 140, width=200, height=20)
        tk.Label(insertT, background= '#566573', text= 'Telefono del conductor').place(x = 600, y = 200, width=250, height=20)
        tk.Label(insertT, background= '#566573', text= 'Correo electronico del propietario').place(x = 600, y = 260, width=250, height=20)
        tk.Label(insertT, background= '#566573', text= 'Correo electronico del conductor').place(x = 600, y = 320, width=250, height=20)
        tk.Label(insertT, background= '#566573', text= 'Observaciones').place(x = 600, y = 380, width=200, height=20)

        # Entry
        tk.Entry(insertT, background= '#566573', textvariable= enAreaT).place(x = 50, y = 50, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enClaveT).place(x = 50, y = 110, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enPlacaT).place(x = 50, y = 170, width = 400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enNomproT).place(x = 50, y = 290, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enNomconT).place(x = 50, y = 350, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enMarcaT).place(x = 650, y = 50, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enModeloT).place(x = 650, y = 110, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enTelproT).place(x = 650, y = 170, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enTelconT).place(x = 650, y = 230, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enCorreoproT).place(x = 650, y = 290, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enCorreoconT).place(x = 650, y = 350, width=400, height=20)
        tk.Entry(insertT, background= '#566573', textvariable= enObservacionesT).place(x = 650, y = 410, width=400, height=20)
        
        # Combobox
        Combobox(insertT, textvariable= enEstado, values= ('Activo', 'Inactivo'), state="readonly").place(x=50, y=230,width=400, height=20)
        
        # Botones
        tk.Button(insertT, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Ingresar', command = Taxi.Insertar_DatosT).place(x = 300, y = 550, width=200, height=40)
        tk.Button(insertT, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Limpiar', command = Taxi.Limpiar_EntryT).place(x = 550, y = 550, width=200, height=40)
        tk.Button(insertT, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Regresar', command = insertT.destroy).place(x = 800, y = 550, width=200, height=40)

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
        insertC = tk.Tk()
        
        # Declaracion de variables
        global enNombreC, enTelCasaC, enTelPerC, enCorreoPerC, enDirecC, enObservacionesC
        enNombreC = tk.StringVar()
        enTelCasaC = tk.IntVar()
        enTelPerC = tk.IntVar()
        enCorreoPerC = tk.StringVar()
        enDirecC = tk.StringVar()
        enObservacionesC = tk.StringVar()

        # Configuracion de la pantalla
        insertC.title('Insertar datos de Clientes')
        insertC.geometry('2000x2000')
        insertC.configure(bg='#17202A')

        # Insertarle etiquetas a la interfaz 
        tk.Label(insertC, background= '#566573', text= 'Nombre').place(x = 10, y = 20, width = 200, height=20)
        tk.Label(insertC, background= '#566573', text= 'Telefono del la casa').place(x = 10, y = 80, width = 200, height=20)
        tk.Label(insertC, background= '#566573', text= 'Telefono personal').place(x = 10, y = 140, width = 200, height=20) 
        tk.Label(insertC, background= '#566573', text= 'Direccion').place(x = 10, y = 200, width=200, height=20)
        tk.Label(insertC, background= '#566573', text= 'Correo electronico').place(x = 10, y = 260, width=200, height=20)
        tk.Label(insertC, background= '#566573', text= 'Observaciones').place(x = 10, y = 320, width=200, height=20)
        tk.Label(insertC, background= '#566573', text= 'Taxista').place(x = 10, y = 380, width=200, height=20)

        # Con esta parte se puede insertar datos
        tk.Entry(insertC, background= '#566573', textvariable= enNombreC).place(x = 50, y = 50, width=400, height=20)
        tk.Entry(insertC, background= '#566573', textvariable= enTelCasaC).place(x = 50, y = 110, width=400, height=20)
        tk.Entry(insertC, background= '#566573', textvariable= enTelPerC).place(x = 50, y = 170, width=400, height=20)
        tk.Entry(insertC, background= '#566573', textvariable= enDirecC).place(x = 50, y = 230, width=400, height=20)
        tk.Entry(insertC, background= '#566573', textvariable= enCorreoPerC).place(x = 50, y = 290, width=400, height=20)
        tk.Entry(insertC, background= '#566573', textvariable= enObservacionesC).place(x = 50, y = 350, width=400, height=20)

        # Treview
        treeC = Treeview(insertC, height=10)
        treeC.place(x=500, y=20, width= 700, height= 350)

        treeC['columns'] = ("Clave", "Placa", "Nombre del conductor", "Telefono del conductor")

        # Fomato de las columnas
        treeC.column('#0', width = 0)
        treeC.column('Clave', width = 100, anchor= tk.CENTER)
        treeC.column('Placa', width = 100, anchor= tk.CENTER)
        treeC.column('Nombre del conductor', width = 200, anchor= tk.CENTER)
        treeC.column('Telefono del conductor', width = 200, anchor= tk.CENTER)

        # Create headings
        treeC.heading("#0", text = "", anchor = tk.CENTER)
        treeC.heading('Clave', text= "Clave" , anchor= tk.CENTER)
        treeC.heading('Placa', text= "Placa" , anchor= tk.CENTER)
        treeC.heading('Nombre del conductor', text= "Nom. conductor" , anchor= tk.CENTER)
        treeC.heading('Telefono del conductor', text= "Telefono del conductor" , anchor= tk.CENTER)

        # Scrollbar
        scrollYC = Scrollbar(insertC, orient="vertical", command= treeC.yview)
        scrollYC.place(x=502, y=20, width=20, height=350)
        scrollYC.configure(command=treeC.yview)

        scrollXC = Scrollbar(insertC, orient="horizontal", command= treeC.xview)
        scrollXC.place(x=520, y=350, width=675, height=20)
        scrollXC.configure(command=treeC.xview)

        #Style
        styleC = ttk.Style(insertC)
        styleC.theme_use("alt")
        styleC.configure("Treeview", background='#566573', 
                        fieldbackground='#17202A', foreground="black")

        styleC = ttk.Style(insertC)
        styleC.theme_use("alt")
        styleC.configure("Treeview.Heading", background='#566573', darkcolor="#17202A", lightcolor="#566573",
                        troughcolor="#566573", bordercolor="#17202A")

        styleS = ttk.Style(insertC)
        styleS.theme_use('alt')
        styleS.configure("Horizontal.TScrollbar", gripcount=0,
                        background='#566573', darkcolor="#17202A", lightcolor="#566573",
                        troughcolor="#566573", bordercolor="#17202A", arrowcolor="#17202A")

        styleS = ttk.Style(insertC)
        styleS.theme_use('alt')
        styleS.configure("Vertical.TScrollbar", gripcount=0,
                        background='#566573', darkcolor="#17202A", lightcolor="#566573",
                        troughcolor="#566573", bordercolor="#17202A", arrowcolor="#17202A")

        styleC = ttk.Style(insertC)
        styleC.theme_use("alt")
        styleC.configure("TCombobox", background='#566573', darkcolor="#17202A", lightcolor="#566573",
                        troughcolor="#566573", bordercolor="#17202A", arrowcolor="#17202A")

        styleT = ttk.Style(insertC)
        styleT.theme_use('alt')   
        styleT.configure("TCombobox", background ='#566573', fieldbackground='#566573', selectbackground= '#566573')
        styleT.map('TCombobox', fieldbackground=[('readonly', '#566573')])
        insertC.option_add( '*TCombobox*Listbox.background', '#566573')

        # Modulos
        Cliente.Ver_datosC(treeC)
        Cliente.SeleccionTaxistas(insertC)

        # Insertarle botones a la interfaz
        tk.Button(insertC, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Ingresar', command = Cliente.Insertar_DatosC).place(x = 300, y = 550, width=200, height=40)
        tk.Button(insertC, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Limpiar', command = Cliente.Limpiar_EntryC).place(x = 550, y = 550, width=200, height=40)
        tk.Button(insertC, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text='Regresar', command = insertC.destroy).place(x = 800, y = 550, width=200, height=40)

    # Modulos de Insertar Clientes
    def Limpiar_EntryC():
        enNombreC.set('')
        enTelCasaC.set('')
        enTelPerC.set('')
        enCorreoPerC.set('')
        enDirecC.set('')
        enObservacionesC.set('')

    def SeleccionTaxistas(insertC):
        Box = tk.StringVar()

        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")
        curs = conn.cursor()
        curs.execute("SELECT `Clave` FROM `Taxis` WHERE 1")

        results = curs.fetchall()
        curs.close()
        conn.close()

        results_for_combobox = [result[0] for result in results]
        ttk.Combobox(insertC, values=results_for_combobox,state="readonly", textvariable= Box).place(x=50, y = 410, width=400, height=20)

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

    def Insertar_DatosC(Box):
        conn = pymysql.connect(host="localhost", port=3306, user="dicocha", passwd="dcc82002", db="Taxis")

        cursor = conn.cursor()
        cursor.execute(
            
            "INSERT INTO `Cliente` (`Nombre`, `Tel. Casa`, `Tel. Cel`, `Direccion`, `Email`, `Taxista`, `Observaciones`)\
            VALUES ('%s', '%d', '%d', '%s', '%s', '%s', '%s')" % (enNombreC.get(), enTelCasaC.get(), enTelPerC.get(), enDirecC.get(), enCorreoPerC.get(), Box.get() ,enObservacionesC.get())
            )

        conn.commit()
        conn.close()
        
main = tk.Tk()

enClave = tk.StringVar()
enArea = tk.IntVar()

#Formato de la pantalla
main.title('Menu principal')
main.geometry('1200x1400')
main.configure(bg='#17202A')

#Variables
refrescarimg = tk.PhotoImage(file= 'Refresh.gif')

#Labels                                                    
tk.Label(main, background= '#566573', text= 'Area:').place(x=450, y=500, width= 120, height=30)
tk.Label(main, background= '#566573', text= 'Clave:').place(x=450, y=550, width= 120, height=30)
tk.Label(main, background= '#566573', text= enUsuario.get()).place(x=1160, y=670, width= 130, height=30)

#Entry
tk.Entry(main, background= '#566573', textvariable= enArea).place(x=650, y=500, width=200, height=20)
tk.Entry(main, background= '#566573', textvariable= enClave).place(x= 650, y= 550, width= 200, height=20)

# Declaración y formato del arbol
tree = Treeview(main, height=10)
tree.place(x=0, y=0, width= 1300, height= 450)

# Insertar columnas
tree['columns'] = ("Areas","Clave", "Placa", "Estado", "Nombre del propietario", "Nombre del conductor", 
    "Telefono del propietario", "Telefono del conductor", "E-mail Propietario", "E-mail Conductor", "Observacion")

# Fomato de las columnas
tree.column('#0', width = 0, minwidth= 25)
tree.column('Areas', width = 60, anchor= tk.CENTER)
tree.column('Clave', width = 60, anchor= tk.CENTER)
tree.column('Placa', width = 60, anchor= tk.CENTER)
tree.column('Estado', width = 60, anchor= tk.CENTER)
tree.column('Nombre del propietario', width = 200, anchor= tk.CENTER)
tree.column('Nombre del conductor', width = 200, anchor= tk.CENTER)
tree.column('Telefono del propietario', width = 200, anchor= tk.CENTER)
tree.column('Telefono del conductor', width = 200, anchor= tk.CENTER)
tree.column('E-mail Propietario', width = 200, anchor= tk.CENTER)
tree.column('E-mail Conductor', width = 200, anchor= tk.CENTER)
tree.column('Observacion', width = 500, anchor= tk.W)

# Create headings
tree.heading("#0", text = "", anchor = tk.CENTER)
tree.heading('Areas', text= "Areas" , anchor= tk.CENTER)
tree.heading('Clave', text= "Clave" , anchor= tk.CENTER)
tree.heading('Placa', text= "Placa" , anchor= tk.CENTER)
tree.heading('Estado', text= "Estado" , anchor= tk.CENTER)
tree.heading('Nombre del propietario', text= "Nom. propietario" , anchor= tk.CENTER)
tree.heading('Nombre del conductor', text= "Nom. conductor" , anchor= tk.CENTER)
tree.heading('Telefono del propietario', text= "Tel. propietario" , anchor= tk.CENTER)
tree.heading('Telefono del conductor', text= "Tel. conductor" , anchor= tk.CENTER)
tree.heading('E-mail Propietario', text= "E-mail Propietario" , anchor= tk.CENTER)
tree.heading('E-mail Conductor', text= "E-mail Conductor" , anchor= tk.CENTER)
tree.heading('Observacion', text= "Observacion" , anchor= tk.W)

App.Ver_datos(tree)

# Scrollbar
scrollY = Scrollbar(main, orient="vertical", command= tree.yview)
scrollY.place(x=2, y=2, width=20, height=450)
scrollY.configure(command=tree.yview)

scrollX = Scrollbar(main, orient="horizontal", command= tree.xview)
scrollX.place(x=20, y=450, width=1275, height=20)
scrollX.configure(command=tree.xview)

# Color Treeview
styleT = ttk.Style(main)
styleT.theme_use("alt")
styleT.configure("Treeview", background='#566573', 
                fieldbackground='#17202A', foreground="black")

styleT = ttk.Style(main)
styleT.theme_use("alt")
styleT.configure("Treeview.Heading", background='#566573', 
                fieldbackground='#17202A', foreground="black")

styleS = ttk.Style(main)
styleS.theme_use('alt')
styleS.configure("Horizontal.TScrollbar", gripcount=0,
                background='#566573', darkcolor="#17202A", lightcolor="#566573",
                troughcolor="#566573", bordercolor="#17202A", arrowcolor="#17202A")

styleS = ttk.Style(main)
styleS.theme_use('alt')
styleS.configure("Vertical.TScrollbar", gripcount=0,
                background='#566573', darkcolor="#17202A", lightcolor="#566573",
                troughcolor="#566573", bordercolor="#17202A", arrowcolor="#17202A")

# Botones
tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", image= refrescarimg, command= App.Reflescar).place(x=1160, y=500, width= 30, height= 30)
tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text= 'Cambiar', command = App.Cambiar_Area).place(x=1160, y=550, width=80, height=30)
tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text= 'Eliminar', command = App.Borrar_Datos).place(x=1160, y=600, width=80, height=30)

tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text= 'Salir', command = exit).place(x = 50, y = 500, width=200, height=40)
tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text= 'Insertar Taxi', command = Taxi.TaxistaInterfaz).place(x = 50, y = 550, width=200, height=40)
tk.Button(main, background= '#566573', activeforeground='#2C3E50', cursor="hand2", text= 'Insertar Cliente', command = Cliente.ClienteInterfaz).place(x = 50, y = 600, width=200, height=40)

main.mainloop()