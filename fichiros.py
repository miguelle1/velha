with open("ficheiro.txtt", "w", encoding="utf-8") as file2:
   file2.write("Olá\nadeus")

def escrever():
   with open("ficheiro.txtt", "r", encoding="utf-8") as file2:
      print(file2.read())

escrever()

def contar():
   with open("ficheiro.txtt", "r", encoding="utf-8") as file2:
      soma = 0
      conteudo = file2.readlines()
      for i in conteudo:
         soma += 1
      print(soma)

contar()