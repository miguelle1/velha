from tkinter import *
jumi = Tk()
jumi.title('Conversor de Moedas')
jumi.geometry('320x400+200+50')
jumi.wm_resizable(width=False, height=False)

azul = "#96D6DF"
branco = "#FFFFFF"


jumititulo = Label(jumi, text="Conversor de Moedas", font='Time 20 bold', bg = azul, fg = branco)
jumititulo.place(width=395, height=50, x=-35, y=25)





jumi.mainloop()