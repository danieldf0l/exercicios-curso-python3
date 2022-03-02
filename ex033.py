valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
maior = valor1
if valor2 > valor3 and valor2 > valor1:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
menor = valor1
if valor2 < valor3 and valor2 < valor1:
    menor = valor2
if valor3 < valor1 and valor2:
    menor = valor3
print(f'O MAIOR valor digitado foi: {maior}')
print(f'O MENOR valor digitado foi: {menor}')
