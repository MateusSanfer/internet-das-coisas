# x = 'testando teste'

# startswith('') Detectar o trecho inicial
# capitalize()
# strip()

# print(y)

nome = input('Digite o seu nome: ').strip().capitalize()

if nome.startswith('D'):
    print('Seu nome começa com D')
else:
    print('Seu nome não começa com a letra D')