distancia = int(input("Informe a distancia percorrida:"))
tempo = int(input("Informe o tempo total levado:"))
vm = distancia / tempo
print("Velocidade média = ",vm)

conf = str(input("Continuar? (sim ou nao)"))

while conf == "sim":
    distancia = int(input("Informe a distancia percorrida:"))
    tempo = int(input("Informe o tempo total levado:"))
    vm = distancia / tempo
    print("Velocidade média = ",vm)

    conf = str(input("Continuar? (sim ou nao)"))
