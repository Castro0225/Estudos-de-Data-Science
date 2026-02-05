# indice = chave and chave = valor
# ao inves de colocar o indice para alteração, coloco a chave do valor
'''dicionario = {'chave_01':1,
              'chave_02':2}
print(dicionario)'''
print()
print('Aqui temos os dados base da matricula. ')
cadastro = {'matricula':2000168933,
           'dia_cadastro':25,
           'mes_cadastro':10,
           'turma':'2E'}
print(cadastro)
#para realizar uma busca pela chave, vamos fazer dessa forma:
print()
print('Agora vamos filtrar pela matricula')
print(cadastro['matricula'])
print()
# para atualizar um valor vamos fazer assim:
print("Vamos atualizar a turma")
cadastro['turma'] = '2G'
print(cadastro)
#cadastrar uma nova chave
print()
print('Agora vamos criar uma nova chave.')
cadastro['modalidade'] = 'EAD'
print(cadastro)
print()
print()