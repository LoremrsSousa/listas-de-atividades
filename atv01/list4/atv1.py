num = int(input("Digite um número: "))
menor = num
maior = num
while num >= 0:
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    num = int(input("Digite um segundo número: "))
print(f"menor: {menor} maior: {maior}")