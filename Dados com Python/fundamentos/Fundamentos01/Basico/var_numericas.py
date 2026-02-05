q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

salario_seguranca = q_seguranca * s_seguranca
salario_docente = q_docente * s_docente
salario_diretoria = q_diretoria * s_diretoria
salario_total = salario_seguranca + salario_docente + salario_diretoria


total_empregados = q_seguranca+q_docente+q_diretoria
dif_sal = 12500 - 3000
media_salario = salario_total / total_empregados

#print(f"O total de empregados é {total_empregados}, a diferença salarial é {dif_sal} e a media salaria dos empregados é {media_salario}")

# utilizar // = divisão inteira
# utilizar ** = potencia
# utilizar % = modulo - resto

#print(type(s1), type(s2)) visualiza o tipo de variavel