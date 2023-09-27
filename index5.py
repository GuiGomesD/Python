n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))

cod = int(input("Digite o código da operação que deseja efetuar \n 1(Média) \n 2(Diferença) \n 3(Produto) \n 4(Divisão) \n Código:"))

if cod == 1:
    media = (n1 + n2) / 2
    print ("A média entre os número é de:", media)

elif cod == 2:
    dif = n1-n2
    print ("A diferença entre os números é de:", dif)

elif cod == 3:
    res = n1 * n2
    print ("O produto entre os números é de:", res)

elif cod == 4:
    div = n1 / n2
    print ("A divisão entre os números é de:", div)