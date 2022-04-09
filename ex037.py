numeroInteiro = int(input('Insira um número inteiro: '))
print("""Você deseja converter para qual base numérica?
[1] Para converter DECIMAL - BINÁRIO
[2] Para converter DECIMAL - OCTAL 
[3] Para converter DECIMAL - HEXADECIMAL""")
escolha = int(input('Insira sua opção: '))
if escolha == 1:
    print(f'{numeroInteiro} em BINÁRIO é: {bin(numeroInteiro)[2:]}')
elif escolha == 2:
    print(f'{numeroInteiro} em OCTAL é: {oct(numeroInteiro)[2:]}')
elif escolha == 3:
    print(f'{numeroInteiro} em HEXADECIMAL é: {hex(numeroInteiro)[2:]}')
else:
    print('Esta não é uma opção válida, reinicie o programa e tente novamente')
