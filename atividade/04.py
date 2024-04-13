nome = input("Diga o modelo do seu veículo: ")

distancia = int(input("Digite a distancia: "))
consumo = int(input('Qual o consumo do seu veículo? '))
precoCombustivel = float(input("Qual o preço do combustivel? "))

precoDaViagem = round((distancia / consumo) * precoCombustivel, 2)

print(f"O valor para essa viagem será de R$ {precoDaViagem}")


