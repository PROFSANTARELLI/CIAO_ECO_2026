Desafio 01
Instruções
Modifique o notebook desenvolvendo a solução para o problema de otimização da Função Ackley (outra função clássica de teste). Complete os trechos indicados com # SEU CÓDIGO AQUI.

Formulação matemática da Função Ackley 2D:

<img width="515" height="204" alt="image" src="https://github.com/user-attachments/assets/860ecbf9-8e1b-4dc8-ab38-6010a116b45d" />


Codigo para executar no Collab:

import numpy as np
import matplotlib.pyplot as plt

def ackley(x, y):
    # TODO: Implemente a fórmula da Função Ackley apresentada acima
    # Dica: Utilize np.exp, np.sqrt, np.cos e np.pi
    # SEU CÓDIGO AQUI
    pass

# TODO: Ajuste o intervalo de busca para [-32.768, 32.768] e execute 2.000 tentativas
NUM_TENTATIVAS = 2000
LIXO_MIN, LIXO_MAX = -32.768, 32.768

melhor_custo = float('inf')
melhor_x, melhor_y = None, None
historico = []

for _ in range(NUM_TENTATIVAS):
    # TODO: Gere coordenadas aleatórias no novo intervalo
    # SEU CÓDIGO AQUI
    
    # TODO: Avalie a função Ackley e atualize o melhor resultado encontrado
    # SEU CÓDIGO AQUI
    pass

# TODO: Exiba os resultados finais obtidos e plote o gráfico de convergência
