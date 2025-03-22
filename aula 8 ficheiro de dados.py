def cadastrar():
    nome = input("Inserir Nome:")
    idade = int(input("Inserir Idade:"))
    with open("listadeidades.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(nome + "\n")
        ficheiro.write(str(idade) + "\n")


def buscar():
    nome = input("Procurar Idade de:")
    with open("listadeidades.txt", "r", encoding="utf-8") as ficheiro:
       for linha in ficheiro:
           if nome in linha:
               print("Idade:" + ficheiro.readline())


print("-="*12)
print("Manipulação de Dados")
print("-=" * 12)

while True:
    print("0 - Sair \n1 - Cadastrar \n2 - Buscar")
    a = int(input("Opção Desejada:"))
    if a == 0:
        print("Saíste do Programa")
        break

    if a == 1:
        cadastrar()
    if a == 2:
        buscar()

