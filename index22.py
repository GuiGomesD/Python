sim = 0
nao = 0
for cont in range (0, 15):
    res = int(input("Você gosta de beterraba? Digite 1 para SIM e 2 para NÃO:"))
    if res == 1:
        sim = sim + 1
    elif res == 2:
        nao = nao + 1

print ("Sim:", sim)
print ("Não:", nao)
   