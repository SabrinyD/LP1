a = int(input('Informe um valor: '))
b = int(input('Informe um segundo valor: '))
c = int(input('Informe um terceiro valor: '))

if a > 0 and b > 0 and c > 0:
    if (a < b + c) and (b < a + c) and (c < a + b):
        s = (a + b + c) / 2

        area = (s * (s-a) * (s-b) * (s-c))
        print('Os valores formam um triângulo.')
        print(f'A área do triângulo é: {area: .2f}')
    else:
        print('Os valores não formam um triângulo.')
        