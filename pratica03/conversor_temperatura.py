"""
Conversor de Temperatura
Crie um programa que converta temperaturas entre
Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura,
a unidade de origem e
a unidade para qual deseja converter. "

"""

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a temperatura de origem (c, f ou k): ").upper()
destino = input("Digite a temperatura de destino (c, f ou k): ").upper()


if origem == destino:
    resultado = temperatura
elif origem == "c":
    if destino == "f":
        resultado = (temperatura * 9/5) + 32
    else:
          resultado = temperatura + 273.15
elif origem == "f":
    if destino == "c":
        resultado = (temperatura - 32) * 5/9
    else:
        resultado = (temperatura - 32) * 5/9 + 273.15
else:
    if destino == "c":
        resultado = temperatura - 273.15
    else:
        resultado = (temperatura - 273.150) *9/5 +32





    print(f"A temperatura {temperatura} {origem} é igual a {resultado} {destino}")