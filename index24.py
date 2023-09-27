regular = 0
bom = 0
otimo = 0
for cont in range (0, 5):

    opiniao = int(input("Qual sua opinião em relação ao filme? \n regular-1 \n bom-2 \n ótimo-3 \n:"))
    if opiniao == 1:
        regular = regular + 1

    elif opiniao == 2:
        bom = bom + 1

    elif opiniao == 3:
        otimo = otimo + 1

print(regular,"pessoas acharam o filme regular")
print(bom,"pessoas acharam o filme bom")
print(otimo,"pessoas acharam o filme otimo")