AULA 03 AC-1 - PARTE FINAL

Para isso, é necessário obrigatoriamente que:
- Tenha finalizado todos os laboratórios da AC-1 PARTE 1 e PARTE 2
- Leia atentamento os passos deste roteiro.
- Criar o diretorio AULA_04 para guardar todas as entregas de hoje.

As entregas completas e corretas desta ETAPA FINAL AC-1 confere às duplas/trio o valor de até 0,25, estando todas as entregas realizadas e corretas.


Exercício 1: Análise do Elitismo na Estabilidade Algorítmica
Objetivo: Alterar a flag de controle do elitismo para observar o impacto da preservação do melhor indivíduo na curva de convergência.

import numpy as np

def calcular_custo(rota, matriz):
    dist = 0
    for i in range(len(rota)-1):
        dist += matriz[rota[i], rota[i+1]]
    return dist + matriz[rota[-1], rota[0]]

# Modifique para False para testar a execução sem elitismo
USAR_ELITISMO = True

NUM_NOS = 8
matriz_teste = np.random.uniform(10, 100, (NUM_NOS, NUM_NOS))
TAM_POP = 40
GERACOES = 80

populacao = [np.random.permutation(NUM_NOS) for _ in range(TAM_POP)]

for g in range(GERACOES):
    custos = [calcular_custo(ind, matriz_teste) for ind in populacao]
    melhor_idx = np.argmin(custos)
    
    novos = []
    if USAR_ELITISMO:
        novos.append(populacao[melhor_idx].copy())
        
    while len(novos) < TAM_POP:
        i1, i2 = np.random.choice(TAM_POP, 2, replace=False)
        pai = populacao[i1] if custos[i1] < custos[i2] else populacao[i2]
        
        filho = pai.copy()
        if np.random.rand() < 0.3:
            idx1, idx2 = np.random.choice(NUM_NOS, 2, replace=False)
            filho[idx1], filho[idx2] = filho[idx2], filho[idx1]
        novos.append(filho)
        
    populacao = novos

custos_finais = [calcular_custo(ind, matriz_teste) for ind in populacao]
print(f"[Exercício 1] Menor Custo Obtido (Elitismo={USAR_ELITISMO}): {min(custos_finais):.2f}")



Exercício 2: Inserção de Penalidades por Descumprimento de SLA
Objetivo: Implementar o cálculo de penalidade estática de +1000" ms"  para qualquer enlace cuja latência exceda o limite operacional de 50" ms" .

import numpy as np

np.random.seed(15)
matriz_latencia = np.random.uniform(5, 80, (6, 6))

def calcular_custo_com_sla(rota, matriz, limite_sla=50.0):
    custo_total = 0.0
    penalidade = 0.0
    
    for i in range(len(rota) - 1):
        latencia_enlace = matriz[rota[i], rota[i+1]]
        custo_total += latencia_enlace
        
        # Incrementa a penalidade caso a latência do enlace ultrapasse o SLA
        if latencia_enlace > limite_sla:
            penalidade += 1000.0
            
    return custo_total + penalidade

rota_teste = np.array([0, 1, 2, 3, 4, 5])
custo_final = calcular_custo_com_sla(rota_teste, matriz_latencia)

print(f"[Exercício 2] Custo Total (Com Penalizações de SLA): {custo_final:.2f} ms")



Exercício 3: Balanceamento de Carga em Servidores (Desafio de Código)
Especificação: Desenvolver o script desafio_03_alocacao_servidores.py.
	Cenário: Um conjunto de 20 tarefas com os seguintes tempos de processamento (em segundos):
  
T=[12,35,40,8,15,22,19,45,60,31,14,28,50,18,25,33,42,10,5,29]

	Infraestrutura: 4 servidores disponíveis.
  
	Objetivo: Minimizar o Makespan (tempo total gasto pelo servidor com a maior carga acumulada).
  
	Representação do Indivíduo: Vetor de 20 posições contendo inteiros no intervalo [0,3], em que o índice representa a tarefa e o valor representa o servidor atribuído.


4. Desafio de Fechamento da AC-1

Especificação Técnica: Motor de Decisioning SD-WAN Zero-Trust

Nome do Arquivo: desafio_ac1_master_sdwan.py

Cenário de Operação:

Desenvolver o algoritmo de seleção de rota para um nó de comutação central em uma topologia contendo 12 roteadores (indexados de 0 a 11), com origem fixa no Nó 0 e destino no Nó 11.

Cada enlace possui três parâmetros característicos:
	Latência ("ms" ): Valor real positivo.
	Taxa de Perda de Pacotes (%): Valor real no intervalo [0,100].
	Índice de Reputação de Segurança (0" a " 100): Nós com índice <50 são considerados não confiáveis (risco de interceptação ou comprometimento).

Requisitos da Implementação:
	Estruturar a matriz de adjacência e atributos para os 12 nós.
	Implementar a função de fitness ponderada com penalização de segurança:
"Fitness" (X)=w_1⋅"LatenciaTotal" (X)+w_2⋅"PerdaPacotesTotal" (X)+P_"Seguranca"  em que P_"Seguranca" =5000 caso qualquer nó pertencente à rota apresente reputação <50.
	
  Configurar a amostragem estocástica com a semente np.random.seed(2026).
	
  Incluir no cabeçalho do arquivo um relatório técnico descrevendo a rota selecionada e justificando o desvio em relação aos nós penalizados.

