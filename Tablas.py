import customtkinter as ctk
import tkinter as tk
import FuncionesGenerales as fg
import FuncionesMysql as fm
from tkinter import messagebox

#Una funcion para quitar la ventana
def volver(window):
    window.destroy()


#Una funcion para pedir los datos de la tabla deseada
def insertar(tabla):
    vinsertar = ctk.CTk()
    ctk.set_appearance_mode("dark")
    fg.center_window(vinsertar)
    vinsertar.title("Insertar registro")
    if tabla == 0:
        ctk.CTkLabel(vinsertar, text="").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="Categoria").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        entry1 = ctk.CTkEntry(vinsertar)
        entry1.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")
        button2 = ctk.CTkButton(vinsertar, text="Insertar", fg_color="green", hover_color="#005000",
                                command=lambda: insertCategoria(entry1.get()))
        button2.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        button3 = ctk.CTkButton(vinsertar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                                command=vinsertar.destroy)
        button3.grid(row=8, column=4, padx=10, pady=10, sticky="w")
    elif tabla == 1:
        valores = fm.obtenerCampo("categoria", "idcategoria")
        valores = [str(valor) for valor in valores]
        print(valores)
        ctk.CTkLabel(vinsertar, text="").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="Nombre").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry1 = ctk.CTkEntry(vinsertar)
        entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Medida").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        entry3 = ctk.CTkEntry(vinsertar)
        entry3.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Precio").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry4 = ctk.CTkEntry(vinsertar)
        entry4.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Stock").grid(row=2, column=2, padx=10, pady=10, sticky="e")
        entry5 = ctk.CTkEntry(vinsertar)
        entry5.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="IdCategoria").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        combobox_campos = ctk.CTkComboBox(vinsertar, values=valores)
        combobox_campos.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        combobox_campos.set(valores[0])

        ctk.CTkLabel(vinsertar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")
        button2 = ctk.CTkButton(vinsertar, text="Insertar", fg_color="green", hover_color="#005000",
                                command=lambda: insertProducto(entry1.get(), entry3.get(), entry4.get(), entry5.get(),
                                                               combobox_campos.get()))
        button2.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        button3 = ctk.CTkButton(vinsertar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                                command=vinsertar.destroy)
        button3.grid(row=8, column=3, padx=10, pady=10, sticky="w")
    elif tabla == 2:
        ctk.CTkLabel(vinsertar, text="").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="CIA").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry1 = ctk.CTkEntry(vinsertar)
        entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Contacto").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        entry2 = ctk.CTkEntry(vinsertar)
        entry2.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="Cargo").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry3 = ctk.CTkEntry(vinsertar)
        entry3.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Direccion").grid(row=2, column=2, padx=10, pady=10, sticky="e")
        entry4 = ctk.CTkEntry(vinsertar)
        entry4.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="Ciudad").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        entry5 = ctk.CTkEntry(vinsertar)
        entry5.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Region").grid(row=3, column=2, padx=10, pady=10, sticky="e")
        entry6 = ctk.CTkEntry(vinsertar)
        entry6.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="CP").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        entry7 = ctk.CTkEntry(vinsertar)
        entry7.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Pais").grid(row=4, column=2, padx=10, pady=10, sticky="e")
        entry8 = ctk.CTkEntry(vinsertar)
        entry8.grid(row=4, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="Telefono").grid(row=5, column=0, padx=10, pady=10, sticky="e")
        entry9 = ctk.CTkEntry(vinsertar)
        entry9.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Fax").grid(row=5, column=2, padx=10, pady=10, sticky="e")
        entry10 = ctk.CTkEntry(vinsertar)
        entry10.grid(row=5, column=3, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(vinsertar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")

        button2 = ctk.CTkButton(vinsertar, text="Insertar", fg_color="green", hover_color="#005000",
                                command=lambda: insertCliente(
                                    entry1.get(), entry2.get(), entry3.get(), entry4.get(),
                                    entry5.get(), entry6.get(), entry7.get(), entry8.get(),
                                    entry9.get(), entry10.get()))
        button2.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        button3 = ctk.CTkButton(vinsertar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                                command=vinsertar.destroy)
        button3.grid(row=8, column=3, padx=10, pady=10, sticky="w")

    elif tabla == 3:
        valores = fm.obtenerCampo("cliente", "idcliente")
        valores = [str(valor) for valor in valores]
        print(valores)
        ctk.CTkLabel(vinsertar, text="").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="Fecha pedido").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry1 = ctk.CTkEntry(vinsertar)
        entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Fecha entrega").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        entry3 = ctk.CTkEntry(vinsertar)
        entry3.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="IdCategoria").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        combobox_campos = ctk.CTkComboBox(vinsertar, values=valores)
        combobox_campos.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        combobox_campos.set(valores[0])

        ctk.CTkLabel(vinsertar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")
        button2 = ctk.CTkButton(vinsertar, text="Insertar", fg_color="green", hover_color="#005000",
                                command=lambda: insertPedido(entry1.get(), entry3.get(), combobox_campos.get()))
        button2.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        button3 = ctk.CTkButton(vinsertar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                                command=vinsertar.destroy)
        button3.grid(row=8, column=3, padx=10, pady=10, sticky="w")

    else:
        valores = fm.obtenerCampo("producto", "idproducto")
        valores = [str(valor) for valor in valores]
        print(valores)
        ctk.CTkLabel(vinsertar, text="").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="Precio").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry1 = ctk.CTkEntry(vinsertar)
        entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Unidades").grid(row=1, column=2, padx=10, pady=10, sticky="e")
        entry3 = ctk.CTkEntry(vinsertar)
        entry3.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="Descuento").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        entry4 = ctk.CTkEntry(vinsertar)
        entry4.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(vinsertar, text="IdPedido").grid(row=2, column=2, padx=10, pady=10, sticky="e")
        combobox_campos = ctk.CTkComboBox(vinsertar, values=valores)
        combobox_campos.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        combobox_campos.set(valores[0])

        ctk.CTkLabel(vinsertar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
        ctk.CTkLabel(vinsertar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")
        button2 = ctk.CTkButton(vinsertar, text="Insertar", fg_color="green", hover_color="#005000",
                                command=lambda: insertPedido(entry1.get(), entry3.get(), combobox_campos.get()))
        button2.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        button3 = ctk.CTkButton(vinsertar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                                command=vinsertar.destroy)
        button3.grid(row=8, column=3, padx=10, pady=10, sticky="w")

    vinsertar.mainloop()


def insertCliente(cia, contacto, cargo, direccion, ciudad, region, cp, pais, telefono, fax):
    fg.ventanaEmergente("Funcionalidad no implementada.")


def insertPedido(fecha_pedido, fecha_entrega, idcliente):
    fg.ventanaEmergente("Funcionalidad no implementada.")


def insertCategoria(categoria):
    fg.ventanaEmergente("Funcionalidad no implementada.")


def insertProducto(nombre, medida, precio, stock, idcategoria):
    if not nombre or not medida or not stock or not precio:
        fg.ventanaEmergente("No puede haber ningun campo vacío")
    else:
        if not fg.es_entero(stock):
            fg.ventanaEmergente("Stock tiene que ser un valor entero")
        else:
            if fg.es_decimal(precio) or fg.es_entero(precio):
                ids = fm.obtenerCampo("producto", "idproducto")
                idproducto = ids[-1]
                idproducto = idproducto + 1
                datos = {"idproducto": int(idproducto), "nombre": nombre, "idcategoria": int(idcategoria),
                         "medida": medida, "precio": float(precio), "stock": int(stock)}
                mensaje = fm.insertar_datos("producto", datos)
                fg.ventanaEmergente(mensaje)
            else:
                fg.ventanaEmergente("Precio tiene que ser entero o decimal")


def borrar(tabla):
    vborrar = ctk.CTk()
    ctk.set_appearance_mode("dark")
    fg.center_window(vborrar)
    vborrar.title("Borrar registro")
    if tabla == 0:
        tabla = "categoria"
    elif tabla == 1:
        tabla = "producto"
    elif tabla == 2:
        tabla = "cliente"
    elif tabla == 3:
        tabla = "pedido"
    else:
        tabla = "detalle"

    campos = fm.obtener_campos_de_tabla(tabla)
    ctk.CTkLabel(vborrar, text="").grid(row=0, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vborrar, text="Campo").grid(row=1, column=3, padx=10, pady=10, sticky="e")
    combobox_campos = ctk.CTkComboBox(vborrar, values=campos)
    combobox_campos.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    combobox_campos.set(campos[0])
    ctk.CTkLabel(vborrar, text="Valor").grid(row=2, column=3, padx=10, pady=10, sticky="e")
    entry = ctk.CTkEntry(vborrar)
    entry.grid(row=2, column=4, padx=10, pady=10, sticky="w")

    ctk.CTkLabel(vborrar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vborrar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vborrar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vborrar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")
    button2 = ctk.CTkButton(vborrar, text="Borrar", fg_color="green", hover_color="#005000",
                            command=lambda: borrarProducto(tabla, combobox_campos.get(), entry.get()))
    button2.grid(row=8, column=2, padx=20, pady=10, sticky="e")

    button3 = ctk.CTkButton(vborrar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                            command=vborrar.destroy)
    button3.grid(row=8, column=5, padx=10, pady=10, sticky="w")

    vborrar.mainloop()


def borrarProducto(tabla, campo, valor):
    if tabla == "producto":
        if not valor:
            fg.ventanaEmergente("No puede estar vacío el campo")
        else:
            if campo == "idpedido" or campo == "idcategoria" or campo == "stock":
                mensaje = fm.borrar_datos(tabla, campo, int(valor))
                fg.ventanaEmergente(mensaje)
            else:
                if campo == "precio":
                    mensaje = fm.borrar_datos("producto", campo, float(valor))
                    fg.ventanaEmergente(mensaje)
                else:
                    mensaje = fm.borrar_datos("producto", campo, valor)
                    fg.ventanaEmergente(mensaje)
    else:
        fg.ventanaEmergente("Funcionalidad no implementada.")


def actualizar(tabla):
    vactualizar = ctk.CTk()
    ctk.set_appearance_mode("dark")
    fg.center_window(vactualizar)
    vactualizar.title("Actualizar registro")
    if tabla == 0:
        tabla = "categoria"
    elif tabla == 1:
        tabla = "producto"
    elif tabla == 2:
        tabla = "cliente"
    elif tabla == 3:
        tabla = "pedido"
    else:
        tabla = "detalle"

    campos = fm.obtener_campos_de_tabla(tabla)

    combobox_campos1 = ctk.CTkComboBox(vactualizar, values=campos)
    combobox_campos1.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    combobox_campos1.set(campos[0])
    ctk.CTkLabel(vactualizar, text="Valor").grid(row=2, column=3, padx=10, pady=10, sticky="e")
    entry1 = ctk.CTkEntry(vactualizar)
    entry1.grid(row=2, column=4, padx=10, pady=10, sticky="w")

    campos = campos[1:]
    ctk.CTkLabel(vactualizar, text="").grid(row=0, column=2, padx=10, pady=10, sticky="e")
    combobox_campos2 = ctk.CTkComboBox(vactualizar, values=campos)
    combobox_campos2.grid(row=1, column=6, padx=10, pady=10, sticky="w")
    combobox_campos2.set(campos[0])
    ctk.CTkLabel(vactualizar, text="Valor").grid(row=2, column=5, padx=10, pady=10, sticky="e")
    entry2 = ctk.CTkEntry(vactualizar)
    entry2.grid(row=2, column=6, padx=10, pady=10, sticky="w")

    ctk.CTkLabel(vactualizar, text="").grid(row=4, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vactualizar, text="").grid(row=5, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vactualizar, text="").grid(row=6, column=2, padx=10, pady=10, sticky="e")
    ctk.CTkLabel(vactualizar, text="").grid(row=7, column=2, padx=10, pady=10, sticky="e")

    button2 = ctk.CTkButton(vactualizar, text="Actualizar", fg_color="green", hover_color="#005000",
                            command=lambda: actualizarRegistro(tabla, combobox_campos1.get(), entry1.get(),
                                                               combobox_campos2.get(), entry2.get()))
    button2.grid(row=8, column=4, padx=20, pady=10, sticky="e")

    button3 = ctk.CTkButton(vactualizar, text="Cerrar", fg_color="#d20000", hover_color="#8c0000",
                            command=vactualizar.destroy)
    button3.grid(row=8, column=6, padx=10, pady=10, sticky="w")

    vactualizar.mainloop()

# La para actualizar los valores de la tabla, su campo y sus valores
def actualizarRegistro(tabla, campoW, datoW, campoC, datoC):
    if tabla == "producto":
        if not datoW or not datoC:
            fg.ventanaEmergente("No puede haber un campo vacio")
        else:
            if campoW == "idpedido" or campoW == "idcategoria" or campoW == "stock" or campoW == "idproducto":
                datoW = int(datoW)
            else:
                if campoW == "precio":
                    datoW = float(datoW)
            if campoC == "idpedido" or campoC == "idcategoria" or campoC == "stock":
                datoC = int(datoC)
            else:
                if campoC == "precio":
                    datoC = float(datoC)
            datos = {campoC: datoC}
            mensaje = fm.actualizar_datos(tabla, datos, campoW, datoW)
            fg.ventanaEmergente(mensaje)
    else:
        fg.ventanaEmergente("Funcionalidad no implementada.")

# La funcion principal donde tenemos todas las opciones y las tablas
def tablas():
    vtablas = ctk.CTk()
    ctk.set_appearance_mode("dark")
    fg.center_window_grande(vtablas)
    vtablas.title("Tablas")
    titulo = ctk.CTkLabel(vtablas, text="Seleccione una tabla y una operacion", font=("Georgia, serif", 20))
    titulo.pack(pady=20)

    tablas = fm.obtener_lista_de_tablas()
    radio_var = tk.IntVar(value=0)
    contador = 0
    for tabla in tablas:
        radiobutton = ctk.CTkRadioButton(vtablas, text=tabla, variable=radio_var, value=contador)
        radiobutton.pack(pady=20)
        contador += 1

    button2 = ctk.CTkButton(vtablas, text="Insertar", fg_color="green", hover_color="#005000",
                            command=lambda: insertar(radio_var.get()))
    button2.pack(side=tk.LEFT, pady=35, padx=35)

    button3 = ctk.CTkButton(vtablas, text="Modificar", fg_color="green", hover_color="#005000",
                            command=lambda: actualizar(radio_var.get()))
    button3.pack(side=tk.LEFT, pady=35, padx=35)

    button4 = ctk.CTkButton(vtablas, text="Borrar", fg_color="green", hover_color="#005000",
                            command=lambda: borrar(radio_var.get()))
    button4.pack(side=tk.LEFT, pady=35, padx=35)

    # Botón "Volver" abajo en el medio
    button1 = ctk.CTkButton(vtablas, text="Volver", fg_color="#d20000", hover_color="#8c0000",
                            command=lambda: volver(vtablas))
    button1.pack(side=tk.RIGHT, pady=35, padx=35)

    vtablas.mainloop()
