import datetime
class Config:
    ruta_directorio_input = "C:/Users/Usuario/OneDrive/Escritorio/Workspace/automatizacionNotas/inputs"
    ruta_salida = "C:/Users/Usuario/OneDrive/Escritorio/Workspace/automatizacionNotas/Outputs"


    ''' Vamos a condicionar el archivo procesador. cosa de que cunado el mes en curso sea >= 2 and <= 4 me filtre solamente
    la columna que se llama acreditacion y cuando sea > 4 and <= 1 que me filtre la columna calificacion final'''
    fecha_actual = datetime.datetime.now()
    mes = fecha_actual.month