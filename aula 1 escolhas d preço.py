print("1 - carro")
print("2 - comboio")
print("3 - avião")

carro = 0.5
comboio = 0.3
aviao = 0.7

condutor_privado = 70
bilhetes_privilegiados = 10
jato_privado = 900

opcao = input("Qual das opções escolhes?")
if opcao == ("1"):
    print("Escolheste ir de carro. Terás de pagar", carro, "cêntimos por km")
    segunda_opcao_um = input("Gostarias de ter um condutor privado?")
    if segunda_opcao_um == ("sim"):
        print("Escolheste ter um condutor privado. Terás de pagar", condutor_privado, "euros")
    if segunda_opcao_um == ("não"):
        print("Escolheste não o ter. Poupaste", condutor_privado, "euros")

if opcao == ("2"):
    print("Escolheste ir de comboio. Terás de pagar", comboio,"cêntimos por km")
    segunda_opcao_dois = input("Gostarias de ter bilhetes privilegiados?")
    if segunda_opcao_dois == ("sim"):
        print("Escolheste ter bilhetes privilegiados. Terás de pagar", bilhetes_privilegiados, "euros")
    if segunda_opcao_dois == ("não"):
        print("Escolheste não os ter. Poupaste", bilhetes_privilegiados, "euros")

if opcao == ("3"):
    print("Escolheste ir de avião. Terás de pagar", aviao, "cêntimos por km")
    segunda_opcao_tres = input("Gostarias de ter um jato privado?")
    if segunda_opcao_tres == ("sim"):
        print("Escolheste ter um jato privado. Terás de pagar", jato_privado, "euros")
    if segunda_opcao_tres == ("não"):
        print("Escolheste não o ter. Poupaste", jato_privado, "euros")

