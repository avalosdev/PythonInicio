#Estrutura de Condição 5
#Menu de opçoes.
#Escreva uma mensagem de erro se a opções forem inválidas.
#Escolha a opção
# 1 - Soma dois números
# 2 - Diferença entre 2 números(maior pelo menor)
# 3 - Produto entre 2 números

print("*********************")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números(maior pelo menor)")
print("3 - Produto entre 2 números")
print("")
print("Escolha uma das opções digitando somente o número:")
n= int(input(""))
n1 = int(input("Digite um número(inteiro): "))
n2 = int(input("Digite outro número(inteiro): "))


if (n == 1):
    print("A Soma entre Números:", n1, "e", n2, "é igual:", n1 + n2 )
    
elif (n == 2):
    if (n1 > n2):
      print("Diferença entre:", n1, "e", n2, "é igual:", n1 - n2 )
    elif (n2 > n1):
      print("Diferença entre:", n2, "e", n1, "é igual:", n2 - n1 )
    else:
      print("Os números inseridos: São iguais")
          

elif (n == 3):
    print("Produto entre :", n1, "e", n2, "é igual:", n1*n2 )

else:
    print("Número da Opção INVÁLIDA!")
   
