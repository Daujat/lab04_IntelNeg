import matplotlib.pyplot as plt

def grafico_lineal(x, y, titulo, etiqueta_x, etiqueta_y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o')
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.grid(True)
    plt.show()

def grafico_lineal_multiple(x, y1, y2, titulo, etiqueta_x, etiqueta_y, leyenda1, leyenda2):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, marker='o', label=leyenda1)
    plt.plot(x, y2, marker='s', label=leyenda2)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.legend()
    plt.grid(True)
    plt.show()

#Ejemplito
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
grafico_lineal(x, y, 'Gráfico Lineal', 'Eje X', 'Eje Y')

#Ejemplito 2
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
grafico_lineal_multiple(x, y1, y2, 'Gráfico Lineal Múltiple', 'Eje X', 'Eje Y', 'Serie 1', 'Serie 2')