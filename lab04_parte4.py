import pandas as pd
import matplotlib.pyplot as plt
archivo = pd.read_csv('problemas_del_corazon.csv', delimiter=',')

def grafico_barra_genero(df):
    genero_conteo = df['genero'].value_counts()
    etiquetas = ['Masculino', 'Femenino']
    valores = [genero_conteo[1], genero_conteo[0]]

    plt.figure(figsize=(8, 6))
    plt.bar(etiquetas, valores)
    plt.xlabel('Género')
    plt.ylabel('Cantidad')
    plt.title('Distribución por Género')
    plt.grid(True)
    plt.show()

def grafico_barra_diabetico(df):
    diabetico_conteo = df['diabetico'].value_counts()
    etiquetas = ['No Diabético', 'Diabético']
    valores = [diabetico_conteo[0], diabetico_conteo[1]]

    plt.figure(figsize=(8, 6))
    plt.bar(etiquetas, valores)
    plt.xlabel('Diabético')
    plt.ylabel('Cantidad')
    plt.title('Distribución por Diabético')
    plt.grid(True)
    plt.show()

def grafico_barra_cardiaco(df):
    cardiaco_conteo = df['cardiaco'].value_counts()
    etiquetas = ['No Cardíaco', 'Cardíaco']
    valores = [cardiaco_conteo[0], cardiaco_conteo[1]]

    plt.figure(figsize=(8, 6))
    plt.bar(etiquetas, valores)
    plt.xlabel('Cardíaco')
    plt.ylabel('Cantidad')
    plt.title('Distribución por Problemas Cardíacos')
    plt.grid(True)
    plt.show()

#Gráfiquitos
grafico_barra_genero(archivo)
grafico_barra_diabetico(archivo)
grafico_barra_cardiaco(archivo)