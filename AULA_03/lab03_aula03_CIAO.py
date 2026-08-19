#ATIVIDADE 3: Complete o Algoritmo Genético
#Problema: Encontrar x ∈ [0, 10] que maximiza f(x) = x * sin(3x)

import numpy as np
import matplotlib.pyplot as plt
import random

# ==================== CONFIGURAÇÕES ====================
BITS = 8              # 8 bits → valores de 0 a 255
POP_SIZE = 20
GERACOES = 50
TAXA_CROSS = 0.8
TAXA_MUT = 0.05

# Intervalo de x
X_MIN = 0
X_MAX = 10

# ==================== FUNÇÃO OBJETIVO ====================
def funcao_objetivo(x):
    """f(x) = x * sin(3*x)"""
    return x * np.sin(3 * x)

# ==================== FUNÇÕES A COMPLETAR ====================

# TODO 1: Converter bits para x real
def bits_para_x(bits):
    """
    Converte lista de 8 bits para valor real no intervalo [X_MIN, X_MAX].
    Dica: primeiro converta para decimal, depois normalize.
    """
    # SEU CÓDIGO AQUI
    pass

# TODO 2: Calcular fitness (nota) de um indivíduo
def fitness(individuo):
    """
    Calcula o fitness de um indivíduo.
    Lembre-se: Queremos MAXIMIZAR f(x).
    """
    # SEU CÓDIGO AQUI
    pass

# TODO 3: Mutação bit-flip
def mutacao(individuo):
    """
    Aplica mutação bit-flip.
    Cada bit tem TAXA_MUT de chance de ser invertido.
    """
    # SEU CÓDIGO AQUI
    pass

# ==================== CÓDIGO PRONTO (NÃO MEXER) ====================

def criar_individuo():
    return [random.randint(0, 1) for _ in range(BITS)]

def criar_populacao():
    return [criar_individuo() for _ in range(POP_SIZE)]

def selecao_roleta(pop, fitnesses):
    total = sum(fitnesses)
    if total == 0:
        return random.choice(pop)
    pick = random.uniform(0, total)
    acumulado = 0
    for i, ind in enumerate(pop):
        acumulado += fitnesses[i]
        if acumulado > pick:
            return ind.copy()
    return pop[-1].copy()

def crossover(pai1, pai2):
    if random.random() > TAXA_CROSS:
        return pai1.copy(), pai2.copy()
    ponto = random.randint(1, BITS - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def executar_ag():
    pop = criar_populacao()
    historico = []
    
    for gen in range(GERACOES):
        # Avaliar
        fitnesses = [fitness(ind) for ind in pop]
        
        melhor_fit = max(fitnesses)
        melhor_ind = pop[fitnesses.index(melhor_fit)]
        melhor_x = bits_para_x(melhor_ind)
        historico.append((melhor_x, melhor_fit))
        
        if gen % 10 == 0:
            print(f"Geração {gen:3d}: Melhor f(x) = {melhor_fit:.4f} (x = {melhor_x:.4f})")
        
        # Elitismo
        sorted_idx = np.argsort(fitnesses)[::-1]
        nova_pop = [pop[i].copy() for i in sorted_idx[:2]]
        
        # Criar filhos
        while len(nova_pop) < POP_SIZE:
            pai1 = selecao_roleta(pop, fitnesses)
            pai2 = selecao_roleta(pop, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            nova_pop.append(mutacao(filho1))
            if len(nova_pop) < POP_SIZE:
                nova_pop.append(mutacao(filho2))
        
        pop = nova_pop
    
    return historico

# ==================== EXECUTAR ====================
print("=" * 50)
print("OTIMIZANDO f(x) = x * sin(3x)")
print("=" * 50)

historico = executar_ag()

# Visualizar
x_plot = np.linspace(X_MIN, X_MAX, 1000)
y_plot = funcao_objetivo(x_plot)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x)')
melhor_x, melhor_fit = max(historico, key=lambda x: x[1])
plt.scatter(melhor_x, melhor_fit, color='red', s=100, zorder=5, label=f'Melhor: x={melhor_x:.3f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Função e Melhor Solução')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
x_hist = [h[0] for h in historico]
y_hist = [h[1] for h in historico]
plt.plot(range(GERACOES), y_hist, 'r-o', linewidth=2, markersize=4)
plt.xlabel('Geração')
plt.ylabel('Melhor f(x)')
plt.title('Convergência do AG')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\n MELHOR SOLUÇÃO: x = {melhor_x:.4f}, f(x) = {melhor_fit:.4f}")
