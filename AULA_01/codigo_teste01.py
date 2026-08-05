#FUNÇÃO: f(x,y) = 20 + (x² - 10·cos(2π·x)) + (y² - 10·cos(2π·y))
#MÍNIMO GLOBAL: (0, 0) com f(0,0) = 0

# Importa a biblioteca NumPy para manipulação de matrizes e cálculos matemáticos vetoriais
import numpy as np

# Importa a biblioteca Matplotlib para geração de gráficos 2D e 3D
import matplotlib.pyplot as plt

# Importa o módulo time para medir a eficiência computacional e tempo de execução
import time

# Define a função objetivo Rastrigin em 2D que recebe as coordenadas x e y
def rastrigin(x, y):
    # Retorna o valor de fitness calculado pela fórmula matemática da Rastrigin
    return 20 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))

# Define um intervalo discreto de 100 pontos entre -5.12 e 5.12 para o eixo X
x_range = np.linspace(-5.12, 5.12, 100)

# Define um intervalo discreto de 100 pontos entre -5.12 e 5.12 para o eixo Y
y_range = np.linspace(-5.12, 5.12, 100)

# Gera a grade bidimensional (malha de pontos) combinando todos os valores de X e Y
X, Y = np.meshgrid(x_range, y_range)

# Executa a função Rastrigin para cada par de coordenadas na malha gerada
Z = rastrigin(X, Y)

# Cria a estrutura da figura do gráfico com tamanho de 10 por 6 polegadas
fig = plt.figure(figsize=(10, 6))

# Adiciona um subgráfico tridimensional (3D) à figura criada
ax = fig.add_subplot(111, projection='3d')

# Plota a superfície 3D utilizando a paleta de cores 'viridis' e transparência 0.8
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)

# Adiciona a barra lateral indicando os valores de custo/fitness da função
fig.colorbar(surf, shrink=0.5, aspect=5)

# Define o título principal do gráfico
ax.set_title("Espaço de Busca 3D: Função Rastrigin")

# Exibe a janela gráfica na tela
plt.show()

# Fixa a semente de gerador de números aleatórios para permitir reprodutibilidade dos testes
np.random.seed(42)

# Define a quantidade total de amostras aleatórias que o algoritmo irá testar
NUM_TENTATIVAS = 1000

# Inicializa a variável com valor infinito para garantir que a primeira tentativa seja aceita
melhor_custo = float('inf')

# Inicializa as variáveis de melhor coordenada X e Y como nulas
melhor_x, melhor_y = None, None

# Cria uma lista vazia para armazenar o histórico do melhor resultado ao longo do tempo
historico = []

# Registra o instante de tempo de início do processo de busca
tempo_inicio = time.time()

# Loop de repetição executado NUM_TENTATIVAS vezes
for tentativa in range(NUM_TENTATIVAS):
    # Sorteia um valor aleatório contínuo entre -5.12 e 5.12 para o candidato X
    x_cand = np.random.uniform(-5.12, 5.12)
    
    # Sorteia um valor aleatório contínuo entre -5.12 e 5.12 para o candidato Y
    y_cand = np.random.uniform(-5.12, 5.12)
    
    # Avalia o candidato sorteado passando as coordenadas na função Rastrigin
    custo_atual = rastrigin(x_cand, y_cand)
    
    # Verifica se o custo atual obtido é menor do que o melhor custo registrado até agora
    if custo_atual < melhor_custo:
        # Atualiza o melhor custo com o novo valor mais baixo encontrado
        melhor_custo = custo_atual
        
        # Atualiza a melhor coordenada X registrada
        melhor_x = x_cand
        
        # Atualiza a melhor coordenada Y registrada
        melhor_y = y_cand
        
    # Adiciona o melhor custo atual à lista de histórico para acompanhamento da evolução
    historico.append(melhor_custo)

# Registra o instante de tempo de encerramento da busca
tempo_fim = time.time()

# Exibe no terminal a melhor coordenada X encontrada
print(f"Melhor X: {melhor_x:.4f}")

# Exibe no terminal a melhor coordenada Y encontrada
print(f"Melhor Y: {melhor_y:.4f}")

# Exibe no terminal o menor valor de custo (fitness) alcançado pelo algoritmo
print(f"Melhor Custo: {melhor_custo:.4f}")

# Exibe o tempo total gasto na busca em milissegundos
print(f"Tempo: {(tempo_fim - tempo_inicio)*1000:.2f} ms")

# Cria uma figura para o gráfico de linha de convergência 2D
plt.figure(figsize=(8, 4))

# Plota a linha de evolução do histórico na cor vermelha
plt.plot(historico, color='red')

# Define o título do gráfico de convergência
plt.title("Evolução da Busca Aleatória")

# Define o rótulo do eixo horizontal (tentativas)
plt.xlabel("Tentativas")

# Define o rótulo do eixo vertical (menor custo encontrado)
plt.ylabel("Melhor Custo")

# Adiciona a grade de linhas ao fundo do gráfico
plt.grid(True)

# Exibe o gráfico 2D na tela
plt.show()
