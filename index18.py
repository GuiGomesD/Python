maior = 0
num = int(input("Digite um número:"))

while num > 0 and num != 0:
    if num > maior:
        maior = num
        print(num, "foi o maior número digitado até o momento")
    num = int(input("Digite um número:"))
