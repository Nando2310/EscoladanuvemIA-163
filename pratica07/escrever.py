import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['nome', 'idade', 'cidade'])  # Cabeçalho
        escritor.writerows(dados)  # Várias linhas
    print(f"Dados salvos em {nome_arquivo}")

dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bruno', 25, 'São Paulo'],
    ['Carlos', 33, 'Belo Horizonte']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    escrever_csv(nome_arquivo, dados)

