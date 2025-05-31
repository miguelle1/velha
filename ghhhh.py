import tkinter as tk

class IntroScreen:
    def __init__(self, master, on_start):
        self.master = master
        self.master.title("Introdução ao Jogo")

        self.texts = [
            "Bem-vindo ao Escape Room Químico!",
            "Estás preso num laboratório secreto.",
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
            self.label.destroy()
            self.next_button.destroy()
            self.on_start()


def cenario_1(root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, width=600, height=400, bg="#e6f2ff")
    canvas.pack()

    # Piso
    canvas.create_rectangle(0, 280, 600, 400, fill="#cccccc", outline="")

    # Bancada
    canvas.create_rectangle(100, 250, 500, 280, fill="#4d4d4d")

    # Frascos na bancada
    canvas.create_oval(130, 200, 160, 250, fill="#66ccff")  # Frasco 1
    canvas.create_oval(180, 210, 210, 250, fill="#ff9999")  # Frasco 2
    canvas.create_oval(230, 190, 260, 250, fill="#99ff99")  # Frasco 3

    # Porta trancada (lado direito)
    canvas.create_rectangle(480, 180, 560, 300, fill="#E9DCDB", outline="#402000", width=3, tags="porta")
    canvas.create_oval(550, 240, 558, 248, fill="gold", tags="porta")
    canvas.create_rectangle(495, 235, 535, 245, fill="gray20", tags="porta")

    # Luz no teto
    canvas.create_oval(270, 50, 330, 90, fill="yellow", outline="orange")

    frame_opcoes = tk.Frame(root)
    frame_opcoes.pack(pady=10)

    pergunta_label = tk.Label(frame_opcoes, text="A porta é feita de ferro com óxido de cálcio (CaO).\nPoção azul: fria, vermelha: ácida, verde: neutralizante.\nQual poção usar?")
    pergunta_label.pack()

    resposta_label = tk.Label(frame_opcoes, text="", fg="blue")
    resposta_label.pack(pady=5)

    avancar_btn = tk.Button(
        frame_opcoes,
        text="Avançar para próxima sala",
        command=lambda: cenario2(root),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12),
        activebackground="#45a049",
        cursor="hand2",
        relief="raised"
    )
    avancar_btn.pack(pady=10)
    avancar_btn.pack_forget()  # Começa oculto

    def usar_pocao(pocao):
        if pocao == "vermelha":
            resposta_label.config(text="Usaste a poção ácida! A porta está a dissolver-se... 💥")
            canvas.delete("porta")
            avancar_btn.pack(pady=10)  # Mostra botão
        else:
            resposta_label.config(text="Nada aconteceu.")

    botoes_frame = tk.Frame(frame_opcoes)
    botoes_frame.pack(pady=5)

    tk.Button(botoes_frame, text="Poção Azul", command=lambda: usar_pocao("azul")).pack(side="left", padx=5)
    tk.Button(botoes_frame, text="Poção Vermelha", command=lambda: usar_pocao("vermelha")).pack(side="left", padx=5)
    tk.Button(botoes_frame, text="Poção Verde", command=lambda: usar_pocao("verde")).pack(side="left", padx=5)


def cenario2(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Você entrou na sala secreta! 🧪", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="Para abrir o cofre, clique na sequência correta de elementos químicos:", font=("Arial", 12)).pack(pady=10)

    resposta_label = tk.Label(root, text="", fg="blue")
    resposta_label.pack(pady=5)

    sequencia_correta = ["H", "O", "Na"]
    sequencia_usuario = []

    def clicar_elemento(elemento):
        sequencia_usuario.append(elemento)
        resposta_label.config(text=f"Sequência atual: {' - '.join(sequencia_usuario)}")

        if len(sequencia_usuario) == len(sequencia_correta):
            if sequencia_usuario == sequencia_correta:
                resposta_label.config(text="Cofre aberto! Parabéns, você escapou! 🎉")
                for btn in botoes:
                    btn.config(state="disabled")
            else:
                resposta_label.config(text="Sequência incorreta! Tente novamente.")
                sequencia_usuario.clear()

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10)

    elementos = ["H", "O", "Na", "Cl", "C"]
    botoes = []
    for elem in elementos:
        btn = tk.Button(frame_botoes, text=elem, width=6, command=lambda e=elem: clicar_elemento(e))
        btn.pack(side="left", padx=5)
        botoes.append(btn)


# ----------------------------

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x450")
    IntroScreen(root, lambda: cenario_1(root))
    root.mainloop()
