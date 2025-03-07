def solicitar_nome():
    nome = input("Digite um nome: ")
    return nome

def adicionar_nome(lista, nome):
    lista.append(nome)

def exibir_nomes(lista):
    print("Lista de nomes:")
    for nome in lista:
        print(nome)

def main():
    nomes = []
    
    for i in range(5):
        nome = solicitar_nome()  # Solicita o nome
        adicionar_nome(nomes, nome)  # Adiciona o nome à lista
    
    exibir_nomes(nomes)

if __name__ == "__main__":
    main()
