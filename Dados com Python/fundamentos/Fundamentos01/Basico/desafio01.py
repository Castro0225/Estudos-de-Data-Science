#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
"""
01 -
nome = str(input("Qual seu nome? "))
print(f"Olá {nome}")

#--------------
02 -
nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade ?"))

print(f"olá {nome}, voce tem {idade} anos. ")

"""
"""
nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade ?"))
altura = float(input("Qual sua altura em metros?"))

print(f"olá {nome}, voce tem {idade} anos e sua altura é {altura} metros.")"""

num1 = float(input("Digite um valor"))
num2 = float(input("Digite um valor"))

soma = num1 + num2

print(f"A soma deu {soma}")
