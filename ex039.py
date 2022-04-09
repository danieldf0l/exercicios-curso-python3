from datetime import date
anoAtual = date.today().year
anoNasc = int(input('insira seu ano de nascimento'))
idade = anoAtual - anoNasc
if idade == 18:
    print('Este é o seu ano de Alistamento Militar')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda não é sua vez, seu alistamento será em {saldo}')
    print(f'')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
