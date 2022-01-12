from math import hypot
catetoOposto = float(input('Insira o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Insira o comprimento do cateto adjacente: '))
###hipotenusa = (catetoOposto**2 + catetoAdjacente**2)**(1/2)
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'o comprimento da hipotenusa é de {hipotenusa:.2f}')
