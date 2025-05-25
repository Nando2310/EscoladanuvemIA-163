"""
Calculadora de Media Escolar
Crie um programa que calcula a média escolar de um aluno.
Use as seguintes notas:
- Nota 1: 7.5
- Nota 2: 8.0
- Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final,
arredondando para duas casas decimais.
"""

# Calculadora de média escolar

# Notas dos alunos
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3


# Exibir para o usuario
print("Notas do estudante")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media,2))