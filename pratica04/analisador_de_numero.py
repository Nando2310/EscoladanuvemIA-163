def analisador_de_numero():
    pares = 0
    impares = 0


    while True:
        entrada = input("Digite um numero inteiro ou 'fim' para encerrar: ")

        if entrada.lower() == "fim":
           break
        
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f" O numero {numero} é par.")
                pares = pares + 1
            else:
                print(f" O numero {numero} é impar.")
                impares = impares + 1
        except ValueError:
            print("Erro encontrado. Por favor digite apenas numeros inteiros.")
            continue        

    print("\nResultado final:")
    print(f"Quantidade de numeros pares é {pares}.")
    print(f"Quantidade de numeros impares é {impares}.")
        
                


analisador_de_numero()