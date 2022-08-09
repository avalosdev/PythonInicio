#Estrutura de Condição 3
#Faça um programa  para a leitura de 2 notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresetar:
# Mensagem de "Aprovado", se a média alcançada for maior ou igual a sete(7)
# Mensagem de "Recuperação - Examem", se a média alcançada for menor a sete(7) ou maior que cinco(5)
# Mensagem de "Reprovado", se a média alcançada for menor que cinco(5)




nota1 = int(input("Digite a nota da p1: "))

nota2 = int(input("Digite a nota da p2: "))

media = (nota1 + nota2)/2
if media >= 7:
    print("Você foi Aprovado")
    
elif media < 7 and media >= 5 :
    print("Você foi para Exame")
else:
    print("Você foi Reprovado")
