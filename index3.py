gsport = int(input("Informe o número de gols do Sport:"))
gnautico = int(input("Informe o número de gols do Náutico:"))

if gsport == gnautico:
    print ("Empate")

elif gsport > gnautico:
    print ("Sport é o time vencedor")

elif gnautico > gsport:
    print ("Náutico é o time vencedor")

