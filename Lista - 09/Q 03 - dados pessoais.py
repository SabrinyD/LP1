def obter_dados():
    try:
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        if sexo not in ['M', 'F']:
            raise ValueError("Sexo inválido! Deve ser 'M' ou 'F'.")
        
        altura = float(input("Digite a altura (em metros): "))
        if altura <= 0:
            raise ValueError("A altura deve ser um valor positivo.")
        
        return sexo, altura
    except ValueError as e:
        print(f"Erro: {e}")
        return None, None

def processar_dados():
    homens = 0
    mulheres = []
    alturas = []
    
    for i in range(10):
        print(f"Pessoa {i+1}:")
        sexo, altura = obter_dados()
        
        if sexo is not None:
            alturas.append(altura)
            if sexo == 'M':
                homens += 1
            elif sexo == 'F':
                mulheres.append(altura)
    
    return homens, mulheres, alturas

def main():
    homens, mulheres, alturas = processar_dados()

    if alturas:  
        maior_altura = max(alturas)
        menor_altura = min(alturas)

        if mulheres:  
            media_altura_mulheres = sum(mulheres) / len(mulheres)
        else:
            media_altura_mulheres = 0
        
        print(f"Maior altura: {maior_altura}m")
        print(f"Menor altura: {menor_altura}m")
        print(f"Média de altura das mulheres: {media_altura_mulheres:.2f}m")
        print(f"Número de homens: {homens}")
    else:
        print("Nenhuma altura válida foi registrada.")

if __name__ == "__main__":
    main()
