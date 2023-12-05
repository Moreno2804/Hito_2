import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import FuncionesMysql as fm
import FuncionesGenerales as fg
import pandas as pd


# Aqui tenemos todas las funcionalidades del apartado de consulta, como la creacion de su ventana y el resto de funciones
# Una funcion para destruir la ventana
def volver(window):
    window.destroy()


# Una funcion para destruir la ventana y volver a llamar a la funcion consulta
def volver1(window):
    window.destroy()
    consulta()

# Una funcion para cuando pulsamos en una columna que se ordene
def ordenar_columna(tree, col, reverse):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse)
    for i, item in enumerate(data):
        tree.move(item[1], '', i)
    tree.heading(col, command=lambda: ordenar_columna(tree, col, not reverse))


# Una funcion para buscar el valor deseado del campo deseado
def buscar(entry, combobox_campos, treeview, datos, campos):
    criterio = entry.get()
    campo_seleccionado = combobox_campos.get()

    # Limpiar el Treeview antes de aplicar la busqueda
    for item in treeview.get_children():
        treeview.delete(item)

    # Aplicar la busqueda
    for fila in datos:
        if criterio.lower() in str(fila[campos.index(campo_seleccionado)]).lower():
            treeview.insert("", "end", values=fila)


#Una funcion para realizar un filtro, con un criterio de mayor menor o igual
def aplicar_filtro(campo_seleccionado, operacion_seleccionada, criterio, treeview, datos, campos):
    # Limpiar el Treeview antes de aplicar el filtro
    for item in treeview.get_children():
        treeview.delete(item)

    # Aplicar el filtro
    for fila in datos:
        valor_campo = fila[campos.index(campo_seleccionado)]

        if operacion_seleccionada == "Igual" and criterio.lower() == str(valor_campo).lower():
            treeview.insert("", "end", values=fila)
        elif operacion_seleccionada == "Mayor" and valor_campo > float(criterio):
            treeview.insert("", "end", values=fila)
        elif operacion_seleccionada == "Menor" and valor_campo < float(criterio):
            treeview.insert("", "end", values=fila)
        elif operacion_seleccionada == "Mayor-Igual" and valor_campo >= float(criterio):
            treeview.insert("", "end", values=fila)
        elif operacion_seleccionada == "Menor-Igual" and valor_campo <= float(criterio):
            treeview.insert("", "end", values=fila)

#La funcion de pasar los datos del treeview a dataframe y exportarlos
def exportar(treeview):
    columnas = treeview["columns"]

    # Crear un DataFrame de pandas con las columnas del Treeview
    df = pd.DataFrame(columns=columnas)

    # Obtener los datos del Treeview y añadirlos al DataFrame
    for item in treeview.get_children():
        valores = [treeview.item(item, "values")]
        df = pd.concat([df, pd.DataFrame(valores, columns=columnas)], ignore_index=True)

    ruta_resultado = r'./recursos/resultadoSQL.xlsx'

    # Exportar el DataFrame a un archivo Excel
    df.to_excel(ruta_resultado, index=False)

# La funcion consultar sobre la tabla deseada, la creacion del treeview, los entry y los botones.
def consultar(window, radio, tablas):
    window.destroy()
    vview = ctk.CTk()
    vview.attributes('-fullscreen', True)
    vview.title("Consultas")

    tabla = radio.get()
    tabla = tablas[tabla]
    datos = fm.leerTabla(tabla)
    campos = fm.obtener_campos_de_tabla(tabla)

    frame_contenedor = ctk.CTkFrame(vview)
    frame_contenedor.pack(side=tk.TOP, pady=20)

    buttonFiltro = ctk.CTkButton(frame_contenedor, text="Buscar",
                                 command=lambda: buscar(entry_filtro, combobox_campos, treeview, datos,
                                                        campos))
    buttonFiltro.pack(side=tk.LEFT, padx=10, anchor=tk.N)
    entry_filtro = ctk.CTkEntry(frame_contenedor)
    entry_filtro.pack(side=tk.LEFT, padx=10, anchor=tk.N)

    # Aqui guardo los datos que hacen referencia a los campos de la tabla
    combobox_campos = ctk.CTkComboBox(frame_contenedor, values=campos)
    combobox_campos.pack(side=tk.LEFT, padx=10, anchor=tk.N)
    combobox_campos.set(campos[0])

    campos1 = ["Mayor", "Menor", "Mayor-Igual", "Menor-Igual", "Igual"]
    combobox_campos1 = ctk.CTkComboBox(frame_contenedor, values=campos1)
    combobox_campos1.pack(side=tk.LEFT, padx=10, anchor=tk.N)
    combobox_campos1.set(campos1[0])
    entry_filtro1 = ctk.CTkEntry(frame_contenedor)
    entry_filtro1.pack(side=tk.LEFT, padx=10, anchor=tk.N)
    buttonFiltro1 = ctk.CTkButton(frame_contenedor, text="Filtrar",
                                  command=lambda: aplicar_filtro(combobox_campos.get(), combobox_campos1.get(),
                                                                 entry_filtro1.get(), treeview, datos, campos))
    buttonFiltro1.pack(side=tk.LEFT, padx=10, anchor=tk.N)

    buttonExport = ctk.CTkButton(frame_contenedor, text="Exportar", fg_color="green", hover_color="#005000",
                                 command=lambda: exportar(treeview))
    buttonExport.pack(side=tk.LEFT, padx=10, anchor=tk.N)

    treeview = ttk.Treeview(vview, columns=campos, show="headings")

    # Establecemos encabezados del treeview
    for columna in campos:
        treeview.heading(columna, text=columna, command=lambda col=columna: ordenar_columna(treeview, col, False))

    # Llenanamos el treeview con los datos
    for fila in datos:
        treeview.insert("", "end", values=fila)

    # Creamos dos barras de desplazamiento
    scroll_y = ttk.Scrollbar(vview, orient="vertical", command=treeview.yview)
    scroll_y.pack(side="right", fill="y")
    treeview.configure(yscrollcommand=scroll_y.set)

    scroll_x = ttk.Scrollbar(vview, orient="horizontal", command=treeview.xview)
    scroll_x.pack(side="bottom", fill="x")
    treeview.configure(xscrollcommand=scroll_x.set)

    # Empaquetar el Treeview
    treeview.pack(fill="both", expand=True, pady=10, padx=20)

    button1 = ctk.CTkButton(vview, text="Volver", fg_color="green", hover_color="#005000",
                            command=lambda: volver1(vview))
    button1.pack(side="bottom", anchor="s", pady=35, padx=35)
    vview.mainloop()

# Funcion consulta, que es la ventana principal de este apartado, donde podremos elegir la tabla a consultar
def consulta():
    vconsulta = ctk.CTk()
    ctk.set_appearance_mode("dark")
    fg.center_window(vconsulta)
    vconsulta.title("Consultas")

    titulo = ctk.CTkLabel(vconsulta, text="Seleccione una tabla", font=("Georgia, serif", 20))
    titulo.pack()

    tablas = fm.obtener_lista_de_tablas()

    radio_var = tk.IntVar(value=0)
    contador = 0
    for tabla in tablas:
        radiobutton = ctk.CTkRadioButton(vconsulta, text=tabla, variable=radio_var, value=contador)
        radiobutton.pack(pady=20)
        contador += 1

    button1 = ctk.CTkButton(vconsulta, text="Volver", fg_color="#d20000", hover_color="#8c0000",
                            command=lambda: volver(vconsulta))
    button1.pack(side="left", anchor="se", pady=35, padx=35)
    button2 = ctk.CTkButton(vconsulta, text="Consultar", fg_color="green", hover_color="#005000",
                            command=lambda: consultar(vconsulta, radio_var, tablas))
    button2.pack(side="right", anchor="sw", pady=40, padx=50)
    vconsulta.mainloop()
