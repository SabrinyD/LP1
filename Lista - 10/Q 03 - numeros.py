numeros = [1,2,3,5,12,34,7]

numero_informado = int(input('Digite um número: '))

encontrou = False
for numero in numeros:
    if numero == numero_informado: 
        encontrou = True

if encontrou: 
    print('Número encontrado!')
else: 
    print ('Número não encontrado!')
