numero = int(input('Informe um número inteiro: '))

def verificar_primo(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
if verificar_primo (numero):
    print(f'{numero} é um número primo.')
else: 
    print(f'{numero} não é um número primo.')