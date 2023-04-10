quantidade = int(input("Quantidade: "))
valor = int(input("Valor: "))

valorMes = (quantidade / 3) * valor
valorAno = valorMes * 12

valorAtraso = (((quantidade / 3) / 10) * valor) * 0.1

fitas = round(quantidade + (quantidade / 10), 0)
fitas = round(fitas - (fitas * 0.02), 0)

print ("Faturamento anual", valorAno )
print ("Valor multas mensais", valorAtraso)
print ("Fitas ao longo de um ano", fitas)

