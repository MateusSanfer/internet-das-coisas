import random
import os

nSorteado = random.randint(1,1000)

while True:
    palpite = int(input("Digite um numero entre 1 e 1000:"))
    os.system('cls')
    
    if palpite == nSorteado:
        print(f"Parabéns!! Você acertou {nSorteado}")
        break
    
    elif palpite < nSorteado:
        print('O seu palpite é menor que o numero Sorteado!')
        
    else:
        print('O seu palpite é maior que o numero Sorteado!')
        