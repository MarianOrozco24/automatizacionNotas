import xlwings as xw
import os
from config import Config

def progress(nombre_xls):
    # Ruta del archivo .xls
    
    nombre_xlsx = nombre_xls.replace(".xls", ".xlsx")

    if os.path.exists(f"{Config.ruta_directorio_input}/{nombre_xls}"):
        print("Se encontro el archivo")
        app = xw.App(visible=False)  # Iniciar Excel visible para depuración
        app.display_alerts = False  # Evitar alertas
        app.screen_updating = False  # Mejorar rendimiento

        # Cerrar el libro en blanco si se abre por defecto
        if len(app.books) > 0:
            for book in app.books:
                if book.name == "Libro1":  # O "Book1" en inglés
                    book.close()
        try:
            # Ahora sí abrir el archivo correcto
            wb = xw.Book(f"{Config.ruta_directorio_input}/{nombre_xls}") 
            print("✅ Archivo abierto correctamente:", nombre_xls)

            # Guardar como .xlsx
            wb.save(f"{Config.ruta_directorio_input}/{nombre_xlsx}")
            wb.close()
            app.quit()

            print("✅ Conversión completada:", nombre_xlsx)
            os.remove(f"{Config.ruta_directorio_input}/{nombre_xls}")
            if os.remove:
                print("✅ El archivo fue eliminado con exito")
            else: 
                print("❌ ERROR: El archivo no fue eliminado")
        except Exception as e:
            print(e)
    else:
            print("❌ ERROR: Archivo no encontrado")
        
    return nombre_xlsx

def buscar_archivos(ruta):
    
    archivos = os.listdir(ruta)
    return archivos

