numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe um segundo número: '))
numero3 = int(input('Informe um terceiro número: '))

if (numero1 >= numero2 and numero1 >= numero3):
    maior = numero1
elif (numero2 >= numero1 and numero2 >= numero3):
    maior = numero2
else: 
    maior = numero3

print (f'O maior número é: {maior}')