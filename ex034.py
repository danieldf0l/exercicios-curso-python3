salario = float(input('Insira o salário do funcionário que receberá um aumento: '))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
else:
    novoSalario = salario + (salario * 10 / 100)
print(f'Um funcionário com o salário de {salario}, após o aumento, passa a receber R${novoSalario:.2f}')
