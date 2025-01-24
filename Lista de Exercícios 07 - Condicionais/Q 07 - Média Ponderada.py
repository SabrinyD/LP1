tipo = input("Escolha o tipo de média desejada ('A'ritmética/'P'onderada): ")
tipo = tipo.upper()

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

if (tipo == 'A'):
    media = (nota1 + nota2 + nota3) / 3
elif (tipo == 'P'):
    media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10
else:
    media = 0 
    print ('Tipo de média desconhecido!')

print (f'Sua média é: {media: .1f}')