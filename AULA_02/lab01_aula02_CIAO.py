# ============================================================
# ATIVIDADE 1 - Enumeracao completa do Problema da Mochila
# Objetivo: mostrar o espaco de busca e encontrar a solucao otima
# ============================================================
import itertools # biblioteca que gera todas as combinacoes possiveis
import time # para medir quanto tempo o computador demora

# ----------------------------------------------------------
# 1. DEFINICAO DO PROBLEMA (dados de entrada)
# ----------------------------------------------------------
nomes = ['Livro', 'Fone', 'Camiseta', 'Carregador', 'Chocolate']
pesos = [2, 1, 2, 1, 1] # peso de cada item (na mesma ordem)
valores = [3, 2, 2, 3, 1] # valor (beneficio) de cada item
capacidade = 5 # peso maximo que a mochila aguenta
n = len(pesos) # quantidade de itens (neste caso 5)

# ----------------------------------------------------------
# 2. ENUMERACAO DE TODAS AS POSSIBILIDADES
# ----------------------------------------------------------
# Cada item pode ser escolhido (1) ou nao (0).
# Com n itens existem 2**n possibilidades.
# itertools.product gera todas as tuplas possiveis de 0s e 1s.
melhor_valor = -1 # guarda o melhor valor encontrado ate agora
melhor_combinacao = None # guarda a combinacao que deu o melhor valor
total_avaliadas = 0 # contador de quantas solucoes olhamos
inicio = time.time() # marca o tempo de inicio
# Gera todas as combinacoes: (0,0,0,0,0), (0,0,0,0,1), ..., (1,1,1,1,1)
for combinacao in itertools.product([0, 1], repeat=n):
  total_avaliadas += 1 # mais uma solucao foi avaliada
  # Calcula o peso total e o valor total desta combinacao
  peso_total = 0
  valor_total = 0
  for i in range(n): # percorre cada item
    if combinacao[i] == 1: # se o item i foi escolhido
      peso_total += pesos[i]
      valor_total += valores[i]
  # So consideramos a solucao se ela respeitar a capacidade
  if peso_total <= capacidade:
    # Se esta solucao for melhor que a melhor ate agora, atualizamos
    if valor_total > melhor_valor:
      melhor_valor = valor_total
      melhor_combinacao = combinacao
fim = time.time() # marca o tempo de fim

# ----------------------------------------------------------
# 3. MOSTRANDO OS RESULTADOS
# ----------------------------------------------------------
print('Total de solucoes avaliadas:', total_avaliadas)
print('Tempo de execucao: {:.6f} segundos'.format(fim - inicio))
print('Melhor valor encontrado:', melhor_valor)
print('Combinacao otima (0=nao leva, 1=leva):', melhor_combinacao)
# Mostra quais itens foram escolhidos de forma legivel
print('\nItens escolhidos:')
for i in range(n):
  if melhor_combinacao[i] == 1:
    print(' -', nomes[i], '(peso:', pesos[i], ', valor:', valores[i], ')')


#PERGUNTAS:
# 1. Por que o total de solucoes avaliadas e exatamente 32?
# 2. O que aconteceria se eu colocasse 15 itens?
# 3.Voces conseguem imaginar um problema da vida real que seja parecido com este?
