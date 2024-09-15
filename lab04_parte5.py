import pandas as pd
df = pd.read_excel('BI_Clientes.xlsx')

# Calcular la distribución de frecuencias
freq = df['TotalChildren'].value_counts().sort_index()
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

# Mostrar la tabla
print(tabla_freq)

# Calcular estadísticas descriptivas
media = df['TotalChildren'].mean()
mediana = df['TotalChildren'].median()
moda = df['TotalChildren'].mode().values[0]
desv_est = df['TotalChildren'].std()

print(f"\nEstadísticas descriptivas:")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")
print(f"Desviación estándar: {desv_est:.2f}")