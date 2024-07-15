import pandas as pd
import os

# get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
backend_dir = os.path.dirname(current_dir)

def process_data():
    """
    Process the data by loading, merging, transforming, and saving it.

    Returns:
        tuple: A tuple containing two elements:
            - A list of dictionaries representing the processed data.
            - A dictionary containing various statistics calculated from the data.
    """
    # Load data
    df_personal = pd.read_excel(os.path.join(backend_dir, 'data', 'data1.xlsx'))
    df_financial = pd.read_excel(os.path.join(backend_dir, 'data', 'data2.xlsx'))

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
    df_stats = pd.DataFrame(list(stats.items()), columns=['descripcion', 'valor'])
    df_merged.to_csv(os.path.join(backend_dir, 'results', 'data_merged.csv'), index=False)
    df_stats.to_csv(os.path.join(backend_dir, 'results', 'data_stats.csv'), index=False)

    return df_merged.to_dict('records'), stats


def get_data():
    return pd.read_csv('backend/results/data_merged.csv').to_dict('records')

def get_stats():
    return pd.read_csv('backend/results/data_stats.csv').set_index('descripcion')['valor'].to_dict()

