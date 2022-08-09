#Estrutura de Condição 4
#Faça um programa que peça um número inteiro e determine se é par ou impar.
# Dica: utilize o operador módulo(resto da divisão): %




n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print("O n°", n, "é PAR")
    
else:
    print("O n°:", n, "é IMPAR")
