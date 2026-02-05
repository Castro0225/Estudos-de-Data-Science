# idenficar a quantidade de elementos de uma lista = len()
#indices           0            1      2      3       4
print()
print('No começo do codigo, temos a seguinte lista:')
aprovacao = ['Victor Castro', '9.0', '9.5', '10.0', 'true']
print(aprovacao)
#print(f"{len(aprovacao)}")
media = (float(aprovacao[1]) + float(aprovacao[2]) + (float(aprovacao[3])))/3
#print(f"{aprovacao[1:4]}")
#print(f"{aprovacao[3:]}") - pega do indice 3 ate o final
#se é metodo tem que ter ()
#append() - é um metodo que adiciona um elemento ao final da lista
print()
aprovacao.append(media)
print('Aqui estamos utilizando o metodo append. Ele adiciona ao final da lista uma nova informação, no caso a média das notas.')
print(aprovacao)
print()
#extend - adiciona varios elementos de uma vez no final da lista
print('Aqui agora vamos utilizar o metodo extend. Ele reaproveitará o append e adicionará as "notas" de 3 materias.')
aprovacao.extend([9.0,6.5,10.0])
print(aprovacao)
print()
#remove - com esse metodo conseguimos retirar um elemento de uma lista. se tiver repetição ele retirará o primeiro. recomendavel utilizar da seguinte forma.
print("Agora vamos remover o meu nome da lista com o remove")
#aprovacao.remove([9.0,6.5,10.0])
aprovacao.pop(0)
print(aprovacao)
