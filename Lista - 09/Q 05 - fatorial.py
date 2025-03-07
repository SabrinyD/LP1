def fatorial(n):
    if n < 0:
        raise ValueError("O número deve ser maior ou igual a 0.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def main():
    try:
        numero = int(input("Digite um número para calcular o fatorial: "))
        print(f"O fatorial de {numero} é {fatorial(numero)}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
