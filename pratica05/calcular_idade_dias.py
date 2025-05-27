import datetime

def calcular_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias
     
ano_nascimento = int(input("Digite o ano do nascimento: "))

idade_em_dias = calcular_idade_dias(ano_nascimento)
print(f"Sua idade aproximada é : {idade_em_dias} dia. ")
    