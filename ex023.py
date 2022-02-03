Numero = int(input('Insira um número: '))
Unidade = Numero//1%10
Dezena = Numero//10%10
Centena = Numero//100%10
Milhar = Numero//1000%10
print(f'Analisando o número {Numero}...')
print(f'Unidade: {Unidade}')
print(f'Dezena: {Dezena}')
print(f'Centena: {Centena}')
print(f'Milhar: {Milhar}')