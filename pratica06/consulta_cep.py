import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "CEP não encontrado"
        return f"""
        CEP: {dados['cep']}
        logradouro:{dados ['logradouro']}
        bairro: {dados ['bairro']}
        cidade: {dados ['localidade']}
        estado: {dados ['uf']}
        """
    except requests.RequestException as e:
        return f"Erro na consulta: {e}"
def main():
    cep = input("Digite um CEP valido para consulta (apenas numeros):")
    print("Consultando seu CEP...")
    resultado = consultar_cep(cep)
    print(resultado)

if __name__ == "__main__":
    main()
