import urllib.request

def download_executavel(url, nome_do_arquivo):
    try:
        urllib.request.urlretrieve(url, nome_do_arquivo)
        print(f"O arquivo {nome_do_arquivo} foi baixado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o arquivo: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do executável: ")
    nome_do_arquivo = input("Digite o nome do arquivo de destino: ")

    download_executavel(url, nome_do_arquivo)