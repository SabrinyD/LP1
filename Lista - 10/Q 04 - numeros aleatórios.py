import random

numeros = random.sample(range(1, 101), 7)

numero_informado = int(input('Digite um número: '))

encontrou = False
for numero in numeros:
    if numero == numero_informado: 
        encontrou = True

if encontrou: 
    print('Número encontrado!')
else: 
    print('Número não encontrado!')

print(f"Lista gerada: {numeros}")