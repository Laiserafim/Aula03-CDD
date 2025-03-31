nome = input("Digite o seu nome: ")
idade = int( input("Digite a sua idade: "))
salario = float( input("Digite o seu salário: "))
print(f"{nome} tem {idade} anos e recebe R$ {salario} reais")
aumento = float(input ("Qual o percentual de aumento salarial? "))
taxa = aumento / 100
valorAumento= (taxa * salario )
novoSalario= valorAumento + salario
print(f"O novo salário será de R$ {novoSalario:.2f} e você teve um aumento de R$ {valorAumento:.2f}")