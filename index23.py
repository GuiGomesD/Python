caro = 0
for produto in range (0, 10):
    preco = float(input("Informe o preço do produto:"))
    if preco > caro:
        caro = preco
print("Produto mais caro:R$",caro)