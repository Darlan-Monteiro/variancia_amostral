import pandas as pd
import numpy as np
import statistics
import math
from IPython.display import display

# Uma série de TV teve 10 episódios com as seguintes durações, em minutos: 35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
# Qual foi a duração média de cada episódio?

lista_minutos_ep = np.array([35, 34, 26, 32, 37, 28, 27, 33, 36, 32]) # lista com o tempo dos eps
qtde_itens_lista = len(lista_minutos_ep) # len para ler a qtd de item na lista

total_minutos_assistidos = np.sum(lista_minutos_ep) # sum para somar todos os itens da lista

media_minutos_ep = np.mean(lista_minutos_ep) # mean para descobrir a média dos itens da lista

lista_minutos_ep.sort() # sort para ordenar a lista do menor ao maior
moda_minutos_ep = statistics.mode(lista_minutos_ep) # mode para descobrir a moda da lista

tabela = pd.DataFrame(lista_minutos_ep, columns=['Xi']) # estou criando uma tabela. criei uma coluna "xi" e coloquei os valores da lista em cada linha

tabela['Xi - X'] = lista_minutos_ep - media_minutos_ep # criei outra coluna para calcular o valor de xi - a média
tabela['(Xi - X)^2'] = (lista_minutos_ep - media_minutos_ep)**2 # outra coluna, agora é para deixar 'Xi - X' ao quadrado

diferenca_quadrado = (lista_minutos_ep - media_minutos_ep)**2 # atribui a fórmula a uma variável

total_quadrado = diferenca_quadrado.sum() # sum para somar todos os valores ao quadrado

variancia_amostral = total_quadrado/(qtde_itens_lista - 1) # aqui é a fórmula estátistica da variância amostral. OBS: Em caso de dúvidas, procurar exemplo no google.

raiz_quadrada = math.sqrt(variancia_amostral) # math.sqrt para descobrir a raiz quadrada da variança


print(f'A mediana de minutos assistidos: {np.median(lista_minutos_ep)}')
print(f'O total de minutos assistidos: {total_minutos_assistidos}')
print(f'A média de minutos assistidos: {media_minutos_ep}')
print(f'A moda de minutos assistidos: {moda_minutos_ep}\n')

print(tabela.to_string(index=False))

print(f'\nValor total da coluna "(Xi - X)^2": {total_quadrado}')
print(f'Valor da Variância Amostral: {variancia_amostral:.2f}')
print(f'Valor da Raiz Quadrada: {raiz_quadrada:.2f}')