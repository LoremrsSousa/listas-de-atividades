repita = True

while repita == True:
    salario = int(input("Informe o valor do seu sálario: "))
    quilowatts = int(input("Informe a quantia de quilowatts gastos em sua residência: "))

    razao = (salario/quilowatts)
    umwatts = (salario/700)

    valordacontainicial = (umwatts*quilowatts)
    valorcomdesconto = (valordacontainicial*0.90)

    print (umwatts, "este é o valor de cada quilowatts gasto por esta residência:  \n")
    print(valordacontainicial, " este é o valor em reais a ser pago: \n")
    print(valorcomdesconto,  "este é o valor a ser pago com 10 porcento de desconto:  \n")

    op2 = int(input("Deseja repetir? \n1 - Sim\n2 - Não "))

    if op2 ==1:
        repita = True
    else:
        repita = False