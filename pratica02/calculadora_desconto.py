# calculadora de desconto

#Informações do produto

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calculo do desconto e do preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto


#Exibição dos resultados
print("Produto", nome_produto)
print(f"Preço original: R$ {preco_original: .2f}")
print("Desconto:", porcentagem_desconto, "%")
print(f"Valor do desconto: R$ {valor_desconto: .2f}")
print(f"preço final: R$ {preco_final: .2f}")
