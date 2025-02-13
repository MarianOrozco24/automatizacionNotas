import pandas as pd

def limpiar_df (df):
    # Eliminamos la fila 0 y renombramos las columnas con los valores de la fila 1
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)

    # Obtenemos los valores de laas columnas
    columnas_df = df.columns
    
    # Creamos un df llamado nombres con el valor del df principal en la posicion 0
    df_nombres = df.loc[:, columnas_df[0]]

    # Creamos un df_filtrado con los valores de la calificacion final
    df_filtrado = df.loc[:, "Calificación Final":"Intensificación"]

    df_nombres = df_nombres.to_frame()  # Convierte Series a DataFrame

    # Concatenamos los df
    df_concatenado = pd.concat([df_nombres, df_filtrado], axis=1, ignore_index=False)



    df_concatenado.columns
    df_concatenado.columns = df_concatenado.iloc[0]
    df_concatenado = df_concatenado[1:].reset_index(drop=True)

    return df_concatenado


def analisis_df (df):

    # analsis df
    materias_df = ["Nombre y Apellido", "Cantidad_materias"]
    for i in range(10):
        materias_df.append(f"materias {i}")
    # Creamos un df_vacio
    df_adeudantes_x_año = pd.DataFrame(columns=materias_df)
    contador_adeudantes = 0
    # Recorremos las filas del df
    for index in df.index:

        # Verificamos que las filas que analizamos tengan nombre de estudiante
        if not pd.isna(df.loc[index, "Nombre y Apellido"]):

            # Creamos una cadena vacia para almacenar las variables de cada alumno
            materias_x_alumno = []
            # Recorremos las columnas del df
            for index_columns in range(1, len(df.columns) - 1):

                # condicionamos las notas de cada alumno
                if df.iloc[index, index_columns] < 7:
                    materias_x_alumno.append(df.columns[index_columns])


            if len(materias_x_alumno) > 0:
                df_adeudantes_x_año.loc[contador_adeudantes, "Nombre y Apellido"] = df.loc[index, "Nombre y Apellido"]
                df_adeudantes_x_año.loc[contador_adeudantes, "Cantidad_materias"] = len(materias_x_alumno)
                for c in range(len(materias_x_alumno)):
                    df_adeudantes_x_año.loc[contador_adeudantes, f"materias {c}"] = materias_x_alumno[c]
                contador_adeudantes +=1
        else:
            break
        
    return df_adeudantes_x_año