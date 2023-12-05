import customtkinter as ctk
import tkinter as tk

#Una funcion para que la ventana se abra centrada y en el tamaño deseado
def center_window(window):
    window.update_idletasks()
    window_width = 600
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


# Una funcion igual que arriba pero distinto tamaño, a mayor
def center_window_grande(window):
    window.update_idletasks()
    window_width = 900
    window_height = 700
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Una funcion igual que arriba pero distinto tamaño, a menor
def center_window_peque(window):
    window.update_idletasks()
    window_width = 400
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Una funcion para saber si el valor es entero o no
def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Una funcion para saber si el valor es decimal o no
def es_decimal(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

#Una funcion para crear ventanas emergentes con el mensaje de texto deseado
def ventanaEmergente(texto):
    app = ctk.CTk()
    ctk.set_appearance_mode("dark")
    center_window_peque(app)
    app.title("Hito 2 Francisco Moreno")
    label = ctk.CTkLabel(app, text=texto, font=("Georgia, serif", 20))
    label.pack(pady=20)
    buton1 = ctk.CTkButton(app, text="Aceptar", fg_color="#d20000", hover_color="#8c0000", command=app.destroy)
    buton1.pack(pady=35)
    app.mainloop()
