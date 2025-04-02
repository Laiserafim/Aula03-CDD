litro = float (input("Quantos litros de combustível?" ))
tipo = input("Qual o tipo de combustivel? Use 'e' para Etanol e 'g' para gasolina. ")

if tipo == "g" or tipo == "G":
    gasolina = litro * 5.80
    print(f"Você abasteceu com gasolina e pagou R$ {gasolina:.2f} por {litro} litros")
else:
    if tipo == "e" or tipo == "E":
        etanol = litro * 4.90
        print(f"Você abasteceu com etanol e pagou R$ {etanol:.2f} por {litro} litros")
    else:
        print("Tipo de combustível inválido! ")