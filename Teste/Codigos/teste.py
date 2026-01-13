import pandas as pd
import time

avaliacoes = pd.read_csv ("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv")

print(avaliacoes.head(31))
print()
print(f"Os nomes das colunas são: {avaliacoes.columns}")

avaliacoes.colums= ["usuarioId","filmeId","nota","momento"]

time.sleep(10)

