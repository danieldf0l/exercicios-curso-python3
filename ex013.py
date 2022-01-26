salario = float(input('Insira o salário do funcionário: R$'))
porcentagem = int(input('Insira a % de acréssimo do salário: '))
aumento = porcentagem*salario/100
print(f'O salário de {salario} após um aumento de {porcentagem} será de R${salario + aumento:.2f}')
