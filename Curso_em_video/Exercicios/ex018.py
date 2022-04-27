import math
angulo = float(input("Digite o ângulo que você deseja: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {sen :.2f}\nO ângulo de {angulo} tem o COSSENO de {cos :.2f}\nO ângulo de {angulo} tem o TANGENTE de {tan :.2f}")