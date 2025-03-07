def obter_nota():
    while True:
        try:
            nota = float(input("Digite a nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar no intervalo de 0 a 10. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido para a nota.")

def main():
    alunos_aprovados = 0
    while True:
        print("igite as notas do aluno:")
        nota1 = obter_nota()
        nota2 = obter_nota()
        
        media = (nota1 + nota2) / 2
        print(f"Média do aluno: {media:.2f}")

        if media >= 7:
            alunos_aprovados += 1
        
        resposta = input("Calcular a média de um outro aluno [S]im ou [N]ão? ").strip().upper()
        if resposta != 'S':
            break
    
    print(f"Quantidade de alunos aprovados: {alunos_aprovados}")

if __name__ == "__main__":
    main()
