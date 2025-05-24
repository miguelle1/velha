import tkinter as tk

class IntroScreen:
    def __init__(self, master, on_start):
        self.master = master
        self.master.title("Introdução ao Jogo")

        self.texts = [
            "Bem-vindo ao Escape Room Químico!",
            "Estás preso em um laboratório secreto.",
            "O teu objetivo é resolver enigmas e escapar antes que seja tarde.",
            "Boa sorte!"
        ]
        self.index = 0
        self.on_start = on_start

        self.label = tk.Label(master, text=self.texts[self.index], font=("Arial", 16), wraplength=400, pady=20)
        self.label.pack()

        self.next_button = tk.Button(master, text="Próximo", command=self.next_text)
        self.next_button.pack(pady=10)

    def next_text(self):
        self.index += 1
        if self.index < len(self.texts):
            self.label.config(text=self.texts[self.index])
        else:
            # Quando acabar, chama a função para iniciar o jogo
            self.master.destroy()
            self.on_start()

def start_game():
    # Aqui você colocaria o código para iniciar a janela principal do jogo
    game_root = tk.Tk()
    game_root.title("Jogo Escape Room")
    tk.Label(game_root, text="Aqui começa o jogo!", font=("Arial", 18)).pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    intro = IntroScreen(root, start_game)
    root.mainloop()
