#Peça para o usuário digitar sua idade, e exiba as seguientes mensagens:
#Se idade >= 0 e <= 11, "Criança"
#Se idade >= 12 e <= 17, "Adolecente"
#Se idade >= 18 e <= 100, "Adulto"




i = int(input("Digite sua idade: "))

if (i  >= 0 or i <= 11):
    print("você tem idade de:", "Criança" )
    
elif (i  >= 12 and i <= 17):
    print("você tem idade de:", "Adolecente" )

elif (i  >= 18 and i <= 100):
    print("você tem idade de:", "Adulto" )
else:
    print("Número é inválido")
