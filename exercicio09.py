#entrada1: 3:45
#entrada2: 14:20
#saida: 6:05

hora1 = int(input("Digite a primeira hora"))
minuto1 = int (input("Digite o primeiro minuto"))
hora2 = int(input("Digite a psegunda hora"))
minuto2 = int (input("Digite o segundo minuto"))


horafinal = (hora1 + hora2)
minutofinal = minuto1 + minuto2

if minutofinal > 60:
    horafinal +=1
    minutofinal -= 60


if horafinal >= 24:
    horafinal-=24
else:
    horafinal-=12

print(f"{horafinal}:{minutofinal}h")
