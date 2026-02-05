
nota1 = float(input("Qual a primeira nota: "))
nota2 = float(input("Qual a segunda nota: "))
nota3 = float(input("Qual a terceira nota: "))

somaNota = nota1 + nota2 + nota3

media = somaNota / 3
"""
if media >= 7:
    print("Aprovado")
else:
    print("reprovado")
"""
#uso do Elif 

if media >=7:
    print("Aprovado! ")
elif media >=5:
    print("recuperação")
else :
    print("reprovado")