def obter_numeros():
    numeros = []
    for i in range(10):
        while True:
            try:
                numero = int(input(f"Digite o {i+1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Erro: Digite um número válido.")
    return numeros

def separar_pares_e_impares(numeros):
    pares = [numero for numero in numeros if numero % 2 == 0]
    impares = [numero for numero in numeros if numero % 2 != 0]
    return pares, impares

def exibir_numeros(pares, impares):
    print("\nNúmeros pares:")
    print(pares)
    print("\nNúmeros ímpares:")
    print(impares)

def main():
    numeros = obter_numeros()
    pares, impares = separar_pares_e_impares(numeros)
    exibir_numeros(pares, impares)

if __name__ == "__main__":
    main()
