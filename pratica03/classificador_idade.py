"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:
*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade invalida!")
elif idade <= 12:
    print("Voçe é uma criança")
elif idade <= 17:
    print("Voçe é uma adolescente")    
elif idade <= 59:
    print("Voçe é uma adulto")
else: 
    print("Voçe é idoso. ")        



        