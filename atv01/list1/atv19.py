repita = True

while repita == True:
    razao = input("Insira um número com 3 digitos: ")

    soma = int(razao) + int(razao[2] + razao [1] + razao [0])
    soma = str(soma)

    somap = int(soma [0])*1
    somap = somap + (int(soma[1])*2)
    somap = somap + (int(soma[2])*3)

    somap =  str (somap)
    print("O digito é: ", somap[1])

    op2 = int (input("Deseja repetir?\n1 - sim\n2 - não" ))
    if op2 == 1:
        repita = True
    else:
        repita = False
