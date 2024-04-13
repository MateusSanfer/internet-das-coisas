import os

nome = input("Digite seu nome: ")
os.system('clear')
peso = int(input("Digite seu peso: "))
os.system('clear')
altura = float(input("Digite sua altura:"))
os.system('clear')

imc = round(peso/(altura**2))

if imc < 18.5:
    print(f"{nome}, seu IMC é {imc:.2f}, você esta abaixo do peso.")
    # Serve para arredondar/formatar o numero
    
elif imc >= 18.5 and imc <= 24.9:
     print(f"{nome}, seu IMC é {imc}, você esta com o peso normal.")
     
elif imc >= 24.9 and imc <= 29.9:
      print(f"{nome}, seu IMC é {imc}, você esta acima peso.")
      
elif imc >= 29.9 and imc <= 39.9:
    print(f"{nome}, seu IMC é {imc}, você esta com obsidade grau I.")
    
else:
     print(f"{nome}, seu IMC é {imc}, você esta com obsidade grau II.")


