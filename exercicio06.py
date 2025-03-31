time01= input("Qual o nome do primeiro time?")
gol01 = int (input(f"Quantidade de gols do {time01}:"))
time02= input("Qual o nome do segundo time?")
gol02 = int (input(f"Quantidade de gols do {time02}:"))

if gol01 > gol02:
    print(f"O time {time01} foi campeão com {gol01} gols")
else:
    if gol01 < gol02:
        print(f"O time {time02} foi campeão com {gol02} gols")
    else:
        print("Jogo empatado!")