
print ("Calculadura de Média de Notas.")

nome = input("Digite o nome do aluno:")

nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))
nota3 = float(input("Digite a Terceira Nota: "))


media = (nota1 + nota2 + nota3)/3

media = round(media, 2)

print ("A média do aluno", nome, "é igual a:", media)

if media >=7:
    print ("O Aluno", nome, "está aprovado.")
elif media < 7 and media >= 4 :
    print ("O Aluno", nome, "precisa fazer prova final.")
else:
    print ("O Aluno", nome, "está reprovado.")