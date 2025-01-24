valor1 = int(input('Informe um número: '))
valor2 = int(input('Informe um segundo número: '))

if (valor1 % valor2 == 0) or (valor2 % valor1 == 0):
    print ('São múltiplos!')
else: 
    print('Não são múltiplos!')