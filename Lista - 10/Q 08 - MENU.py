opcao = 0
opcoes = [1,2,3]
while opcao not in opcoes: 
    print('Selecione uma das opções a seguir: ')
    print('1 - Olá mundo')
    print('2 - Eu programo em Pyhton')
    print('3 - Laçoes de repetição')
    opcao = int(input('Opção: '))

if (opcao == 1):
    print('Foi a escolhida a opção 1')

elif (opcao == 2):
    print('Foi escolhida a opção 2')

elif (opcao == 3):
    print('Foi escolhida a opção 3')