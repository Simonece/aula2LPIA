# Atividade 01:
# Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para
# verificar se a primeira idade é maior, menor ou igual à segunda.

# Atividade 02:
# Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores
# de comparação para verificar se elas são iguais.

idade1 = int(input("Digite a Primeira idade:"))
idade2 = int(input("Digite a Segunda idade:"))

if idade1 > idade2:
    print("A primeira idade é maior que a segunda!")

elif idade1 < idade2:
    print("A primeira idade é menor que a segunda!")

else:
    print("As idades são iguais!")