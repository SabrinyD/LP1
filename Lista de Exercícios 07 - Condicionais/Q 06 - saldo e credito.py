saldo_medio = int(input('Informe o saldo do cliente: '))

if (saldo_medio >= 0) and (saldo_medio <= 200):
    credito = 0
elif (saldo_medio >= 201) and (saldo_medio <= 400):
    credito = (saldo_medio * 20) / 100
elif (saldo_medio >= 401) and (saldo_medio <= 600):
    credito = (saldo_medio * 30) / 100
elif (saldo_medio >= 601):
    credito = (saldo_medio * 40) / 100

print (f'O saldo do cliente é de: {saldo_medio} e o seu crédito é de: {credito}.')