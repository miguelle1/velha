import tkinter as tk

root = tk.Tk()

def teste1():
    print("OLÁ SHARKCODERS")

def teste2():
    print("ADEUS SHARKCODERS")

def teste3():
    print("ENTÃO SHARKCODERS?")


root.title("SHARKCODERS")
root.geometry("300x300+200+200")

root.wm_resizable(width=True, height=True)



button1 = tk.Button(root, text="Click Me", font="Time 15 bold", command=teste1)
button1.place(x=105, y=80)



button2 = tk.Button(root, text="No! Click Me", command=teste2)
button2.place(x=115, y=20)



button3 = tk.Button(root, text="What About Me?", command=teste3)
button3.place(x=105, y=150)


lb1 = tk.Label(root, text="Olá")
lb1.place(width=20, height=10, x=145, y=55)

lb1 = tk.Label(root, text="Tudo bem?")
lb1.place(width=60, height=10, x=125, y=130)

lb1 = tk.Label(root, text="Como te chamas?")
lb1.place(width=100, height=20, x=105, y=190)

root.mainloop()