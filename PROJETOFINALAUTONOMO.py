import tkinter as tk


def intro():
    global index
    root = tk.Tk()
    root.title("Introdução ao Jogo")

    texts = [
        "Bem-vindo ao Escape Room Químico!",
        "Estás preso em um laboratório secreto.",
        "O teu objetivo é resolver enigmas e escapar antes que seja tarde.",
        "Boa sorte!"
    ]
    index = 0

    label = tk.Label(root, text=texts[index], font=("Arial", 16), wraplength=400, pady=20)
    label.pack()

    def next_text():
        global index
        index += 1
        if index < len(texts):
            label.config(text=texts[index])
        else:
            # Quando acabar, chama a função para iniciar o jogo
            root.destroy()
            cenario_1()

    next_button = tk.Button(root, text="Próximo", command=next_text)
    next_button.pack(pady=10)
    root.mainloop()


#---------------------------------------------------------------------------------------------------------


def cenario_1():
    # Aqui coloco o código para iniciar a janela principal do jogo
    game_root = tk.Tk()
    game_root.title("Jogo Escape Room")
    canvas = tk.Canvas(game_root, width=600, height=400, bg="#e6f2ff")
    canvas.pack()

    # Chão
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
            canvas.delete("porta")
            # Espera 2 segundos antes de continuar
            game_root.after(2000, lambda: [game_root.destroy(), cenario2()])

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

    # Não é necessário destruir widgets aqui, pois é uma nova janela

    game_root.title("Sala da Chave")

    canvas = tk.Canvas(game_root, width=700, height=350, bg="#f0f0f0")
    canvas.pack()

    # Fundo: parede e chão
    canvas.create_rectangle(0, 0, 700, 100, fill="#b0b0b0")      # parede
    canvas.create_rectangle(0, 100, 700, 350, fill="#e0d7c6")    # chão

    # Mesa
    canvas.create_rectangle(150, 220, 550, 320, fill="#8b7d6b", outline="black")

    # Gaveta (fechada)
    gaveta_x1, gaveta_y1 = 320, 270
    gaveta_x2, gaveta_y2 = 380, 300
    puxador_x1, puxador_y1 = 340, 275
    puxador_x2, puxador_y2 = 360, 295

    gaveta = canvas.create_rectangle(gaveta_x1, gaveta_y1, gaveta_x2, gaveta_y2, fill="#c0c0c0", outline="black", width=2)
    puxador = canvas.create_rectangle(puxador_x1, puxador_y1, puxador_x2, puxador_y2, fill="black", outline="gray20", width=2)

    # Chave enferrujada
    chave_x, chave_y = 250, 230
    canvas.create_rectangle(chave_x, chave_y, chave_x + 70, chave_y + 15, fill="#a0522d", outline="black")
    canvas.create_oval(chave_x - 15, chave_y - 10, chave_x + 15, chave_y + 25, fill="#8b4513", outline="black")

    # Texto inicial
    label_texto = tk.Label(game_root, text=(
        "Após abrires a porta, encontras uma chave enferrujada sobre a mesa.\n"
        "Ela abre uma gaveta, mas está enferrujada e não funciona bem.\n"
        "Escolhe uma substância para tentar limpar a ferrugem."
    ), font=("Arial", 12))
    label_texto.pack(pady=5)

    resposta_label = tk.Label(game_root, text="", fg="blue", font=("Arial", 12))
    resposta_label.pack(pady=5)

    # Criação dos botões fora das funções
    frame_botoes = tk.Frame(game_root)
    frame_botoes.pack(pady=5)

    tk.Button(frame_botoes, text="Água", command=lambda: usar_substancia("água")).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Álcool", command=lambda: usar_substancia("álcool")).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Óleo", command=lambda: usar_substancia("óleo")).pack(side="left", padx=5)

    dica_button = tk.Button(game_root, text="Mostrar dica", command=lambda: mostrar_dica())
    dica_button.pack(pady=5)

    sair_button = tk.Button(game_root, text="Sair do jogo", command=lambda: fechar_com_creditos())
    # <-- não será mostrado agora, apenas após vitória

    # Funções principais
    def usar_substancia(substancia):
        if substancia == "óleo":
            resposta_label.config(text="Usaste óleo para limpar a ferrugem! A gaveta abre automaticamente.")
            abrir_gaveta()
        else:
            resposta_label.config(text=f"Usar {substancia} não remove a ferrugem. Tenta outra substância.")

    def mostrar_dica():
        dica = (
            "Dica:\n"
            "A ferrugem é causada pela oxidação do ferro.\n"
            "Para restaurar a mobilidade da chave enferrujada,\n"
            "procura uma substância oleosa que lubrifique e proteja o metal."
        )
        resposta_label.config(text=dica)

    def abrir_gaveta():
        canvas.delete(gaveta)
        canvas.delete(puxador)
        canvas.create_rectangle(gaveta_x1 + 200, gaveta_y1, gaveta_x2 + 200, gaveta_y2,
                                fill="#dcdcdc", outline="black", width=2)
        canvas.create_rectangle(puxador_x1 + 200, puxador_y1, puxador_x2 + 200, puxador_y2,
                                fill="black", outline="gray20", width=2)

        label_texto.config(text="Abriste a gaveta! Dentro dela, encontras o mapa para a saída.")
        resposta_label.config(text="Parabéns, acabaste o Escape Room Químico! 🎉")

        # Esconder outros botões
        frame_botoes.pack_forget()
        dica_button.pack_forget()

        # Mostrar botão de sair
        sair_button.pack(pady=10)

    def fechar_com_creditos():
        # Limpar tudo
        for widget in game_root.winfo_children():
            widget.destroy()

        # Tela final
        tk.Label(game_root, text="Escape Room Químico", font=("Arial", 20, "bold")).pack(pady=20)
        tk.Label(game_root, text="Obrigado por jogares!", font=("Arial", 14)).pack(pady=10)
        tk.Label(game_root, text="Criado com Python e Tkinter 🧪🔐", font=("Arial", 12), fg="gray").pack(pady=10)

        # Fechar após alguns segundos
        game_root.after(4000, game_root.destroy)

    game_root.mainloop()


#-------------------------------------------------------------------------------


if __name__ == "__main__":
    intro()
