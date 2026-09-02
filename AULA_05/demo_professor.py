import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# 1. PARÂMETROS DO PSO
# ==========================================
N_PARTICULAS = 50
N_ITERACOES = 100

# O segredo do PSO está no equilíbrio destas três forças:
W = 0.5   # Inércia: Peso da velocidade atual (tendência de manter o curso)
C1 = 1.5  # Fator Cognitivo (Teimosia): Peso da melhor memória PESSOAL da partícula (neste caso o passário)
C2 = 1.5  # Fator Social (Efeito Manada): Peso da melhor memória do BANDO

# ==========================================
# 2. "CAMPO DE BUSCA"
# ==========================================
# Função objetivo: queremos encontrar o ponto mais baixo (mínimo)
def funcao_objetivo(x, y):
    # Função com um mínimo global perto de (0,0) e algumas "ondulações" (mínimos locais)
    return x**2 + y**2 + 5 * np.sin(x) * np.sin(y)

# Limites do mapa
X_MIN, X_MAX = -5, 5
Y_MIN, Y_MAX = -5, 5

# ==========================================
# 3. INICIALIZAÇÃO DO ENXAME
# ==========================================
# Posições e velocidades aleatórias iniciais
posicoes = np.random.uniform(X_MIN, X_MAX, (N_PARTICULAS, 2))
velocidades = np.random.uniform(-1, 1, (N_PARTICULAS, 2))

# Memória pessoal (pBest)
pbest_posicoes = np.copy(posicoes)
pbest_valores = np.array([funcao_objetivo(p[0], p[1]) for p in posicoes])

# Memória do bando (gBest)
melhor_idx = np.argmin(pbest_valores)
gbest_posicao = pbest_posicoes[melhor_idx]
gbest_valor = pbest_valores[melhor_idx]

# ==========================================
# 4. CONFIGURAÇÃO DA ANIMAÇÃO
# ==========================================
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Otimização por Enxame de Partículas (PSO)")
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)

# Desenhando o mapa de contorno (as curvas de nível do "vale")
x_grid = np.linspace(X_MIN, X_MAX, 100)
y_grid = np.linspace(Y_MIN, Y_MAX, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = funcao_objetivo(X, Y)
contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)
plt.colorbar(contour, ax=ax, label='Valor da Função (Menor é Melhor)')

# Elementos gráficos que serão atualizados
scatter = ax.scatter(posicoes[:, 0], posicoes[:, 1], color='red', marker='o', edgecolors='white', s=50, label='Partículas')
gbest_marker, = ax.plot(gbest_posicao[0], gbest_posicao[1], marker='*', color='yellow', markersize=15, linestyle='None', label='Melhor do Bando')
ax.legend()

# ==========================================
# 5. O MOTOR DO ALGORITMO (ATUALIZAÇÃO)
# ==========================================
def atualizar(frame):
    global posicoes, velocidades, pbest_posicoes, pbest_valores, gbest_posicao, gbest_valor
    
    for i in range(N_PARTICULAS):
        # 1. Atualizar Velocidade (A fórmula mágica do PSO)
        r1, r2 = np.random.rand(), np.random.rand() # Fator de aleatoriedade
        
        termo_inercia = W * velocidades[i]
        termo_cognitivo = C1 * r1 * (pbest_posicoes[i] - posicoes[i])
        termo_social = C2 * r2 * (gbest_posicao - posicoes[i])
        
        velocidades[i] = termo_inercia + termo_cognitivo + termo_social
        
        # 2. Atualizar Posição
        posicoes[i] = posicoes[i] + velocidades[i]
        
        # Manter as partículas dentro dos limites do mapa
        posicoes[i] = np.clip(posicoes[i], X_MIN, X_MAX)
        
        # 3. Avaliar nova posição
        valor_atual = funcao_objetivo(posicoes[i][0], posicoes[i][1])
        
        # Atualizar memória pessoal (pBest)
        if valor_atual < pbest_valores[i]:
            pbest_valores[i] = valor_atual
            pbest_posicoes[i] = posicoes[i]
            
            # Atualizar memória do bando (gBest)
            if valor_atual < gbest_valor:
                gbest_valor = valor_atual
                gbest_posicao = posicoes[i]
                
    # Atualizar o gráfico
    scatter.set_offsets(posicoes)
    gbest_marker.set_data([gbest_posicao[0]], [gbest_posicao[1]])
    ax.set_title(f"PSO - Iteração: {frame+1}/{N_ITERACOES} | Melhor Valor: {gbest_valor:.4f}")
    
    return scatter, gbest_marker

# Criar a animação
anim = FuncAnimation(fig, atualizar, frames=N_ITERACOES, interval=150, blit=False, repeat=False)

plt.show()
