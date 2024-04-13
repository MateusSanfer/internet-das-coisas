import os

def principal():
    nomes = ["Mateus", "Marcio", "Amanda", "Emerson", "Vinicios", "Gilson", "Evelim", "Fabio"]
    print("Bem vindo ao Jogo da Adivinhação de Nomes")
    print("Tente adinhar um nome")
    
    while True:
        palpite = input('Digite um nome: ').strip().capitalize()
        os.system('cls')
    
        if verificarNome(palpite, nomes):
            print("Parabéns você acertou o nome!")
            break
        else:
            print("Esse nome não existe, tente novamente!")
        
def verificarNome(palpite, nomes):
    if palpite in nomes: # Vai pecorrer o vetor para ver se os dados estão certos
        return True
    else: 
        return False
    
    
principal()