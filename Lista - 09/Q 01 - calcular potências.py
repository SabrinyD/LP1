def calcular_potencias(numero): 
    try:
        quadrado = numero ** 2
        cubo = numero ** 3
        return quadrado, cubo
    except TypeError:
        print("Erro: O valor fornecido não é um número válido.")
        return None, None

def imprimir_tabela():
    print(f"{'NUM'} | {'QUADRADO'} | {'CUBO'}")
    for num in range(11):
        quadrado, cubo = calcular_potencias(num)
        print(f"{num} | {quadrado} | {cubo}")

if __name__ == '__main__':
    imprimir_tabela()