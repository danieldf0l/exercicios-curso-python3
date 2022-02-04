Frase = input('Digita a frase que será analisada: ').strip().upper()
Letra = input('Digite a letra que deseja contar na frase: ').strip().upper()
print(f"""A letra {Letra} aparece {Frase.count(Letra)}\nA letra {Letra} aparece pela primeira vez na posição {Frase.find(Letra)+1}\nA lerta {Letra} aparece pela útima vez na posição {Frase.rfind(Letra)+1}""")
