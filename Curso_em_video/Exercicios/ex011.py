l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))
# A cada 2 metros quadrados de parede precisa de 1 litro de tinta
print(f"Sua parede tem a dimensão de {l}x{h} e sua área é de {l * h}m²\nPara pintar essa parede, você precisará de {(l * h) / 2}l de tinta")