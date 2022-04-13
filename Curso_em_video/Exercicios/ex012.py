price = float(input("Qual é o preço do produto? R$"))
desconto = price * 0.05
print(f"O produto que custava R${price}, na promoção com desconto de 5% vai custar R${price - desconto:.2f}")