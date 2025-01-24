identificacao = input('Informe o número de identificação: ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
ME = float(input('Informe a média dos exercícios: '))

print(f'Número de Identificação: {identificacao}')
print(f'1ª Nota: {nota1}')
print(f'2ª Nota: {nota2}')
print(f'3ª Nota: {nota3}')

MA = (nota1 + (nota2 * 2) + (nota3 * 3) + ME) / 7
print(f'Média de Aproveitamento: {MA: .1f}')

if (MA == 9.0):
    conceito = 'A'
    
elif (MA >= 7.5) and (MA < 9.0):
    conceito = 'B'
    print(f'Conceito: {conceito}')
    print ('Aprovado!')
elif (MA >= 6.0) and (MA < 7.5):
    conceito = 'C'
    print(f'Conceito: {conceito}')
    print ('Aprovado!')
elif (MA >= 4.0) and (MA < 6.0):
    conceito = 'D'
    print(f'Conceito: {conceito}')
    print ('Reprovado!')
elif (MA > 4.0):
    conceito = 'E'
    print(f'Conceito: {conceito}')
    print ('Reprovado!')


