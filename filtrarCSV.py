import os
import pandas as pd

# Diretório onde os arquivos CSV foram extraídos
csv_dir = 'ExtrairCSV/csv_extracoes'

# Diretório onde os arquivos CSV filtrados serão salvos
output_dir = 'FiltrarCSV/csv_filtrados'
os.makedirs(output_dir, exist_ok=True)

# Filtra os dados para manter apenas vereadores e prefeitos
def filtrar_dados(caminho_csv):
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv, delimiter=';', encoding='latin1')

        # Converte a coluna DS_CARGO para minúsculas
        df['DS_CARGO'] = df['DS_CARGO'].str.lower()

        # Filtra para vereadores e prefeitos
        df_filtrado = df[df['DS_CARGO'].isin(['vereador', 'prefeito'])]

        # Nome do arquivo de saída
        nome_arquivo_saida = os.path.join(output_dir, f'filtrado_{os.path.basename(caminho_csv)}')
        
        # Salva os dados filtrados em um novo arquivo CSV
        df_filtrado.to_csv(nome_arquivo_saida, index=False, sep=';', encoding='latin1')
        
        print(f'Successfully filtered and saved: {nome_arquivo_saida}')
    except Exception as e:
        print(f'Error processing {caminho_csv}: {e}')

# Loop através dos arquivos CSV no diretório de extração
for file_name in os.listdir(csv_dir):
    if file_name.endswith('.csv'):
        caminho_csv = os.path.join(csv_dir, file_name)
        filtrar_dados(caminho_csv)
