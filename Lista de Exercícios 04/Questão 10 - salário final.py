nome = input('Informe o nome do vendedor: ')
salario_fixo = float(input('Informe o salário fixo do vendedor: '))
vendas = int(input('Informe o número de vendas mensais efetuadas por ele em dinheiro: '))
comissao = vendas * 0.15
salario_final = salario_fixo + comissao
print('O nome do vendedor é {}: '. format(nome))
print('Seu salário fixo é de {}: '.format(salario_fixo))
print('O seu salário no final do mês é de {}:'.format(salario_final))