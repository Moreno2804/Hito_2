import ConexionBD as cb
import FuncionesMysql as fm
import customtkinter as ctk
import Consulta as cs
import Tablas as ts
import Graficos as gs
import FuncionesGenerales as fg


# Esta es la funcion para crear o conectarme a la base de datos
cb.conectar()

#En el caso de que no esté creada la base de datos, aqui creamos e insertamos los datos
#fm.insertTablas()
#fm.insertarDatos()

#Creamos la ventana con sus botones
app = ctk.CTk()
ctk.set_appearance_mode("dark")
fg.center_window(app)
app.title("Hito 2 Francisco Moreno")
label = ctk.CTkLabel(app, text='Gestion del Supermercado', font=("Georgia, serif", 20))
label.pack(pady=20)
buton1 = ctk.CTkButton(app, text="Consultar datos", fg_color="green", hover_color="#005000", command=cs.consulta)
buton1.pack(pady=35)
buton3 = ctk.CTkButton(app, text="Modificar tablas", command=ts.tablas)
buton3.pack(pady=35)
buton4 = ctk.CTkButton(app, text="Mostrar graficos", command=gs.graficos)
buton4.pack(pady=35)

app.mainloop()
