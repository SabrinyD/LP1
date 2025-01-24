horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
valor_hora = float(input('Informe o valor da hora de trabalho: '))
desconto = float(input('Informe o valor de desconto (imposto) do salário: '))

salario_bruto = horas_trabalhadas * valor_hora
valor_descontado = (salario_bruto * desconto) / 100
salario_liquido = salario_bruto - valor_descontado

print('O seu salário bruto é de: {}'.format(salario_bruto))
print('O valor descontado do seu salário é de: {}'.format(valor_descontado))
print('O seu salário líquido é de: {}'.format(salario_liquido))

