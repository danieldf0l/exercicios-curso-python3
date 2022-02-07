print('Verificando se um número é PAR ou ÍMPAR')
Numero = int(input('Insira o número: '))
RestoDivisao = Numero % 2
if RestoDivisao == 0:
    print(f'{Numero} é PAR!')
else:
    print(f'{Numero} é ÍMPAR!')
