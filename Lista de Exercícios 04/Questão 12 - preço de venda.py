preco_compra = float(input('Informe o preço da compra: '))
lucro = int(input('Informe o percentual de lucro desejado: '))
percentual = (preco_compra * lucro) / 100 
preco_venda = preco_compra + percentual
print('O preço de venda será de: {} '.format(preco_venda))