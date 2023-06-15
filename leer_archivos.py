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

# # Lista con los nombres de las columnas a buscar
# columnas_buscar = ["nombre_columna1", "nombre_columna2", "nombre_columna3"]
# # columnas = ['lectura_correctas', 'comprension_correctas', 'oral_correctas', 'comparacion_correctas', 
# #             'numero_faltante_correctas', 'sumas_correctas', 'restas_correctas' ]
# columnas =['programa','año', 'Departamento', 'Municipio', 'Colegio', 'Sede', 'tratamiento/control', 'focalizado', 
#            'Género', 'Grado', 'Grupo', 'Jornada', 'ID']

# archivos_en_carpeta = os.listdir('Base')

# # Abrir archivo de texto para guardar los nombres de las columnas que no se encuentren
# with open("columnas_faltantes3.txt", "w") as archivo_txt:
    
#     archivos_excel = [archivo for archivo in archivos_en_carpeta if archivo.endswith(".xlsx")]
#     # print(archivos_excel)
#     # Ciclo para leer cada archivo excel
#     for nombre_archivo in archivos_excel:
        
#         # Leer archivo excel con pandas
#         df = pd.read_excel(os.path.join('Base', nombre_archivo), sheet_name='3°')
#         print(nombre_archivo) 
#         # Verificar si las columnas buscadas existen en el archivo
#         columnas_existentes = df.columns.tolist()
#         columnas_faltantes = set(columnas) - set(columnas_existentes)
        
#         # Si faltan columnas, guardar sus nombres en el archivo de texto
#         if columnas_faltantes:
#             mensaje = f"Archivo {nombre_archivo}: faltan columnas {columnas_faltantes}\n"
#             archivo_txt.write(mensaje)





# for numero_hoja in range(2,5,1):
#     nombre_hoja = str(numero_hoja) + '°'
#     df1 = pd.read_excel('C:/Users/franc/OneDrive - Universidad Icesi (@icesi.edu.co)/Escritorio/Prueba trabajo/Trabajo_AulaGlobal/Proyecto_AulaGlobal/Base_organizada/BBDD_AG_JARPMJ_2022/BBDD_AG_JARPMJ_Entrada_2022.xlsx', sheet_name=nombre_hoja, usecols=['ID_cruce'])
#     df2 = pd.read_excel('C:/Users/franc/OneDrive - Universidad Icesi (@icesi.edu.co)/Escritorio/Prueba trabajo/Trabajo_AulaGlobal/Proyecto_AulaGlobal/Base_organizada//BBDD_AG_JARPMJ_2022/BBDD_AG_JARPMJ_Salida_2022.xlsx', sheet_name=nombre_hoja, usecols=['ID estudiante'])
#     df2= df2.rename(columns={'ID estudiante':'ID_cruce'})

# valores_comunes = df1['ID_cruce'].isin(df2['ID_cruce'])
# df1['esta_en_comun'] = valores_comunes

# with pd.ExcelWriter('C:/Users/franc/OneDrive - Universidad Icesi (@icesi.edu.co)/Escritorio/Prueba trabajo/Trabajo_AulaGlobal/Proyecto_AulaGlobal/Base_organizada/Comunes.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='2', index=False)
#     df1.to_excel(writer, sheet_name='3', index=False)




# df1.to_excel('C:/Users/Admin/OneDrive - BAMBOO ANALYTICS SAS/Documentos/Prueba_GIT_AG/Proyecto_AulaGlobal/Base_organizada/Comunes.xlsx', index=False)



# Cargar los dataframes de entrada
dfs_entrada = {}
for numero_hoja in range(2, 6):
    nombre_hoja = str(numero_hoja) + '°'
    dfs_entrada[nombre_hoja] = pd.read_excel('C:/Users/Admin/OneDrive - BAMBOO ANALYTICS SAS/Documentos/Prueba_GIT_AG/Proyecto_AulaGlobal/Base_organizada/BBDD_AG_JARPMJ_2022\BBDD_AG_JARPMJ_Entrada_2022.xlsx', sheet_name=nombre_hoja, usecols=['ID_global'])

# Cargar los dataframes de salida y separarlos en hojas
dfs_salida = {}
for numero_hoja in range(2, 6):
    nombre_hoja = str(numero_hoja) + '°'
    df_salida = pd.read_excel('C:/Users/Admin/OneDrive - BAMBOO ANALYTICS SAS/Documentos/Prueba_GIT_AG/Proyecto_AulaGlobal/Base_organizada/BBDD_AG_JARPMJ_2022/BBDD_AG_JARPMJ_Salida_2022.xlsx', sheet_name=nombre_hoja, usecols=['ID_global'])
    # df_salida = df_salida.rename(columns={'CodigoAG': 'CodigoAulaGlobal'})
    dfs_salida[nombre_hoja] = df_salida

# Realizar la validación para cada hoja y guardar los resultados en un diccionario
resultados = {}
for nombre_hoja in dfs_entrada:
    df_entrada = dfs_entrada[nombre_hoja]
    df_salida = dfs_salida[nombre_hoja]
    valores_comunes = df_entrada['ID_global'].isin(df_salida['ID_global'])
    df_entrada['esta_en_comun'] = valores_comunes
    resultados[nombre_hoja] = df_entrada

# Guardar los resultados en un archivo de Excel con hojas separadas
with pd.ExcelWriter('C:/Users/franc/OneDrive - Universidad Icesi (@icesi.edu.co)/Escritorio/Prueba trabajo/Trabajo_AulaGlobal/Proyecto_AulaGlobal/Base_organizada/BBDD_AG_JARPMJ_Salida_2022_Comparativo.xlsx') as writer:
    for nombre_hoja, df_resultado in resultados.items():
        df_resultado.to_excel(writer, sheet_name=nombre_hoja, index=False)