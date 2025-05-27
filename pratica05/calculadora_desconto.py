"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto.
Requisitos:

- Permitir que o usuário informe o preço do produto e o percentual de desconto.
- Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
- Exibir o preço final com duas casas decimais para garantir precisão.
Entrada esperada:
- Um número decimal representando o preço do produto (exemplo: 250.75).
"""

def calculadora_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final




#input do usuario
preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

# Calculo do desconto
preco_com_desconto = calculadora_desconto(preco_original, desconto)

print(f"O preço final com {desconto}% de desconto é: {preco_com_desconto:.2f}.")
