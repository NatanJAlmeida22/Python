dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
dias_pagar = dias * 60
km_pagar = km * 0.15
print(f"O total a pagar é de R${dias_pagar + km_pagar :.2f}")