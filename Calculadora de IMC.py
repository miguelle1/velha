from tkinter import *
from tkinter import messagebox


tela1 = Tk()
tela1.title('Calculadora de IMC')
tela1.geometry('380x500+500+100')
tela1.wm_resizable(width=False, height=False)

azul = '#262DB6'

lb2 = Label(tela1, text="Calculadora de IMC", font='Time 20 bold', fg=azul)
lb2.place(width=395, height=50, x=-5, y=10)

lb1 = Label(tela1, text="Peso (Kg)", font='Time 10 bold')
lb1.place(width=65, height=50, x=90, y=65)
input_peso = Entry(tela1, font='Time 10 bold')
input_peso.place(width=100, height= 20, x=165, y=80)

lb1 = Label(tela1, text="Altura (Cm)", font='Time 10 bold')
lb1.place(width=75, height=50, x=85, y=125)
input_altura = Entry(tela1, font='Time 10 bold')
input_altura.place(width=100, height= 20, x=170, y=140)

def calcular_imc():
    peso = float(input_peso.get())
    altura = float(input_altura.get()) / 100
    imc = peso / (altura ** 2)
    texto  = "IMC:" + str(round(imc, 2))
    label_resultado = Label(tela1, text=texto, font="Arial 12")
    label_resultado.place(x=30, y=250, width=300, height=30)

    if imc < 18.5:
        imagem_path = "underweight.png"
    elif imc < 24.9:
        imagem_path = "normal.png"
    elif imc < 29.9:
        imagem_path = "overweight.png"
    elif imc < 39.9:
        imagem_path = "obesity.png"
    else:
        imagem_path = "extreme obesity.png"

    imagem = PhotoImage(file=imagem_path)
    label_imagem = Label(tela1, image=imagem)
    label_imagem.place(x=80, y=290, width=200, height=205)
    label_imagem.image = imagem


button1 = Button(tela1, text="Calcular IMC", font="Time 10 bold", command=calcular_imc)
button1.place(x=130, y=200)


tela1.mainloop()