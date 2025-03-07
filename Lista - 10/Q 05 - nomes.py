nomes = []

for i in range(1,6):
    nome = input('Informe um nome: ')
    nomes.append(nome)
    print(nomes)

posicao = int(input("Digite um número de 0 a 4 para remover o nome dessa posição: "))

if 0 <= posicao < len(nomes):
    nomes.pop(posicao)
    print("Nome removido com sucesso!")
else:
    print("Posição inválida!")

print(f"Lista de nomes atualizada: {nomes}")