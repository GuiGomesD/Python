n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
cod = int(input("Código:"))

if cod == 1 or cod == 2:
    if n1 > n2:
        print(n1, "é o maior número")
    elif n2 > n1:
        print(n2, "é o maior número")

elif cod == 3 or cod == 4:
    if n1 < n2:
        print(n1, "é o menor número")
    elif n2 < n1:
        print(n2, "é o menor número")

else:
    print ("Error. Código inválido")
