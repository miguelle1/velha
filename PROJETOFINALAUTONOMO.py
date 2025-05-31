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


#---------------------------------------------------------------------------------------------------------


def cenario_1():
    # Aqui você colocaria o código para iniciar a janela principal do jogo
    game_root = tk.Tk()
    game_root.title("Jogo Escape Room")
    canvas = tk.Canvas(game_root, width=600, height=400, bg="#e6f2ff")
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
    canvas.create_rectangle(480, 180, 560, 300, fill="#E9DCDB", outline="#402000", width=3, tags="porta")  # porta
    canvas.create_oval(550, 240, 558, 248, fill="gold", tags="porta")  # maçaneta
    canvas.create_rectangle(495, 235, 535, 245, fill="gray20", tags="porta")  # tranca

    # Luz no teto
    canvas.create_oval(270, 50, 330, 90, fill="yellow", outline="orange")

    #desenvolvimento

    frame_opcoes = tk.Frame(game_root)
    frame_opcoes.pack(pady=10)

    # Pergunta
    pergunta_label = tk.Label(frame_opcoes, text="A porta é feita de ferro com revestimento de óxido de cálcio (CaO):\num material duro, alcalino e resistente à água, mas vulnerável a uma certa coisa..\nA poção azul é uma poção fria, a vermelha é ácida e a verde é neutralizante.\nUma delas corrói a porta devido à reação química.\nQual poção desejas usar para abrir a porta?")
    pergunta_label.pack()

    # Label de resposta
    resposta_label = tk.Label(frame_opcoes, text="", fg="blue")
    resposta_label.pack(pady=5)




    #------------------------------------------------------------------------------------------------------------------------


    # Funções dos botões
    def usar_pocao(pocao):
        if pocao == "vermelha":
            resposta_label.config(text="Usaste a poção ácida! A porta está a dissolver-se... 💥")
            # Aqui você pode fazer a porta "sumir" do canvas se quiser
            canvas.delete("porta")
        else:
            resposta_label.config(text="Nada aconteceu. Essa poção não afeta a porta.")

    # Botões das poções
    botoes_frame = tk.Frame(frame_opcoes)
    botoes_frame.pack(pady=5)

    tk.Button(botoes_frame, text="Poção Azul", command=lambda: usar_pocao("azul")).pack(side="left", padx=5)
    tk.Button(botoes_frame, text="Poção Vermelha", command=lambda: usar_pocao("vermelha")).pack(side="left", padx=5)
    tk.Button(botoes_frame, text="Poção Verde", command=lambda: usar_pocao("verde")).pack(side="left", padx=5)




#---------------------------------------------------------------------------------------------------------------


def cenario2():
    game_root = tk.Tk()
    for widget in game_root.winfo_children():
        widget.destroy()

        label_instrucao = tk.Label(game_root, text="Você entrou na sala secreta! 🧪\nPara abrir o cofre, clique na sequência correta de elementos químicos:", font=("Arial", 14))
        label_instrucao.pack(pady=15)

        resposta_label = tk.Label(game_root, text="", fg="blue")
        resposta_label.pack(pady=5)

        # Sequência correta (exemplo)
        sequencia_correta = ["H", "O", "Na"]
        sequencia_usuario = []

        def clicar_elemento(elemento):
            nonlocal sequencia_usuario
            sequencia_usuario.append(elemento)
            resposta_label.config(text=f"Sequência atual: {' - '.join(sequencia_usuario)}")

            if len(sequencia_usuario) == len(sequencia_correta):
                if sequencia_usuario == sequencia_correta:
                    resposta_label.config(text="Cofre aberto! Parabéns, você escapou! 🎉")
                    for btn in botoes:
                        btn.config(state="disabled")
                else:
                    resposta_label.config(text="Sequência incorreta! Tente novamente.")
                    sequencia_usuario = []

        frame_botoes = tk.Frame(game_root)
        frame_botoes.pack(pady=10)

        elementos = ["H", "O", "Na", "Cl", "C"]
        botoes = []
        for elem in elementos:
            btn = tk.Button(frame_botoes, text=elem, width=6, command=lambda e=elem: clicar_elemento(e))
            btn.pack(side="left", padx=5)
            botoes.append(btn)


#-------------------------------------------------------------------------------


if __name__ == "__main__":
    root = tk.Tk()
    intro = IntroScreen(root, cenario_1)
    root.mainloop()
