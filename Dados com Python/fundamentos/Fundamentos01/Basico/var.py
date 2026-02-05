#int = numeros inteiros. 5
#float = numeros com pontos flutuantes. 3,14
#str = armazena como forma de texto. Sempre entre "" aspas.
#Bool = armazena valores logicos. True and False
 
nome_aluno = str (input("Qual seu nome? "))
idade_aluno = int(input("Qual sua idade? "))
nota1 = float (input("Qual a nota da C1 ?"))
nota2 = float (input("Qual a nota da C2 ?"))
nota3 = float (input("Qual a nota da C3 ?"))

nota_total = nota1 + nota2 + nota3 
media_nota = nota_total/3

#str.upper() - str em maiusculo
#str.lower() - str em minusculo
#str.strip() - remove os espaços
#str.replace() - substitui uma letra do str - sanyos para santos (apenas visualização)
#Utilizar """ """ para utilizar docstring

print(f"olá {nome_aluno}, você tem {idade_aluno} anos, e sue media anual foi de {media_nota} ")

