notas_lista = []
while True:
    try:
        entrada = input("Digite a nota do aluno ou digite 'fim' para encerrar: ")
        if entrada == "fim":
            break # Interrompe o blobo de loop e segue o progama

        nota = float(entrada)
        if 0 <= nota <=10:
            notas_lista.append(nota)

        else:
            print("Nota invalida. Digite um valor entre 0 e 10. ")
            continue
    except ValueError:
        print("Entrada invalida. Por favor digite um numero ou 'fim'. ")    
if notas_lista: 
    media = sum(notas_lista) / len(notas_lista)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas validas é: {len(notas_lista)}")
else:
    print("Nenhuma nota valida foi registrada.")    