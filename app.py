import customtkinter as ctk
import pandas as pd
from tkinter import messagebox as mx
from procesamiento_notas.procesador import limpiar_df, analisis_df


def main(df, nombre_excel):
    df = pd.read_excel(ruta)
    nombre_excel = nombre_excel

    df_limpio = limpiar_df(df)
    resultado = analisis_df(df_limpio)

    resultado.to_excel(f"{nombre_excel}.xlsx",engine="openpyxl", index=False)
    if resultado.to_excel:
        mx.showinfo("Exportacion completa", f"El archivo {nombre_excel}, se exporto correctamente al escritorio")

# interfaz grafica
ventana_principal = ctk.CTk()
ventana_principal.title("Analisis Notas")
ventana_principal.geometry("850x450")

# label_title
label_title = ctk.CTkLabel(ventana_principal, text="Analisis Notas", font=("Helvetica", 20, "bold"))
label_title.pack(pady=35, padx=5)

from tkinter import filedialog

# Función para abrir el explorador de archivos
def buscar_archivo():
    global ruta
    ruta = filedialog.askopenfilename(title="Seleccionar archivo")
    if ruta:  # Si el usuario selecciona un archivo
        label_seleccion.configure(text=f"Se ha seleccionado el archivo: {ruta}")


# Boton buscar excel
frame_explorardor = ctk.CTkFrame(ventana_principal, fg_color="#00ADB5")
frame_explorardor.pack(pady=5, padx=5)
explorador = ctk.CTkButton(frame_explorardor, text="Seleccionar excel con notas", fg_color="#2E2E2E", command=buscar_archivo)
explorador.pack(pady=2, padx=2)
label_seleccion = ctk.CTkLabel(ventana_principal, text="Archivo seleccionado: Ninguno", font=("Helvetica", 12))
label_seleccion.pack(pady=5, padx=5)

## Nombre del excel
entrada_name = ctk.CTkEntry(ventana_principal, placeholder_text="Nombre excel")
entrada_name.pack(pady=25, padx=5)

# Botton continuar 
frame_continuar = ctk.CTkFrame(ventana_principal, fg_color="#00ADB5")
frame_continuar.pack(pady=5, padx=5, side ="bottom")
button_continue = ctk.CTkButton(frame_continuar, text="Procesar", fg_color="#2E2E2E", command=lambda:main(ruta, entrada_name.get()))
button_continue.pack(pady=2, padx=2)

ventana_principal.mainloop()


