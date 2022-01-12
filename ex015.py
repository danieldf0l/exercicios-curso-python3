dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual a distância percorrida com o carro, em Km? '))
print(f'O valor para ser pago pelo aluguel do veículo é de R${(dias*60)+(km*0.15):.2f}')
