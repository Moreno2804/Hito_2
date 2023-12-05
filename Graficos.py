import tkinter as tk
import matplotlib.pyplot as plt
import customtkinter as ctk
import FuncionesGenerales as fg
import FuncionesMysql as fm

# Una funcion para quitar la ventana
def volver(window):
    window.destroy()

# Una funcion para obtener el gráfico de los precios de los productos
def graficoPrecios():
    precios = fm.obtenerCampo("producto", "precio")

    plt.hist(precios, bins=20)
    plt.title("Grafico repeticion precios-productos")

    # Mostrar el gráfico
    plt.show()
# Una funcion para obtener el gráfico de cantidad de productos por categoría y ver porcentajes
def graficoCategoria():
    categoria = fm.obtenerCampo("producto", "idcategoria")
    idcategoria = fm.obtenerCampo("categoria", "categoria")
    lista = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in categoria:
        posicion = x - 1
        lista[posicion] += 1
    fig, ax = plt.subplots()
    ax.pie(lista, labels=idcategoria, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title("Grafico cantidad productos-categorias")
    plt.show()

# Una funcion para ver las unidades de los pedidos
def graficoUnidades():
    unidades = fm.obtenerCampo("detalle", "unidades")
    fig, ax = plt.subplots()
    ax.violinplot(unidades)
    plt.title("Grafico cantidad de unidades-pedidos")
    plt.show()

# Una funcion para crear la ventana de graficos y sus respectivos botones
def graficos():
    vgraficos = ctk.CTk()
    ctk.set_appearance_mode("dark")
    vgraficos.title("Gráficos")
    fg.center_window(vgraficos)
    buton1 = ctk.CTkButton(vgraficos, text="Ver gráfico 1", fg_color="green", hover_color="#005000", command= graficoUnidades)
    buton1.pack(pady=35)
    buton2 = ctk.CTkButton(vgraficos, text="Ver gráfico 2", fg_color="green", hover_color="#005000",command= graficoPrecios)
    buton2.pack(pady=35)
    buton3 = ctk.CTkButton(vgraficos, text="Ver gráfico 3", fg_color="green", hover_color="#005000", command= graficoCategoria)
    buton3.pack(pady=35)
    buton4 = ctk.CTkButton(vgraficos, text="Volver", fg_color="#d20000", hover_color="#8c0000", command= lambda : volver(vgraficos))
    buton4.pack(pady=35)
    vgraficos.mainloop()
