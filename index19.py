adol = 0
idade = int(input("Informe a idade:"))

while idade > 0:
    if idade >= 12 and idade <= 17:
        adol = adol + 1
    idade = int(input("Informe a idade:"))
print ("Quantidade de adolescentes:", adol)