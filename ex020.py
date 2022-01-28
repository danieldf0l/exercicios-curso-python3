from random import shuffle
Item1 = input('Insira o primeiro item da lista: ')
Item2 = input('Insira o segundo item da lista: ')
Item3 = input('Insira o terceiro item da lista: ')
Item4 = input('Insira o quarto item da lista: ')
Lista = [Item1, Item2, Item3, Item4]
shuffle(Lista)
print(f'A ordem aleatória destes itens é: {Lista}')