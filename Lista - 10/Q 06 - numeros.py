numeros = []

for i in range(0,10):
        while True:
            try:
                 numero = int(input(f"Digite o {i+1}º número: "))
                 if numero not in numeros:  # Garantindo que o número seja único
                      break
                 else:
                      print("Número repetido! Digite um número diferente.")
            except ValueError:
                  print("Erro: Digite um número válido.")
    
        if numero % 2 == 0:
             numero += 1
    
        numeros.append(numero)

print("Os números digitados (com possíveis modificações, caso tenha sido digitado um número par) são:")
print(numeros)