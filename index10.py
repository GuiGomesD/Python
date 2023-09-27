sal = float(input("Informe o seu salário atual:"))

if sal < 300:
    reajuste = sal * 45 / 100
    final = sal + reajuste
    print ("O seu salário final é de:", final)

elif sal <= 600:
    reajuste = sal * 25 / 100
    final = sal + reajuste
    print ("O seu salário final é de:", final)

elif sal > 600:
    reajuste = sal * 15 / 100
    final = sal + reajuste
    print ("O seu salário final é de:", final)