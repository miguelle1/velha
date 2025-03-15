#"w" - write (file1.write) = poder escrever noutro ficheiro
#"r" - read (file1.read) = poder ler na interface abaixo
#"a" - append (file1.write(\n)) = poder adicionar frases
#"encoding="utf-8" = reconhecer todos os tipos de texto (acentos símbolos, etc.)

with open("ficheiro.txt", "w", encoding="utf-8") as file1:
    file1.write("Olá SharkCoders!\nTudo Bem?")