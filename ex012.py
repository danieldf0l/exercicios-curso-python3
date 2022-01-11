valorProduto = float(input('Insira o valor do produto: R$'))
porcentagem = int(input('Insira a % de desconto deste produto: '))
valorDesconto = porcentagem*valorProduto/100
print(f'O valor final é de: R${valorProduto-valorDesconto:.2f} ')
