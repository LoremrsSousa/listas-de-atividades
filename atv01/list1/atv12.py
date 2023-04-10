repita = True

while repita == True:
 razao = int(input("informe a razão: "))
 primeiro = int(input("valor do primeiro termo da sequência: "))
 
 decimotermo = (primeiro) + (razao*9)
 print (decimotermo, "o valor do décimo termo é: \n")
 op2 = int(input("Deseja repetir? \n1 - SIM \n2 - NÃO" ))


if op2 == 1:
  repita = True
else:
  repita = False