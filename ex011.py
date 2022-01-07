l = float(input("Insira a LARGURA da parde, em Metros: "))
a = float(input("Insira a ALTURA da parede, em Metros: "))
h = l * a
print(
    f"""se a dimnesão da parede é de {l}x{a}, ela tem uma área de {h:.2f}m²\nSerão necessários {h/2:.2f}l de tinta"""
)
