import os
import requests
import threading

# Diretório onde os arquivos serão salvos
output_dir = 'arquivos_tse'
os.makedirs(output_dir, exist_ok=True)

# Anos a serem baixados
anos = [2020]

# Estados do Brasil
estados = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

# URL base
url_base = 'https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_secao/'

# Função para baixar o arquivo
def download_file(url, dest_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(dest_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Successfully downloaded: {dest_path}')
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err} - URL: {url}')
    except Exception as err:
        print(f'Other error occurred: {err} - URL: {url}')

# Função para gerenciar o download com threads
def thread_manager(urls):
    threads = []
    for url, dest_path in urls:
        thread = threading.Thread(target=download_file, args=(url, dest_path))
        threads.append(thread)
        thread.start()
        if len(threads) >= 10:
            for thread in threads:
                thread.join()
            threads = []
    for thread in threads:
        thread.join()

# Cria a lista de URLs e caminhos de destino
urls = []
for ano in anos:
    for estado in estados:
        file_name = f'votacao_secao_{ano}_{estado}.zip'
        url = f'{url_base}{file_name}'
        dest_path = os.path.join(output_dir, file_name)
        urls.append((url, dest_path))

# Inicia o download com threads
thread_manager(urls)
