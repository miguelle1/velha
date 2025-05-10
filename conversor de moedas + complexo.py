import requests

lista = ["EUR", "USD", "BRL"]

print("-="*10)
print("Conversor de Moedas")
print("-=" * 10)



print("Qual a moeda de origem?\n0 - Euro\n1 - Dólar Americano\n2 - Real Brasileiro")
moeda_origem = input("Escolha a opção:")

if moeda_origem == "0":
    de = "EUR"
elif moeda_origem == "1":
    de = "USD"
elif moeda_origem == "2":
    de = "BRL"



valor_desejado = int(input("Qual valor deseja converter?"))



print("Para qual moeda deseja converter?\n0 - Euro\n1 - Dólar Americano\n2 - Real Brasileiro")
moeda_conversao = input("Escolha a opção:")

if moeda_conversao == "0":
    para = "EUR"
elif moeda_conversao == "1":
    para = "USD"
elif moeda_conversao == "2":
    para = "BRL"


cotacao = requests.get("https://economia.awesomeapi.com.br/last/{}".format(de+"-"+para))
cotacao = cotacao.json()
cotacao_moeda = float(cotacao["{}".format(de+para)]["bid"])

r = round(valor_desejado * cotacao_moeda,2)
print("O valor convertido é de",r,para)