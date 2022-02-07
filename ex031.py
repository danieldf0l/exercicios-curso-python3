Distancia = float(input('Insira a distância (em Km) da viagem: '))
if Distancia > 200:
    print(f'O valor da passagem é de R${Distancia * 0.45:.2f}')
else: 
    print(f'O valor da passagem é de R${Distancia * 0.50:.2f}')
