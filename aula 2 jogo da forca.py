#1 escolher aleatoriamente uma palavra +
#2 atribuir uma letra
#3 define se existe a letra na palavra
#4 número máximo de tentativas +
#5 terminar o jogo com vitória ou derrota

import random
def escolher_palavra():
    palavras=("casa", "carro", "floresta", "montanha", "navio")
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_adivinhadas):
    palavra_adivinhada = ""
    for x in palavra:
        if x in letras_adivinhadas:
            palavra_adivinhada += x
        else:
            palavra_adivinhada += "_"
    print("Palavra:", palavra_adivinhada)

def jogar():
    palavra = escolher_palavra()
    print(palavra)
    tentativas = 6

    #criar lista de letras adivinhadas

    letras_adivinhadas = []
    while tentativas>0:
        mostrar_palavra(palavra, letras_adivinhadas)
        letra = input("escolhe uma letra").lower()

        #verificar se a letra já foi adivinhada

        if letra in letras_adivinhadas:
            print("Letra usada, tenta outra")
            continue

        letras_adivinhadas.append(letra)

    #verificar se a letra pertence à palavra

        if letra in palavra:
            print("Boa! Essa letra pertence à palavra")
        else:
            print("Errado! Essa letra não pertence à palavra")
            tentativas -= 1
        if tentativas == 0:
            print("Perdeste o jogo")


        palavra_adivinhada = True
        for i in palavra:
            if i not in letras_adivinhadas:
                palavra_adivinhada = False
                break
        if palavra_adivinhada:
            print("Parabéns! Ganhaste o jogo")
            break

jogar()