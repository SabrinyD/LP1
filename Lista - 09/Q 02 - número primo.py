def primo(numero):
    if numero < 2:
        print(f"{numero} não é um número primo!")
        return
    
    quantidade_divisores = 0
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1
    
    if quantidade_divisores == 2:
        print(f"{numero} é um número primo!")
    else:
        print(f"{numero} não é um número primo!")

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        primo(numero)
    except ValueError:
        print("Erro: Informe um número inteiro válido!")