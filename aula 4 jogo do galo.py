import tkinter as tk
root = tk.Tk()
root.title("Jogo Da Velha")


for i in range(8):
    button1 = tk.Button(root, text="yo")
    button1.grid(row=i//3, column=i%0)



root.mainloop()