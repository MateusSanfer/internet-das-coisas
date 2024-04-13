salarioBruto = float(input('Digite seu salario Bruto: '))

ir = salarioBruto*0.08
inss = salarioBruto*0.05
salarioFamiliar = salarioBruto * 0.03


if salarioBruto >= 3200:
    salarioLiquido = salarioBruto - ir - inss
    
elif salarioBruto >= 1500 and salarioBruto < 3200:
    salarioLiquido = salarioBruto - inss
    
else:
    salarioLiquido = salarioBruto + salarioFamiliar - inss
    
print(f"Seu salario liquido é: {salarioLiquido:.2f}")
    