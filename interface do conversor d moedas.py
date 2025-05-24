from tkinter import ttk
from tkinter import *
import requests

def converter():
    de = moeda_de.get()
    para = moeda_para.get()
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/{}".format(de + "-" + para))
    cotacao = cotacao.json()
    cotacao_moeda = float(cotacao["{}".format(de + para)]["bid"])

    valor = float(valor_input.get())
    r = round(valor * cotacao_moeda, 2)

    conversao = Label(jumi, text=r, font='Time 16 bold', anchor='w', fg=vermelho)
    conversao.place(width=200, height=30, x=120, y=120)



list = ['EUR', 'USD', 'BRL']

azul = "#40596B"
branco = "#FFFFFF"
vermelho = '#B53128'
preto = '#02040D'

jumi = Tk()
jumi.title('Conversor de Moedas')
jumi.geometry('320x500+200+50')
jumi.wm_resizable(width=False, height=False)

jumititulo = Label(jumi, text="Conversor de Moedas", font='Time 20 bold', bg = azul, fg = branco)
jumititulo.place(width=395, height=50, x=-35, y=25)

label_de = Label(jumi, text='De', font='Time 15 bold', fg=preto, anchor='w')
label_de.place(width=100, height=20, x=10, y=200)
moeda_de = ttk.Combobox(jumi, font='Time 11 bold', justify=CENTER)
moeda_de.place(width=110, height=30, x=11, y=228)
moeda_de['values']=(list)

label_para = Label(jumi, text='Para', font='Time 15 bold', fg=preto, anchor='w')
label_para.place(width=100, height=20, x=185, y=200)
moeda_para = ttk.Combobox(jumi, font='Time 11 bold', justify=CENTER)
moeda_para.place(width=110, height=30, x=186, y=228)
moeda_para['values']=(list)

valor_input = Entry(jumi, justify=CENTER)
valor_input.place(width=290, height=40, x=10, y=300)

button = Button(jumi, text="Converter", font="Time 10 bold", bg=azul, fg=branco, command=converter)
button.place(width=290, height=40, x=10, y=370)



jumi.mainloop()