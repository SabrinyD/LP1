nota1 = float(input('Informe a primeira nota: '))   
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print (f'Sua média é: {media}!')

if (media >= 6):
    print('Aprovado!')
else:
    print('Reprovado!')