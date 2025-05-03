contador = {}

frase = "eu gosto daquilo e daquilo"

palavras = frase.split()

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1


print("\nContador:")
for palavra in contador.items():
    print(f"{palavra}")