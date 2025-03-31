nota01 = float(input("Primeira nota: "))
nota02 = float(input("Segunda nota: "))
nota03 = float(input("Terceira nota: "))
media =  (nota01 + nota02 + nota03)/3

if media >= 7 :
    print("Aluno aprovado!")
else:
    if media <4:
        print("Aluno reprovado!")
    else:
        print("Aluno em recuperação!")