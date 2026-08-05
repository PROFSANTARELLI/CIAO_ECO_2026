# ============================================================================
# DEMONSTRAÇÃO: Função Rastrigin e Busca Aleatória
# ============================================================================
#
# OBJETIVO: Demonstrar o conceito de Espaço de Busca e a limitação da
# Busca Aleatória (Monte Carlo) para encontrar o mínimo global de uma
# função com múltiplos mínimos locais.
#
# FUNÇÃO: Rastrigin 2D - benchmark clássico em otimização
#   f(x,y) = 20 + (x² - 10·cos(2π·x)) + (y² - 10·cos(2π·y))
#
# MÍNIMO GLOBAL: (x=0, y=0) com f(0,0) = 0
# ============================================================================

# Importação das bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import time

# ============================================================================
# 1. DEFINIÇÃO DA FUNÇÃO RASTRIGIN
# ============================================================================

def rastrigin_2d(x, y):
    """
    Função Rastrigin em 2 dimensões.
    
    A função é composta por uma constante 20 somada a termos quadráticos
    com cossenos para cada dimensão, criando múltiplos mínimos locais.
    
    Parâmetros:
    -----------
    x, y : float ou numpy.array
        Coordenadas a serem avaliadas
    
    Retorna:
    --------
    float ou numpy.array
        Valor da função em (x, y)
    
    Exemplo:
    --------
    >>> rastrigin_2d(0, 0)
    0.0
    >>> rastrigin_2d(1, 1)
    20 + (1 - 10·cos(2π)) + (1 - 10·cos(2π)) = 20 + (1-10) + (1-10) = 2.0
    """
    # Termo para dimensão x: x² - 10·cos(2π·x)
    termo_x = x**2 - 10 * np.cos(2 * np.pi * x)
    
    # Termo para dimensão y: y² - 10·cos(2π·y)
    termo_y = y**2 - 10 * np.cos(2 * np.pi * y)
    
    # Constante 20 + soma dos termos
    return 20 + termo_x + termo_y


# ============================================================================
# 2. VISUALIZAÇÃO DA FUNÇÃO RASTRIGIN
# ============================================================================

def visualizar_rastrigin():
    """
    Cria visualizações 2D e 3D da função Rastrigin para entender
    sua complexidade e a presença de múltiplos mínimos locais.
    """
    
    print("\n" + "=" * 70)
    print("VISUALIZAÇÃO DA FUNÇÃO RASTRIGIN")
    print("=" * 70)
    
    # Cria um grid de pontos no intervalo [-5.12, 5.12]
    # Este é o domínio tradicional da função Rastrigin
    x = np.linspace(-5.12, 5.12, 300)
    y = np.linspace(-5.12, 5.12, 300)
    X, Y = np.meshgrid(x, y)
    Z = rastrigin_2d(X, Y)
    
    # ---- Figura 1: Visualização 3D ----
    fig1 = plt.figure(figsize=(14, 6))
    
    ax1 = fig1.add_subplot(121, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                            linewidth=0, antialiased=True)
    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('Y', fontsize=12)
    ax1.set_zlabel('f(x,y)', fontsize=12)
    ax1.set_title('Função Rastrigin - Superfície 3D', fontsize=14)
    fig1.colorbar(surf, ax=ax1, shrink=0.5, aspect=10, label='f(x,y)')
    
    # Marca o mínimo global
    ax1.scatter([0], [0], [0], color='red', s=100, 
                label='Mínimo Global (0,0,0)')
    ax1.legend()
    
    # ---- Figura 2: Mapa de Contorno ----
    ax2 = fig1.add_subplot(122)
    contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
    ax2.contour(X, Y, Z, levels=20, colors='white', alpha=0.3, linewidths=0.5)
    ax2.set_xlabel('X', fontsize=12)
    ax2.set_ylabel('Y', fontsize=12)
    ax2.set_title('Função Rastrigin - Mapa de Contorno', fontsize=14)
    fig1.colorbar(contour, ax=ax2, label='f(x,y)')
    
    # Marca o mínimo global
    ax2.scatter([0], [0], color='red', s=100, marker='*', 
                label='Mínimo Global (0,0)')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()
    
    # ---- Análise descritiva ----
    print("\nANÁLISE DA FUNÇÃO RASTRIGIN:")
    print("-" * 50)
    print("• A função possui MÚLTIPLOS MÍNIMOS LOCAIS (vales) espalhados")
    print("  por todo o domínio [-5.12, 5.12]")
    print("• Apenas UM MÍNIMO GLOBAL em (0, 0) com f(0,0) = 0")
    print("• A função é 'acidentada' e desafiadora para métodos simples")
    print("• O domínio [-5.12, 5.12] é o mais comum para benchmarks")
    print("• A complexidade aumenta com o número de dimensões")
    print("-" * 50)
    
    return X, Y, Z


# ============================================================================
# 3. BUSCA ALEATÓRIA (MONTE CARLO)
# ============================================================================

def busca_aleatoria_rastrigin(iteracoes=10000, dominio=(-5.12, 5.12)):
    """
    Implementa a Busca Aleatória (Método de Monte Carlo) para encontrar
    o mínimo da função Rastrigin.
    
    Estratégia: Gera N pontos aleatórios no domínio e mantém o melhor.
    
    Parâmetros:
    -----------
    iteracoes : int
        Número de pontos aleatórios a testar
    dominio : tuple
        (limite_inferior, limite_superior) para ambas as dimensões
    
    Retorna:
    --------
    tuple (melhor_x, melhor_y, melhor_valor, historico, tempo)
    """
    inicio = time.time()
    
    # Inicializa com o pior caso possível
    melhor_x = None
    melhor_y = None
    melhor_valor = float('inf')
    
    # Histórico para visualização da convergência
    historico = []
    
    print(f"\nExecutando Busca Aleatória com {iteracoes} tentativas...")
    
    for i in range(iteracoes):
        # Gera coordenadas aleatórias no domínio
        x = random.uniform(dominio[0], dominio[1])
        y = random.uniform(dominio[0], dominio[1])
        
        # Avalia a função
        valor = rastrigin_2d(x, y)
        
        # Atualiza se encontrou um valor melhor
        if valor < melhor_valor:
            melhor_valor = valor
            melhor_x = x
            melhor_y = y
        
        # Guarda histórico a cada 100 iterações
        if i % 100 == 0:
            historico.append((i, melhor_valor, melhor_x, melhor_y))
    
    fim = time.time()
    tempo = fim - inicio
    
    print(f"   ✓ Melhor valor encontrado: {melhor_valor:.6f}")
    print(f"   ✓ Coordenadas: ({melhor_x:.4f}, {melhor_y:.4f})")
    print(f"   ✓ Tempo de execução: {tempo:.4f} segundos")
    
    return melhor_x, melhor_y, melhor_valor, historico, tempo


# ============================================================================
# 4. VISUALIZAÇÃO DOS RESULTADOS DA BUSCA
# ============================================================================

def visualizar_busca_aleatoria(X, Y, Z, melhor_x, melhor_y, melhor_valor, historico):
    """
    Visualiza os resultados da Busca Aleatória sobreposta à função Rastrigin.
    """
    
    fig2 = plt.figure(figsize=(14, 6))
    
    # ---- Subplot 1: Mapa de Contorno com pontos testados ----
    ax1 = fig2.add_subplot(121)
    contour = ax1.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.7)
    ax1.contour(X, Y, Z, levels=20, colors='white', alpha=0.2, linewidths=0.5)
    
    # Plota os pontos do histórico (a cada 100 iterações)
    if historico:
        hist_x = [h[2] for h in historico]  # coordenada x
        hist_y = [h[3] for h in historico]  # coordenada y
        hist_val = [h[1] for h in historico]  # valor
        
        # Mapeia valores para cores
        scatter = ax1.scatter(hist_x, hist_y, c=hist_val, cmap='hot_r', 
                            s=30, alpha=0.6, edgecolors='white', linewidth=0.5)
        fig2.colorbar(scatter, ax=ax1, label='f(x,y) encontrado')
    
    # Marca o mínimo global
    ax1.scatter([0], [0], color='lime', s=200, marker='*', 
                label='Mínimo Global (0,0)')
    
    # Marca o melhor encontrado
    ax1.scatter([melhor_x], [melhor_y], color='red', s=150, marker='X', 
                label=f'Melhor: ({melhor_x:.3f}, {melhor_y:.3f})')
    
    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('Y', fontsize=12)
    ax1.set_title('Mapa de Contorno com Pontos da Busca Aleatória', fontsize=14)
    ax1.legend()
    
    # ---- Subplot 2: Convergência do melhor valor ----
    ax2 = fig2.add_subplot(122)
    
    if historico:
        iteracoes = [h[0] for h in historico]
        valores = [h[1] for h in historico]
        
        ax2.plot(iteracoes, valores, 'b-', linewidth=2, label='Melhor valor')
        ax2.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Mínimo Global (0)')
        ax2.set_xlabel('Iterações', fontsize=12)
        ax2.set_ylabel('f(x,y) - Melhor Valor Encontrado', fontsize=12)
        ax2.set_title('Convergência da Busca Aleatória', fontsize=14)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.set_yscale('log')  # Escala logarítmica para melhor visualização
        
    plt.tight_layout()
    plt.show()


# ============================================================================
# 5. EXPERIMENTO: COMPARAÇÃO DE DESEMPENHO
# ============================================================================

def experimento_busca_aleatoria():
    """
    Realiza experimentos com diferentes números de iterações para
    demonstrar a ineficiência da Busca Aleatória.
    """
    
    print("\n" + "=" * 70)
    print("EXPERIMENTO: INFLUÊNCIA DO NÚMERO DE ITERAÇÕES")
    print("=" * 70)
    
    # Diferentes configurações de iterações
    configs = [
        (100, "100 tentativas"),
        (1000, "1.000 tentativas"),
        (10000, "10.000 tentativas"),
        (100000, "100.000 tentativas"),
    ]
    
    resultados = []
    
    for iteracoes, label in configs:
        print(f"\nExecutando: {label}")
        x, y, valor, _, tempo = busca_aleatoria_rastrigin(iteracoes)
        resultados.append({
            'iteracoes': iteracoes,
            'label': label,
            'x': x,
            'y': y,
            'valor': valor,
            'tempo': tempo,
            'erro': valor  # mínimo global é 0, então erro = valor
        })
    
    # Tabela comparativa
    print("\n" + "-" * 70)
    print("TABELA COMPARATIVA")
    print("-" * 70)
    print(f"{'Método':<20} {'Valor Encontrado':<18} {'Erro':<12} {'Tempo (s)':<10}")
    print("-" * 70)
    
    for r in resultados:
        print(f"{r['label']:<20} {r['valor']:<18.6f} {r['erro']:<12.6f} {r['tempo']:<10.4f}")
    
    print("-" * 70)
    
    # Análise dos resultados
    print("\nANÁLISE DOS RESULTADOS:")
    print("-" * 50)
    print("• A Busca Aleatória é INEFICIENTE para encontrar o mínimo global")
    print("• Mesmo com 100.000 tentativas, o erro ainda é significativo")
    print("• O tempo de execução cresce linearmente com as iterações")
    print("• A qualidade da solução melhora lentamente (lei da potência)")
    print("• Em altas dimensões, este método é completamente inviável")
    print("-" * 50)
    
    return resultados


# ============================================================================
# 6. FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Função principal que executa toda a demonstração.
    """
    
    print("=" * 70)
    print("COMPUTATIONAL INTELLIGENCE - AULA 01")
    print("DEMONSTRAÇÃO: FUNÇÃO RASTRIGIN E BUSCA ALEATÓRIA")
    print("=" * 70)
    
    print("""
OBJETIVO DA DEMONSTRAÇÃO:
-------------------------
1. Visualizar a complexidade da Função Rastrigin
2. Entender o conceito de mínimos locais vs. mínimo global
3. Demonstrar a ineficiência da Busca Aleatória (Monte Carlo)
4. Estabelecer a motivação para algoritmos mais sofisticados

FUNÇÃO: f(x,y) = 20 + (x² - 10·cos(2π·x)) + (y² - 10·cos(2π·y))
MÍNIMO GLOBAL: (0, 0) com f(0,0) = 0
    """)
    
    input("⏎ Pressione ENTER para iniciar a demonstração...")
    
    # Passo 1: Visualizar a função
    X, Y, Z = visualizar_rastrigin()
    
    input("\n⏎ Pressione ENTER para executar a Busca Aleatória...")
    
    # Passo 2: Executar Busca Aleatória
    melhor_x, melhor_y, melhor_valor, historico, tempo = busca_aleatoria_rastrigin(10000)
    
    # Passo 3: Visualizar resultados
    visualizar_busca_aleatoria(X, Y, Z, melhor_x, melhor_y, melhor_valor, historico)
    
    # Passo 4: Experimento comparativo
    input("\n⏎ Pressione ENTER para executar o experimento comparativo...")
    experimento_busca_aleatoria()
    
    # Conclusão
    print("\n" + "=" * 70)
    print(" DEMONSTRAÇÃO CONCLUÍDA!")
    print("=" * 70)

# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
