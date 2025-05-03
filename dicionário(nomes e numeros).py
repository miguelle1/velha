agenda = {}

while True:
    nome = input("Nome (ou 'sair' para terminar): ")

    if nome.lower() == "sair":
        break

    numero = input("Número de telefone: ")
    agenda[nome] = numero

print("\nAgenda:")
for nome, numero in agenda.items():
    print(f"{nome}: {numero}")