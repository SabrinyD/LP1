valor_hora = float(input('Informe o valor que você ganha por hora trabalhada: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas por mês: '))

salario_bruto = valor_hora * horas_trabalhadas
inss = (salario_bruto * 8) / 100
ir = (salario_bruto * 11) / 100
sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - inss - ir - sindicato 

print('Salário bruto: R$ {}'.format(salario_bruto))
print('IR (11%): R$ {}'.format(ir))
print('INSS (8%): R$ {}'.format(inss))
print('Sindicato (5%): R$ {}'.format(sindicato))
print('Salário Líquido: R$ {}'.format(salario_liquido))