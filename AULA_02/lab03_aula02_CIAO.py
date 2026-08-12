# Atividade 3 — SEMI-PRONTA: Heuristica Gulosa + Calculo do Gap de Otimalidade
# Objetivo da atividade: Entender na pratica o que e uma heuristica construtiva simples e como medir o quanto ela fica longe do otimo.

# O que ja esta pronto:
# •	Geracao de instancias aleatorias do Problema da Mochila
# •	Solver de forca-bruta (otimo) para instancias pequenas (n <= 18)
# •	Heuristica gulosa (escolhe primeiro os itens de maior valor/peso)

# O que vocês precisam completar
# •	A funcao que calcula o gap percentual
# •	O loop que roda varias instancias e coleta estatisticas

# ============================================================
# Heuristica Gulosa + Gap de Otimalidade
# Complete as partes marcadas com COMPLETE
# ============================================================
 
import numpy as np
import itertools
import time
 
# ----------------------------------------------------------
# 1. Funcao que resolve a mochila por forca-bruta (otima)
# ----------------------------------------------------------
def mochila_otima(pesos, valores, capacidade):
    n = len(pesos)
    melhor = 0
    for comb in itertools.product([0, 1], repeat=n):
        peso = sum(pesos[i] for i in range(n) if comb[i] == 1)
        if peso <= capacidade:
            valor = sum(valores[i] for i in range(n) if comb[i] == 1)
            if valor > melhor:
                melhor = valor
    return melhor
 
# ----------------------------------------------------------
# 2. Heuristica Gulosa (ja pronta)
# Ideia: ordena os itens pelo valor / peso (densidade)
# e vai colocando enquanto couber.
# ----------------------------------------------------------
def mochila_gulosa(pesos, valores, capacidade):
    n = len(pesos)
    # Calcula a densidade (valor por unidade de peso) de cada item
    densidade = [(valores[i] / pesos[i], i) for i in range(n)]
    # Ordena do maior densidade para o menor
    densidade.sort(reverse=True)
 
    valor_total = 0
    peso_atual = 0
    for dens, i in densidade:
        if peso_atual + pesos[i] <= capacidade:
            peso_atual += pesos[i]
            valor_total += valores[i]
    return valor_total
 
# ----------------------------------------------------------
# 3. COMPLETE ESTA FUNCAO
# ----------------------------------------------------------
def calcular_gap(valor_heuristica, valor_otimo):
    """
    Deve retornar o gap percentual:
    gap = ((valor_otimo - valor_heuristica) / valor_otimo) * 100
    Se o valor otimo for zero, retorne 0 para evitar divisao por zero.
    """
    # COMPLETE AQUI (apague o pass e escreva o codigo)
    pass
 
# ----------------------------------------------------------
# 4. Experimento: varias instancias aleatorias
# ----------------------------------------------------------
np.random.seed(42)                    # para os resultados serem reproduziveis
n_itens = 12                           # tamanho das instancias (pode testar 10 a 16)
capacidade = 30
n_instancias = 20                      # quantas instancias diferentes vamos testar
 
gaps = []                              # lista que vai guardar o gap de cada instancia
 
print('Rodando', n_instancias, 'instancias...')
for k in range(n_instancias):
    # Gera pesos e valores aleatorios
    pesos = np.random.randint(1, 15, size=n_itens)
    valores = np.random.randint(10, 50, size=n_itens)
 
    # Calcula a solucao otima (pode demorar um pouco)
    otimo = mochila_otima(pesos, valores, capacidade)
 
    # Calcula a solucao da heuristica gulosa
    heur = mochila_gulosa(pesos, valores, capacidade)
 
    # COMPLETE: calcule o gap usando a funcao que voce implementou
    # e adicione na lista gaps
    # gap = calcular_gap(heur, otimo)
    # gaps.append(gap)
 
    print(f'Instancia {k+1:2d} | Otimo: {otimo:4d} | Gulosa: {heur:4d} | Gap: {gap:5.1f}%')
 
# ----------------------------------------------------------
# 5. Estatisticas finais
# ----------------------------------------------------------
print('\n===== RESUMO =====')
print(f'Gap medio     : {np.mean(gaps):.2f}%')
print(f'Gap minimo    : {np.min(gaps):.2f}%')
print(f'Gap maximo    : {np.max(gaps):.2f}%')
print(f'Desvio padrao : {np.std(gaps):.2f}%')


# O que entregar / discutir:
# 19.	Codigo completo (com a funcao calcular_gap implementada e o loop funcionando).
# 20.	Valor do gap medio obtido.
# 21.	Resposta: “A heuristica gulosa e boa o suficiente para este problema? Em quais situacoes voce usaria ela e em quais preferiria gastar mais tempo para achar o otimo?”

