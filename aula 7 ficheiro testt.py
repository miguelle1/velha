def criar_ficheiro():
    nome_ficheiro = input("Digite o nome do ficheiro:")
    nome_completo = f"{nome_ficheiro}.txt"

    with open(nome_completo, "w") as ficheiro:
        pass

    print(f"Ficheiro {nome_completo} criado com sucesso!")




def inserir_frase():
    nome_ficheiroo = input("Qual é que vai ser o nome do ficheiro?")
    nome_completoo = f"{nome_ficheiroo}.txt"

    with open(nome_completoo, "a") as ficheiro:
        frase = input("Digite a frase que deseja inserir:")
        ficheiro.write(frase + "\n")
    print(f"Frase adicionada ao ficheiro {nome_completoo} com sucesso!")




def ler_ficheiro():
    nome_ficheiro = input("Nome para o ficheiro")
    nome_completo = f"{nome_ficheiro}.txt"
    with open(nome_completo, "r") as ficheiro:
        conteudo = ficheiro.read()
    print(conteudo)




def menu():
    while True:
        print("\nMenu:")
        print("1 - Criar um ficheiro")
        print("2 - Inserir frase num ficheiro")
        print("3 - Ler conteúdo de um ficheiro")
        print("4 - Sair")
        opcao = input("Escolhe uma opcao:")

        if opcao == "1":
            criar_ficheiro()
        elif opcao == "2":
            inserir_frase()
        elif opcao == "3":
            ler_ficheiro()
        elif opcao == "4":
            break


menu()





