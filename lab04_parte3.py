import pandas as pd
import matplotlib.pyplot as plt
archivo = pd.read_csv('BI_Clientes.csv', delimiter=';', encoding='latin-1')

def generar_histograma(df, columna, titulo, bins=10):
    plt.figure(figsize=(8, 6))
    plt.hist(df[columna], bins=bins, edgecolor='black')
    plt.xlabel(titulo)
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de {titulo}')
    plt.grid(True)
    plt.show()

titulos = {
    'YearlyIncome': 'Ingreso anual',
    'TotalChildren': 'Número total de hijos',
    'NumberCarsOwned': 'Número de vehículos propios'
}

#Histograma para la columna "YearlyIncome"
generar_histograma(archivo, 'YearlyIncome', titulos['YearlyIncome'], bins=20)

#Histograma para la columna "TotalChildren"
generar_histograma(archivo, 'TotalChildren', titulos['TotalChildren'], bins=5)

#Histograma para la columna "NumberCarsOwned"
generar_histograma(archivo, 'NumberCarsOwned', titulos['NumberCarsOwned'], bins=5)