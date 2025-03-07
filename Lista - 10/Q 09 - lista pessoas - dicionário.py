def corrigir_chaves(pessoa):
    pessoa_corrigida = {}
    for chave, valor in pessoa.items():
        pessoa_corrigida[chave.lower()] = valor
    return pessoa_corrigida

def exibir_nomes_e_sobrenomes(pessoas):
    for pessoa in pessoas:
        nome = pessoa.get('nome', 'Desconhecido')
        sobrenome = pessoa.get('sobrenome', 'Desconhecido')
        print(f"{nome} {sobrenome}")

def main():
    pessoas = [
        {'nome': 'João', 'sobrenome': 'Silva'},
        {'NOME': 'Maria', 'SOBRENOME': 'Oliveira'},
        {'nome': 'Carlos', 'sobrenome': 'Pereira'},
        {'NOME': 'Ana', 'SOBRENOME': 'Costa'},
        {'nome': 'Pedro', 'sobrenome': 'Santos'}
    ]
    
    pessoas_corrigidas = [corrigir_chaves(pessoa) for pessoa in pessoas]

    exibir_nomes_e_sobrenomes(pessoas_corrigidas)

if __name__ == "__main__":
    main()
