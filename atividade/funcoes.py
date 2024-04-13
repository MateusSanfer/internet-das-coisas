numero = [10, 20, 30, 40, 50]

def media():
    quantidade = len(numero)
    
    soma = sum(numero)
    resultado = soma / quantidade
    return resultado
    
print(f" A média: {media()}")