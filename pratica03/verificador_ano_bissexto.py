"""
aça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

ano = int(input("Digite um número: "))

if ano % 4 == 0: # O ano pode ser bissexto
    if ano % 100 == 0: # Se o ano for divisivil por 100, precisa ser analisado.
        if ano % 400 == 0: # Se o ano for tambem divisivel por 400, entao ele é bissexto
              print(f"O ano {ano}  é bisssexto. ")
        else:
              print(f"O ano {ano} não é bisssexto. ")
    else:
         print(f"O ano {ano} não é bisssexto.")          
                    
else:
    print(f"O ano {ano} não é bisssexto. ")
