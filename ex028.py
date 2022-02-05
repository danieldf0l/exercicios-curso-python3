from random import randint
NumeroComputador = randint(1, 5)
print('um número de 1 à 5 será sorteado, digite seu palpite')
print('--' * 26)
NumeroUsuario = int(input('Insira seu palpite: '))
print('--' * 26)
if NumeroComputador == NumeroUsuario:
    print('Parabéns, você acertou!!')
else:
    print('Infelizmente você não conseguiu. tente novamente.')
