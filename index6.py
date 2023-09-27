sal_atual = float(input("Digite seu salário atual:"))

if sal_atual <= 300:
    reajuste = (sal_atual * 35) / 100
    sal_final = sal_atual + reajuste
    print("Seu salário final é de:", sal_final)

else:
    reajuste = (sal_atual * 15) / 100
    sal_final = sal_atual + reajuste
    print("Seu salário final é de:", sal_final)