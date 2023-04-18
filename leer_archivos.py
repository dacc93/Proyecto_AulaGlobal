import pandas as pd
import os

# Definir las columnas a incluir en el dataframe final
columnas = ['programa', 'año', 'Colegio', 'Sede', 'Grado', 'Grupo' ]
archivo = 'BBDD_Ortigal_Salida_2021.xlsx'
df = pd.read_excel(os.path.join('Base', archivo), usecols=columnas, sheet_name='2°')
print(df)
print('lectura')
# Inicializar una lista para guardar los dataframes de cada archivo
df_list = []

# Iterar sobre todos los archivos en la carpeta
for archivo in os.listdir('Base'):

    # Si el archivo es un csv
    if archivo.endswith('.xlsx'):
        print('nombre archivo analizado',archivo)
        # Leer el archivo y guardar únicamente las columnas necesarias
        df = pd.read_excel(os.path.join('Base', archivo), usecols=columnas, sheet_name='2°')

        # Agregar el nombre del archivo como una columna en el dataframe
        df['archivo'] = archivo

        # Agregar el dataframe a la lista
        df_list.append(df)
        
# Concatenar todos los dataframes en uno solo
df_final = pd.concat(df_list)

print('ok')
# Guardar el dataframe en un archivo csv
df_final.to_csv('archivo_consolidado.csv', index=False)