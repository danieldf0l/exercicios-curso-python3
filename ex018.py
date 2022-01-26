from math import radians, sin, cos, tan
angulo = int(input('insira o angulo a ser analisado: '))
anguloRadiano = radians(angulo)
seno = sin(anguloRadiano)
cosseno = cos(anguloRadiano)
tangente = tan(anguloRadiano)
print(f"""O ângulo de {angulo:.2f} tem:\nSeno de: {seno:.2f}\nCosseno de: {cosseno:.2f}\nTangente de: {tangente:.2f}""")
