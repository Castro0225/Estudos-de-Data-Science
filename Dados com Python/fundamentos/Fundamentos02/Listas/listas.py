"""
Listas em python são construídas utilizando []
"""
# indices      [-0]            [1] [2] [3] [4]
# aprovacao = ["Victor Castro, 9.0, 6.0, 10.0, true"]
# print(f"{provacao}")
nomes=[]
for i in range(0,5):
    nome =str(input(f"Qual o {i+1}º nome?"))
    nomes.append(nome)
    print(f"{nomes}")