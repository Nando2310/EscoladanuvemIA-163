# Conversor de moedas

# Real para Dólar e Euro
# Valores das moedas

Valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão das taxas
valor_em_dolares = Valor_em_reais / taxa_dolar
valor_em_euros = Valor_em_reais / taxa_euro

# Exibição dos resultados
print(f"Valor em Reais: R$ {Valor_em_reais}")
print("Valor em Dólares $", round(valor_em_dolares,2))
print("Valor em Euros: $", round(valor_em_euros,2))