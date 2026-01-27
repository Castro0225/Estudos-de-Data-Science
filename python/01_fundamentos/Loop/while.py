"""
# I é zero
i = -1

# Enquanto I for menor que 10, some 1
while i <= 10:
    i = i + 1
    print(f"{i}")
"""
i = 1
while i <=3:
    i = i + 1
    nota_1 = float(input("Qual a primeira nota?"))
    nota_2 = float(input("Qual a segunda nota?"))
    nota_3 = float(input("Qual a terceita nota?"))
    media = nota_1 + nota_2 + nota_3 / 3
    if media >=7:
        print(f"Parabens, voce foi Aprovado!! sua média foi de {media}")
    else:
        print(f"Voce foi reprovado! Sua média foi de {media}")