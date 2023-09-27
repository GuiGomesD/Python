idade = int(input("Informe a idade:"))

f1 = 0
f2 = 0
while idade > 0:
    if idade <= 15:
        f1 = f1 + 1
        print ("1 Faixa etária = ",f1)
        print("2 Faixa etária = ",f2)
    elif idade > 15:
        f2 = f2 + 1
        print ("1 Faixa etária = ",f1)
        print("2 Faixa etária = ",f2)
    elif idade <= 15:
        f1 = f1 + 1
        print ("1 Faixa etária = ",f1)
        print("2 Faixa etária = ",f2)
    elif idade > 15:
        f2 = f2 + 1
        print ("1 Faixa etária = ",f1)
        print("2 Faixa etária = ",f2)

    idade = int(input("Informe a idade:"))