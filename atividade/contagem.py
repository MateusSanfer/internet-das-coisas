numeros = [5, -3, 10, 8, -2, 15, 7, -9, 4, 6]

contPositivos = 0
contNegativos = 0
positivos = []
negativos = []

for x in numeros:
    if x > 0:
        positivos.append(x)
        contPositivos += 1
    else: 
        negativos.append(x)
        contNegativos += 1
        
print(f"Quantidade de números positivos {contPositivos}")
print(f"Quantidade de números negativos {contNegativos}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
        