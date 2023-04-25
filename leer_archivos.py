# import pandas as pd
# import os

# # Definir las columnas a incluir en el dataframe final
# # columnas = ['programa', 'año', 'colegio', 'sede', 'grado', 'grupo', 'jornada', 'departamento', 'municipio', 'género'  ]
# columnas = ['lectura_correctas', 'comprension_correctas', 'oral_correctas', 'comparacion_correctas', 
#             'numero_faltante_correctas', 'sumas_correctas', 'restas_correctas' ]
# # archivo = 'BBDD_Ortigal_Salida_2021.xlsx'
# # df = pd.read_excel(os.path.join('Base', archivo), usecols=columnas, sheet_name='2°')

# print('lectura')
# # Inicializar una lista para guardar los dataframes de cada archivo
# df_list = []

# # Iterar sobre todos los archivos en la carpeta
# for archivo in os.listdir('Base'):

#     # Si el archivo es un csv
#     if archivo.endswith('.xlsx'):
#         print('nombre archivo analizado',archivo)
#         # Leer el archivo y guardar únicamente las columnas necesarias
#         df = pd.read_excel(os.path.join('Base', archivo), sheet_name='3°')
#         df.columns = df.columns.str.lower()
#         df = df.loc[:, columnas]
#         # Agregar el nombre del archivo como una columna en el dataframe
#         df['archivo'] = archivo

#         # Agregar el dataframe a la lista
#         df_list.append(df)
        
# # Concatenar todos los dataframes en uno solo
# df_final = pd.concat(df_list)

# print('ok')
# # Guardar el dataframe en un archivo csv
# df_final.to_csv('archivo_consolidado.csv', index=False)

import pandas as pd
import os

# Lista con los nombres de las columnas a buscar
columnas_buscar = ["nombre_columna1", "nombre_columna2", "nombre_columna3"]
columnas = ['lectura_correctas', 'comprension_correctas', 'oral_correctas', 'comparacion_correctas', 
            'numero_faltante_correctas', 'sumas_correctas', 'restas_correctas' ]

archivos_en_carpeta = os.listdir('Base')

# Abrir archivo de texto para guardar los nombres de las columnas que no se encuentren
with open("columnas_faltantes.txt", "w") as archivo_txt:
    
    archivos_excel = [archivo for archivo in archivos_en_carpeta if archivo.endswith(".xlsx")]
    # print(archivos_excel)
    # Ciclo para leer cada archivo excel
    for nombre_archivo in archivos_excel:
        
        # Leer archivo excel con pandas
        df = pd.read_excel(os.path.join('Base', nombre_archivo), sheet_name='4°')
        print(nombre_archivo) 
        # Verificar si las columnas buscadas existen en el archivo
        columnas_existentes = df.columns.tolist()
        columnas_faltantes = set(columnas) - set(columnas_existentes)
        
        # Si faltan columnas, guardar sus nombres en el archivo de texto
        if columnas_faltantes:
            mensaje = f"Archivo {nombre_archivo}: faltan columnas {columnas_faltantes}\n"
            archivo_txt.write(mensaje)