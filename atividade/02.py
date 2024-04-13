nome = 'Marcio'

# Desconto

salarioBruto = 9876
ir = salarioBruto*0.08
inss = salarioBruto*0.05

planoDeSaude = 150
salarioFinal = salarioBruto - ir - inss - planoDeSaude
descontoTotal = salarioBruto - salarioFinal

print(nome, "o seu salário final é", salarioFinal)
print("Desconto Total:", round(descontoTotal, 2))
