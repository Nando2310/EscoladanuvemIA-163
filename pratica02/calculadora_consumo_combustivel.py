# Cálculadora de consumo de combustivel

# Dados da viagem
distancia_percorrida = 300 #km
combustivel_gasto = 25 #litros

# Calculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição dos dados
print("Dados da viagem")
print(f"Distancia percorrida: {distancia_percorrida} km")
print("Combustivel gasto:", combustivel_gasto, "litros")
print(f"Consumo médio: {consumo: .2f} km/l")