#interface origem
from tkinter import *
from tkinter import messagebox

#função para botão adicionar
def adicionar():
    nome = input_nome.get()
    telemovel = input_telemovel.get()
    endereco = input_endereco.get()
    distrito = input_distrito.get()
    pais = input_pais.get()
    email = input_email.get()

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_nome + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_telemovel + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_endereco + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_distrito + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_pais + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')

    with open("cadastro.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write(input_email + "\n")
    with open("cadastro.txt", "r", encoding="utf-8") as ficheiro:
        for linha in ficheiro:
            print('hygygu')


#interface
tela1 = Tk()
tela1.title('Agenda')
tela1.geometry('380x500+500+100')
tela1.wm_resizable(width=False, height=False)


#Texto e entradas
lb1 = Label(tela1, text="Nome", font='Time 10 bold')
lb1.place(width=50, height=50, x=30, y=65)
input_nome = Entry(tela1, font='Time 10 bold')
input_nome.place(width=250, height= 20, x=90, y=80)

lb1 = Label(tela1, text="Telemóvel", font='Time 10 bold')
lb1.place(width=75, height=50, x=30, y=110)
input_telemovel = Entry(tela1, font='Time 10 bold')
input_telemovel.place(width=200, height= 20, x=115, y=125)

lb1 = Label(tela1, text="Endereço", font='Time 10 bold')
lb1.place(width=75, height=50, x=30, y=155)
input_endereco = Entry(tela1, font='Time 10 bold')
input_endereco.place(width=200, height= 20, x=105, y=170)

lb1 = Label(tela1, text="Distrito", font='Time 10 bold')
lb1.place(width=85, height=50, x=17, y=200)
input_distrito = Entry(tela1, font='Time 10 bold')
input_distrito.place(width=100, height= 20, x=90, y=215)

lb1 = Label(tela1, text="País", font='Time 10 bold')
lb1.place(width=50, height=50, x=200, y=200)
input_pais = Entry(tela1, font='Time 10 bold')
input_pais.place(width=100, height= 20, x=245, y=215)

lb1 = Label(tela1, text="Email", font='Time 10 bold')
lb1.place(width=50, height=50, x=30, y=245)
input_email = Entry(tela1, font='Time 10 bold')
input_email.place(width=250, height= 20, x=90, y=260)


#cores
azul = '#262DB6'
branco = '#F4F5FF'
amarelo = '#F6D101'
vermelho = '#F41212'


#botões
button1 = Button(tela1, text="Adicionar", font="Time 15 bold", bg=azul, fg=branco)
button1.place(x=45, y=310)

button1 = Button(tela1, text="Pesquisar", font="Time 15 bold", bg=azul, fg=branco)
button1.place(x=225, y=310)


#título
lb2 = Label(tela1, text="SHARKCODERS PYTHON", font='Time 20 bold', bg=amarelo, fg=vermelho)
lb2.place(width=395, height=50, x=-5, y=10)


tela1.mainloop()