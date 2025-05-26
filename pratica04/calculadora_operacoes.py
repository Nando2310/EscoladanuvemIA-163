def calculadora():

while True:
    try:    
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        operacao = input("Digite a operação (+, -, * ou /): ")

        if operacao == "+":
            resultado = num1 + num2
        
        elif operacao == "-":
            resultado = num1 - num2
        
        elif operacao == "*":
            resultado = num1 * num2
        
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operação Invalida") # Lançamento das excessões manualmente

        print(f"Resultado: {resultado}")
        break
    except ZeroDivisionError:
        print(f"Erro: Divisão por zero não é possivel. Por favor, tente novamente.")
    except ValueError as e:  
        print(f"Erro {e} : Por favor, tente novamente.")
        