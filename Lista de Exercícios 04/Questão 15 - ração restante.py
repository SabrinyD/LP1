peso_saco = float(input('Informe o peso do saco de ração em kg: '))
quantidade_racao = float(input('Informe a quantidade de ração fornecida para cada gato em gramas: '))

peso_gramas = peso_saco * 1000
racao_consumida = 2 * quantidade_racao * 5 
racao_restante = peso_gramas - racao_consumida
racao_restante_kg = racao_restante / 1000

print('Após 5 dias restará {} kg de ração'.format(racao_restante_kg))