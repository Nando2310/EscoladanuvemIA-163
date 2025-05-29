import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados [f"{moeda}BRL"]
        return f"""
        moeda: {moeda} para BRL
        valor: R$ {float(cotacao['bid']):.2f}
        Maxima: R$ {float(cotacao['high']):.2f}
        Minima: R$ {float(cotacao['low']):.2f}
        Data e hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}

        """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    except KeyError:
        return f"Moeda não suportada ou não encontrada."
def main():
    moeda = input("Digite o codigo da moeda para cotação (ex: USD, EUR, GBP):").upper()
    print("\nObtendo sua cotação...")
    resultado = obter_cotacao(moeda)
    print(resultado)

if __name__ == "__main__":
    main()
