import customtkinter as ctk
import pandas as pd
from tkinter import messagebox as mx
from procesamiento_notas.procesador import limpiar_df, analisis_df
from scrapeo import scrapeo
from xls_a_xlsx.transformation import progress
from xls_a_xlsx.transformation import buscar_archivos
from config import Config
def main():
    # Descarga de informacion
    scrapeo()
    try:
        archivos_descargados = buscar_archivos(Config.ruta_directorio_input)
        for archivo in archivos_descargados:
            print(archivo)
            # Luego de terminado el proceso de tranformacion de xls a xlsx extraemos el nombre resultado
            nombre_excel = progress(archivo)

            # Lo convertimos en df
            df = pd.read_excel(f"{Config.ruta_directorio_input}/{nombre_excel}")

            # Lo limpiamos
            df_limpio = limpiar_df(df)
            resultado = analisis_df(df_limpio)

            resultado.to_excel(f"{Config.ruta_salida}/{nombre_excel}.xlsx",engine="openpyxl", index=False)
        
        mx.showinfo("Filtrado completo", "Se han exportado todos los archivos a la carpeta outputs")
            
    except Exception as e:
        print(e)

# interfaz grafica
ventana_principal = ctk.CTk()
ventana_principal.title("Analisis Notas")
ventana_principal.geometry("850x450")

# label_title
label_title = ctk.CTkLabel(ventana_principal, text="Analisis Notas", font=("Helvetica", 20, "bold"))
label_title.pack(pady=35, padx=5)


# Botton continuar 
frame_continuar = ctk.CTkFrame(ventana_principal, fg_color="#00ADB5")
frame_continuar.pack(pady=5, padx=5)
button_continue = ctk.CTkButton(frame_continuar, text="Procesar", fg_color="#2E2E2E", command=lambda:main())
button_continue.pack(pady=2, padx=2)

ventana_principal.mainloop()






