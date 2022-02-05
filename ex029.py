VelocidadeCarro = float(input('O carro passou a que velocidade? '))
LimiteVelocidade = 80
if VelocidadeCarro <= LimiteVelocidade:
    print('Nenhum infração de trânsito foi detectada.')
else:
    Multa = (VelocidadeCarro - 80) * 7
    print(f'ATENÇÃO\nO limite de velocidade foi excedidio. a multa a ser paga é de R${Multa:.2f}')
