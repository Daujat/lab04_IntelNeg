import pandas as pd
import matplotlib.pyplot as plt
archivo = pd.read_csv('WEO_Data.csv', thousands=',', decimal='.')

def grafico_lineal_pais(df, pais, anio_inicio, anio_fin):
    columnas = [str(anio) for anio in range(anio_inicio, anio_fin + 1)]
    datos_pais = df[df['Country'] == pais][columnas].values[0]
    anios = range(anio_inicio, anio_fin + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(anios, datos_pais)
    plt.title(f'PBI de {pais} ({anio_inicio}-{anio_fin})')
    plt.xlabel('Año')
    plt.ylabel('PBI (miles de millones de dólares)')
    plt.xticks(anios, rotation=45)
    plt.grid(True)
    plt.show()

def grafico_lineal_paises(df, paises, anio_inicio, anio_fin):
    columnas = [str(anio) for anio in range(anio_inicio, anio_fin + 1)]
    anios = range(anio_inicio, anio_fin + 1)

    plt.figure(figsize=(10, 6))
    for pais in paises:
        datos_pais = df[df['Country'] == pais][columnas].values[0]
        plt.plot(anios, datos_pais, label=pais)

    plt.title(f'PBI de otros países ({anio_inicio}-{anio_fin})')
    plt.xlabel('Año')
    plt.ylabel('PBI (miles de millones de dólares)')
    plt.xticks(anios, rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

#Ejemplitos
grafico_lineal_pais(archivo, 'Peru', 2000, 2020)
grafico_lineal_paises(archivo, ['Canada', 'Costa Rica'], 2000, 2020)