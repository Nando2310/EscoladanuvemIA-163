def verificar_senha():
    while True:
        senha = input("Digite a senha (ou digite 'sair' para encerrar o progama): ")
        # verificar se o usuario quer encerrar o progama
        if senha == "sair":
            print("Progama encxerrado.")
            break 

        if len(senha) <8:
            print("Senha fraca. a senha precisa ter pelo menos 8 caracteres.")
            continue

        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um numero.")  
            continue

        
        if not any(caractere.isalpha() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um letra.")  
            continue

         if not any(caractere.isupper() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um letra maiuscula.")  
            continue


        print("senha forte e valida")     
        break






verificar_senha()