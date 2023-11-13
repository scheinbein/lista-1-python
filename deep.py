resposta = input("Qual a Grande Questão da Vida, do Universo e Tudo o Mais? ").casefold()

if resposta != "42" and resposta!= "forty two" and resposta != "forty-two":
    print('No')
else:
    print("Yes")

