# Instrucoes:
# 12.	Copie o codigo completo abaixo para um arquivo .py ou para um notebook Jupyter.
# 13.	Execute o codigo. Ele ja resolve o TSP para 4, 5 e 6 cidades.
# 14.	Anote em uma tabela: numero de cidades, quantidade de rotas avaliadas, tempo de execucao e distancia da melhor rota.
# 15.	Responda as perguntas de reflexao no final.

# ============================================================
# ATIVIDADE 2 - Forca-bruta no Problema do Caixeiro Viajante (TSP)
# Objetivo: sentir a explosao combinatoria na pratica
# ============================================================
 
import itertools
import time
import numpy as np
 
# ----------------------------------------------------------
# Funcao que resolve o TSP por forca-bruta (olha todas as rotas)
# ----------------------------------------------------------
def tsp_forca_bruta(matriz_distancias):
    """Recebe uma matriz de distancias e devolve a melhor rota e seu custo."""
    n = len(matriz_distancias)          # numero de cidades
    cidades = list(range(1, n))         # cidades de 1 ate n-1 (cidade 0 e o ponto de partida)
 
    melhor_custo = float('inf')         # comeca com 'infinito'
    melhor_rota = None
    total_rotas = 0
 
    # Gera todas as permutacoes possiveis das cidades intermediarias
    # Exemplo com 4 cidades: as permutacoes de [1,2,3] sao 6 possibilidades
    for permutacao in itertools.permutations(cidades):
        total_rotas += 1
 
        # Monta a rota completa: comeca em 0, visita a permutacao e volta para 0
        rota = (0,) + permutacao + (0,)
 
        # Calcula o custo (distancia total) desta rota
        custo = 0
        for i in range(n):              # n trechos (incluindo a volta)
            cidade_atual = rota[i]
            proxima_cidade = rota[i + 1]
            custo += matriz_distancias[cidade_atual][proxima_cidade]
 
        # Se esta rota for a melhor ate agora, guardamos ela
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = rota
 
    return melhor_custo, melhor_rota, total_rotas
 
# ----------------------------------------------------------
# Matrizes de distancia para 4, 5 e 6 cidades (exemplos pequenos)
# ----------------------------------------------------------
dist_4 = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])
 
dist_5 = np.array([
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 15],
    [10, 3, 0, 4, 11],
    [19, 7, 4, 0, 14],
    [8, 15, 11, 14, 0]
])
 
dist_6 = np.array([
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 17, 28],
    [15, 35, 0, 30, 22, 16],
    [20, 25, 30, 0, 14, 19],
    [25, 17, 22, 14, 0, 11],
    [30, 28, 16, 19, 11, 0]
])
 
# ----------------------------------------------------------
# Executando para 4, 5 e 6 cidades e coletando resultados
# ----------------------------------------------------------
matrizes = [dist_4, dist_5, dist_6]
nomes_cenarios = ['4 cidades', '5 cidades', '6 cidades']
 
print('=' * 65)
print('RESULTADOS DA FORCA-BRUTA NO TSP')
print('=' * 65)
 
for nome, matriz in zip(nomes_cenarios, matrizes):
    inicio = time.time()
    custo, rota, total = tsp_forca_bruta(matriz)
    tempo = time.time() - inicio
 
    print(f'\n>>> {nome}')
    print(f'    Rotas avaliadas : {total}')
    print(f'    Melhor custo    : {custo}')
    print(f'    Melhor rota     : {rota}')
    print(f'    Tempo (segundos): {tempo:.6f}')
 
print('\n' + '=' * 65)
print('OBSERVE: o numero de rotas cresce como (n-1)!  (fatorial)')
print('4 cidades -> 6 rotas | 5 -> 24 | 6 -> 120 | 10 -> 362880 | 15 -> 87 bilhoes')
print('=' * 65)

# REFLEXÃO FINAL
# Tabela que as duplas/trio devem preencher
# Numero de cidades | Rotas avaliadas | Tempo (s) | Melhor custo
# 4                 |                 |           |
# 5                 |                 |           |
# 6                 |                 |           |

# Perguntas de reflexao (obrigatorias)
# 16.	O numero de rotas cresce de forma linear, quadratica ou muito mais rapido? Explique com as quantidades que voce coletou.
# 17.	Com base no padrao observado, estime (mesmo que de forma grosseira) quanto tempo levaria para 10 cidades no mesmo computador.
# 18.	Por que dizemos que o TSP e um problema “dificil”? A resposta nao e “porque e complicado de entender”, e sim por causa do crescimento do tempo.
 




