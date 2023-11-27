"""
Crear un programa que tenga:
- Ventana ✓
- Tamaño fijo ✓
- No redimensionable ✓
- Un menu (inicio, añadir, info, salir) ✓
- Diferentes pantallas ✓
- Formulario de añador productos ✓
- Guardar datos temporalmente ✓
- Mostrar datos listados en la pantalla principal (home) ✓
- Opcion de salir ✓
"""

from tkinter import *
from tkinter import ttk

# Definir ventana
ventana = Tk()
ventana.geometry("800x800")
#ventana.minsize("500x500")
ventana.title("Proyecto Tkinter | Master en Python")
ventana.resizable(0,0)

# Pantallas
def home():
    # Montar pantallas
    home_label.config(
        fg="yellow",
        bg="black",
        font=("Arial",30),
        padx=100,
        pady=20
    )
    home_label.grid(row=0,column=0)

    cajadeproductos.grid(row=2)

    # Listar productos
    """
    for producto in productos:
        if len(producto) == 3:
            producto.append("Añadido")
            Label(cajadeproductos,text=producto[0]).grid()
            Label(cajadeproductos,text=producto[1]).grid()
            Label(cajadeproductos,text=producto[2]).grid()
            Label(cajadeproductos,text="------------------").grid()
     """
    
    for producto in productos:
        if len(producto) == 3:
            producto.append("Añadido")
            cajadeproductos.insert('',0,text=producto[0],values=(producto[1]))


    # Ocultar pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def add():
    # Encabezado
    add_label.config(
        fg="yellow",
        bg="black",
        font=("Arial",30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0,column=0,columnspan=10)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    add_price_label.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    add_price_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    add_descripcion_label.grid(row=3,column=0,padx=5,pady=5,sticky=E)
    add_descripcion_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    add_descripcion_entry.config(
        width=30,
        height=5,
        font=("Times New Roman",12),
        padx=15,
        pady=15
    )

    add_separador.grid(row=4,column=1)

    boton.grid(row=5,column=1,sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="black",
        fg="yellow"
    )

    # Ocultar pantallas
    home_label.grid_remove()
    cajadeproductos.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="yellow",
        bg="black",
        font=("Arial",30),
        padx=100,
        pady=20
    )
    info_label.grid(row=0,column=0)
    data_label.grid(row=1,column=0)

    # Ocultar pantallas
    home_label.grid_remove()
    cajadeproductos.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()

    return True

def add_product():
    productos.append([
        name_data.get(),
        price_data.get(),
        add_descripcion_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_descripcion_entry.delete("1.0",END)

    home()

# Variables impoertantes
productos = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas (inicio)
home_label = Label(ventana, text="Inicio")
#cajadeproductos = Frame(ventana, width=300)

#Label(cajadeproductos).grid(row=0)
Label(ventana).grid(row=1)
cajadeproductos = ttk.Treeview(height=12,columns=2)
cajadeproductos.grid(row=1,column=0,columnspan=2)
cajadeproductos.heading("#0",text='Producto',anchor=W)
cajadeproductos.heading("#1",text='Precio',anchor=W)

# Definir campos de pantallas (Add / Añadir productos)
add_label = Label(ventana, text="Añadir producto")

# Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame,text="Nombre: ")
add_name_entry = Entry(add_frame,textvariable=name_data)

add_price_label = Label(add_frame,text="Precio: ")
add_price_entry = Entry(add_frame,textvariable=price_data)

add_descripcion_label = Label(add_frame,text="Descripcion: ")
add_descripcion_entry = Text(add_frame)

add_separador = Label(add_frame)

boton = Button(add_frame,text="Guardar",command=add_product)

# Definir campos de pantallas (Info)
info_label = Label(ventana, text="Info de la aplicacion")
data_label = Label(ventana,text="Este programa fue creado por Julio Durán en marco a una Master en Python el año 2023")


# Cargar pantalla de inicio
home()

# Crear menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",command=home)
menu_superior.add_command(label="Añadir",command=add)
menu_superior.add_command(label="Info",command=info)
menu_superior.add_command(label="Salir",command=ventana.quit)

# Cargar menu
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()