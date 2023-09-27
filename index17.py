

cod = int(input("Digite o código do produto:"))

while cod != 0:

    if cod == 1:
        print("Caderno-R$12.00")
        valor = 12.00
    elif cod == 2:
        print("Régua-R$2.50")
        valor = 2.50
    elif cod == 3:
        print("Borracha-R$0.25")
        valor = 0.25
    elif cod == 4:
        print("Mochila-R$50.00")
        valor = 50.00
    quant = int(input("Informe a quantidade:"))
    total = valor * quant
    print ("O total a ser pago é = R$",total)

    cod = int(input("Digite o código do produto:"))
