nome = input("Digite seu nome: ")
idade = int(input('Digite sua idade: '))

if idade <= 10:
    print(f'{nome}, você é uma criança!')
elif idade > 10 and idade < 18:
    print(f'{nome}, você é um adolescente!')
elif idade >= 18 and idade < 60:
        print(f'{nome}, você é um adulto!') 
else:
        print(f'{nome}, você é idoso!')