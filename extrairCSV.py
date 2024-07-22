import os
import zipfile

# Diretório onde os arquivos ZIP foram salvos
input_dir = 'DownloadTSE/arquivos_tse'

# Diretório onde os arquivos CSV serão extraídos
output_dir = 'ExtrairCSV/csv_extracoes'
os.makedirs(output_dir, exist_ok=True)

# Função para extrair arquivos CSV de um arquivo ZIP
def extract_csv_from_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Lista de arquivos no zip
            file_list = zip_ref.namelist()
            for file in file_list:
                if file.endswith('.csv'):
                    zip_ref.extract(file, extract_to)
                    print(f'Successfully extracted: {file}')
    except zipfile.BadZipFile as e:
        print(f'Error with ZIP file {zip_path}: {e}')
    except Exception as e:
        print(f'Other error occurred with {zip_path}: {e}')

# Loop através dos arquivos ZIP no diretório de entrada
for file_name in os.listdir(input_dir):
    if file_name.endswith('.zip'):
        zip_path = os.path.join(input_dir, file_name)
        extract_csv_from_zip(zip_path, output_dir)
