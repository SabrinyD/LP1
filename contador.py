git remoto adicionar origem https://github.com/SabrinyD/LP1.git
 git branch -M principal 
git push -u origem principal
contador = 0 
numero = 10
while numero <= 20:
    if numero % 2 == 1: 
        contador = contador + 1
    numero = numero + 1 
print (f'A quantidade de números ímpares é: {contador}')