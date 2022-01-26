from random import choice
Nome1 = str(input('Insira o nome da primeira opção: '))
Nome2 = str(input('Insira o nome da segunda opção: '))
Nome3 = str(input('Insira o nome da terceira opção: '))
ListaNomes = [Nome1, Nome2, Nome3]
print(f'O/A sorteado/a foi: {choice(ListaNomes)}')