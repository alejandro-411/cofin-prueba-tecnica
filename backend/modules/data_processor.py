import pandas as pd

# Load data
df_personal = pd.read_excel('backend/data/data1.xlsx')
df_financial = pd.read_excel('backend/data/data2.xlsx')

# Merge data
df_merged = pd.merge(df_personal, df_financial, on='nit')

df_merged['nombre completo'] = df_merged['nombre'] + ' ' + df_merged['apellido']
df_merged['total'] = df_merged['ingresos'] - df_merged['egresos']
df_merged = df_merged[['nit', 'nombre completo', 'ingresos', 'egresos', 'total']]

stats = {
    'suma de Ingresos': df_merged['ingresos'].sum(),
    'suma de Egresos': df_merged['egresos'].sum(),
    'promedio de Ingresos': df_merged['ingresos'].mean(),
    'promedio de Egresos': df_merged['egresos'].mean(),
    'ingreso Máximo': df_merged['ingresos'].max(),
    'ingreso Mínimo': df_merged['ingresos'].min(),
    'egreso Máximo': df_merged['egresos'].max(),
    'egreso Mínimo': df_merged['egresos'].min()
}

# Save data

df_stats = pd.DataFrame(list(stats.items()), columns=['descripción', 'valor'])
df_merged.to_csv('backend/results/data_merged.csv', index=False)
df_stats.to_csv('backend/results/data_stats.csv', index=False)

print("\nEstadísticas:")
print(df_stats)