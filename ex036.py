valorCasa = float(input('Insira o valor da casa: '))
salarioComprador = float(input('Insira o salário do potencial comprador: '))
prestacoes = float(input('Insira em quantos anos esta casa será paga: '))
valorprestacao = valorCasa / (prestacoes*12)
print(f'Para quitar uma casa de R${valorCasa:.2f} em {prestacoes:.2f} anos, serão R${valorprestacao:.2f}/Mês')
if valorprestacao <= (salarioComprador * 30/100):
    print(valorprestacao)
    print(f'O valor das prestações não excede o limite de 30% do salário do comprador. Empréstimo CONCEDIDO')
else:
    print(valorprestacao)
    print(f'O valor da prestação excede ao limite de 30% do salário do possível comprador. empréstimo NEGADO')
