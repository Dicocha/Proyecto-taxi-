from InsertarCliente import *
from InsertarTaxista import *
from tkinter import *
from tkinter.ttk import *
import pymysql

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
    Ver_datos(tree)

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

#Labels
Label(frame, text= 'Area:').place(x= 275, y=300, width= 120, height=30)
Label(frame, text= 'Clave:').place(x=500, y=500, width= 130, height=30)

#Entry
Entry(frame, textvariable= enArea).place(x=320, y=305, width=200, height=20)
Entry(frame, textvariable= enClave).place(x = 550, y = 505, width = 200, height=20)


# Declaración y formato del arbol
tree = Treeview(main, height=10)
tree.place(x=25, y=50, width= 200, height= 100)
tree.pack(pady=20)

# Insertar columnas
tree['columns'] = ("Areas","Clave", "Placa", "Estado", "Nombre del propietario", "Nombre del conductor", 
    "Telefono del propietario", "Telefono del conductor", "E-mail Propietario", "E-mail Conductor",
    "Observacion", "0")

# Fomato de las columnas
tree.column('#0', width = 0, minwidth= 25)
tree.column('Areas', width = 60, anchor= CENTER)
tree.column('Clave', width = 60, anchor= CENTER)
tree.column('Placa', width = 60, anchor= CENTER)
tree.column('Estado', width = 60, anchor= CENTER)
tree.column('Nombre del propietario', width = 135, anchor= CENTER)
tree.column('Nombre del conductor', width = 130, anchor= CENTER)
tree.column('Telefono del propietario', width = 130, anchor= CENTER)
tree.column('Telefono del conductor', width = 120, anchor= CENTER)
tree.column('E-mail Propietario', width = 145, anchor= CENTER)
tree.column('E-mail Conductor', width = 140, anchor= CENTER)
tree.column('Observacion', width = 130, anchor= CENTER)
tree.column('0', width = 0, anchor= CENTER)

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
tree.heading('0', text= "" , anchor= W)

Ver_datos(tree)

# Scrollbar
scrollY = Scrollbar(main, orient="vertical", command=tree.yview)
scrollY.place(x=1010+200+2, y=21, width=19, height=200+20)
scrollY.configure(command=tree.yview)

# Botones
Button(main, image= refrescarimg, command= Reflescar).place(x=1100, y=275, width= 30, height= 30)
Button(main, text= 'Cambiar', command = Cambiar_Area).place(x=175, y=300, width=80, height=30)
Button(main, text= 'Eliminar', command = Borrar_Datos).place(x=175, y=350, width=80, height=30)
Button(main, text= 'Salir', command = exit).place(x = 300, y = 550, width=200, height=40)
Button(main, text= 'Insertar Taxi', command = TaxistasIntefaz).place(x = 550, y = 550, width=200, height=40)
Button(main, text= 'Insertar Cliente', command = ClienteInterfaz).place(x = 800, y = 550, width=200, height=40)

main.mainloop()