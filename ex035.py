reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta2 + reta1:
    print('Os segmentos de reta PODEM formar um triângulo')
else:
    print('Os segmentos de reta NÃO PODEM formar um triângulo')
