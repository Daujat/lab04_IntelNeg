import pandas as pd
df = pd.read_excel('BI_Alumnos.xlsx')

#Definir intervalos
intervalos = [9, 10, 11, 12, 13, 14, 15, 16]
etiquetas = ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16']

#Nueva columna con los intervalos
df['Intervalo'] = pd.cut(df['Nota'], bins=intervalos, labels=etiquetas, include_lowest=True)

#Calcular distribución de frecuencias
freq = df['Intervalo'].value_counts().sort_index()
rel_freq = freq / len(df)
cum_freq = freq.cumsum()
cum_rel_freq = rel_freq.cumsum()

# Crear la tabla de distribución de frecuencias
tabla_freq = pd.DataFrame({
    'Frecuencia': freq,
    'Frecuencia Relativa': rel_freq,
    'Frecuencia Acumulada': cum_freq,
    'Frecuencia Relativa Acumulada': cum_rel_freq
})

# Formatear las columnas de frecuencias relativas como porcentajes
tabla_freq['Frecuencia Relativa'] = tabla_freq['Frecuencia Relativa'].map('{:.2%}'.format)
tabla_freq['Frecuencia Relativa Acumulada'] = tabla_freq['Frecuencia Relativa Acumulada'].map('{:.2%}'.format)

print(tabla_freq)

#Estadísticas Descriptivas
media = df['Nota'].mean()
mediana = df['Nota'].median()
moda = df['Nota'].mode().values[0]
desv_est = df['Nota'].std()

print(f"\nEstadísticas descriptivas:")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Desviación estándar: {desv_est:.2f}")