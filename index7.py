preco = float(input("Digite o preço do produto:"))

if preco <= 50:
    reajuste = preco * 5 / 100
    newpreco = preco + reajuste
    print("O novo preço é de:", newpreco)
    print("Barato")

elif preco > 50 and preco < 100:
    reajuste = preco * 10 / 100
    newpreco = preco + reajuste
    print("O novo preço é de:", newpreco)
    if newpreco < 80:
        print ("Barato")
    elif newpreco > 80:
        print("Normal")
    elif newpreco > 120:
        print("Caro")
    elif newpreco > 200:
        print("Muito caro")

elif preco > 100:
    reajuste = preco * 15 / 100
    newpreco = preco + reajuste
    print("O novo preço é de:", newpreco)
    if newpreco < 80:
        print("Normal")
    elif newpreco > 120:
        print("Caro")
    elif newpreco > 200:
        print("Muito caro")