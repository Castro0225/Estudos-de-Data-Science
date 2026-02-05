# for "elemento" in "conjunto:"
#range(inicio,fim,passo)
"""
i = 1
ii = 11
# começa em 1, ate o 11
for i in range(i,ii):
    print(i)
"""
for i in range(0,3):
    nota_1=float(input("Qual a primeira nota?"))
    nota_2=float(input("Qual a segunda nota?"))
    nota_3=float(input("Qual a terceira nota?"))
    media = (nota_1+nota_2+nota_3)/3
    if media >=7:
        print(f"Parabens, voce está aprovado e sua media é de {media}")
    else:
        print(f"Voce foi reprovado e sua media foi de {media}")