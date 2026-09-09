**AULA 06 - ACO E ALGORITMOS HÍBRIDOS**


ACO (Ant Colony Optimization), Otimização por Colônia de Formigas.

É um algoritmo de otimização inspirado no comportamento das formigas. Várias formigas virtuais exploram diferentes caminhos e deixam feromônio nas rotas encontradas.

Com o passar das iterações: bons caminhos → mais feromônio → maior chance de serem escolhidos → melhores soluções

**Resumindo:**

ACO é um algoritmo que encontra boas soluções por meio da exploração de caminhos e da aprendizagem coletiva através do feromônio. É especialmente útil para problemas de rotas, caminhos e grafos, como o roteamento de redes.

**Case: Encontrando a melhor rota em uma rede.**

Situação: temos uma rede de computadores. Um pacote precisa sair do **servidor 0** e chegar ao **servidor 5**. Existem vários caminhos possíveis e cada conexão possui um custo. Nosso objetivo é encontrar uma rota de menor custo.

<img width="112" height="233" alt="image" src="https://github.com/user-attachments/assets/2ec4c42c-62f9-4993-9a25-d4b4ce73f7d0" />


Pergunta: Como descobririam o melhor caminho?

É exatamente nesse ponto que começa o ACO.

PARTE 1 — A formiga precisa escolher um caminho

No ACO, criamos várias formigas virtuais. Cada uma delas percorre a rede tentando encontrar uma boa rota.


**O ciclo do ACO**

O funcionamento pode ser construído em quatro etapas:

1. CRIAR
   Formigas

      ↓

2. CONSTRUIR
   Caminhos

      ↓

3. AVALIAR
   Custo das rotas

      ↓

4. ATUALIZAR
   Evaporação + Feromônio

      ↓

    REPETIR
"""

import numpy as np
import random

O grafo é representado por uma matriz de custos:

CUSTOS = np.array([
    [0, 2, 4, np.inf, np.inf, np.inf],
    [2, 0, 1, 5, np.inf, np.inf],
    [4, 1, 0, 2, 3, np.inf],
    [np.inf, 5, 2, 0, 1, 4],
    [np.inf, np.inf, 3, 1, 0, 2],
    [np.inf, np.inf, np.inf, 4, 2, 0]
])

estamos usando np.inf para representar que não existe ligação direta entre dois nós. Neste problema, estamos usando o infinito para representar um caminho que não existe.
O que essa matriz representa? CUSTOS[0][1] = 2 (Ir do nó 0 para o nó 1 custa 2)

ORIGEM = 0
DESTINO = 5

"""PARTE 2 - A formiga precisa saber quais caminhos existem

A formiga está no nó 0. Ela não pode simplesmente escolher qualquer nó. Ela precisa saber quais são seus vizinhos.
"""

def obter_vizinhos(no):

    vizinhos = []

    for proximo in range(len(CUSTOS)):

        if CUSTOS[no][proximo] != np.inf and proximo != no:
            vizinhos.append(proximo)

    return vizinhos

print(obter_vizinhos(0))

"""Por que a formiga só pode escolher 1 ou 2?

Porque são os nós diretamente conectados ao nó 0.

conceito de Vizinhança = conjunto de movimentos possíveis a partir da posição atual.

**PARTE 3 - Mas como a formiga escolhe?**

Agora vem a primeira grande ideia do ACO.

"Se existem dois caminhos, como a formiga decide?"

Imagine:

0 → 1 = custo 2
0 → 2 = custo 4

Naturalmente, gostaríamos que o caminho de custo 2 fosse mais atraente.

Mas existe outro problema:

"E se uma formiga descobrir um caminho muito bom?"

Aí entra o conceito de feromônio.

"As formigas virtuais possuem uma memória coletiva. Essa memória é representada pelo feromônio."
"""

feromonio = np.ones_like(CUSTOS, dtype=float)

feromonio[CUSTOS == np.inf] = 0

print(feromonio)

"""No início, todos os caminhos disponíveis possuem a mesma quantidade de feromônio."

Visualmente:

Caminho A → 1.0
Caminho B → 1.0
Caminho C → 1.0

Ou seja: No começo, nenhuma experiência foi acumulada.

**PARTE 4 — O primeiro comportamento inteligente**

A formiga vai considerar duas coisas:

1. Quanto feromônio existe?
2. Quanto custa o caminho?

Então:

FEROMÔNIO + CUSTO = ATRATIVIDADE

A fórmula:

$$ Atratividade = \tau^\alpha \left(\frac{1}{c}\right)^\beta $$

Simplesmente:

"Quanto maior o feromônio, mais interessante o caminho."

"Quanto menor o custo, mais interessante o caminho."



ALPHA = 1 -> ALPHA controla a influência do feromônio.

BETA = 2 -> BETA controla a influência do custo.


Então:

ALPHA alto
→ confiar mais na experiência

BETA alto
→ confiar mais no custo


**PARTE 5 — Vamos fazer uma formiga andar:**
"""

def escolher_proximo(no_atual, visitados):

    vizinhos = obter_vizinhos(no_atual)

    candidatos = [
        no for no in vizinhos
        if no not in visitados
    ]

    if not candidatos:
        return None

    atratividades = []

    for proximo in candidatos:

        fer = feromonio[no_atual][proximo]
        custo = CUSTOS[no_atual][proximo]

        atratividade = (
            fer ** ALPHA
            * (1 / custo) ** BETA
        )

        atratividades.append(atratividade)

    soma = sum(atratividades)

    probabilidades = [
        x / soma
        for x in atratividades
    ]

    return random.choices(
        candidatos,
        weights=probabilidades,
        k=1
    )[0]

"""Manualmente:

0 → 1 custo = 2

e:

0 → 2 custo = 4

Com:

feromônio = 1

BETA = 2


Teremos:

0 → 1

1 × (1/2)²
= 0,25

e:

0 → 2

1 × (1/4)²
= 0,0625


Portanto:

0 → 1 é muito mais atrativo.

**PARTE 6 — A formiga encontrou uma rota**

Agora construímos a rota inteira.
"""

ALPHA = 1
BETA = 2

def construir_rota():

    rota = [ORIGEM]

    atual = ORIGEM

    while atual != DESTINO:
        proximo = escolher_proximo(
            atual,
            rota
        )

        if proximo is None:
            return None

        rota.append(proximo)

        atual = proximo

    return rota

for i in range(5):

  rota = construir_rota()

  print("Formiga", i + 1, ":", rota)

"""**Todas encontraram a mesma rota?**

E isso é proposital. O ACO não faz todas as formigas seguirem exatamente o mesmo caminho. Existe exploração."

Exploração → experimentar caminhos diferentes

Explotação → aproveitar caminhos que parecem bons

Seguindo...


**PARTE 7 — Precisamos avaliar as formigas agora**

Até agora temos rotas. Mas não sabemos qual é melhor.

Então:
"""

def calcular_custo(rota):

    total = 0

    for i in range(len(rota) - 1):

        origem = rota[i]
        destino = rota[i + 1]

        total += CUSTOS[origem][destino]

    return total

for i in range(5):

    rota = construir_rota()

    custo = calcular_custo(rota)

    print(
        "Rota:",
        rota,
        "| Custo:",
        custo
    )

Pergunta: "Qual dessas rotas deveria receber mais feromônio?"

Resposta: As melhores, ou seja, as de menor custo.

"""**PARTE 8 — A formiga deixa uma trilha**

Agora vamos introduzir o depósito de feromônio.


"""

Q = 100

def depositar_feromonio(rota, custo):

    deposito = Q / custo

    for i in range(len(rota) - 1):

        origem = rota[i]
        destino = rota[i + 1]

        feromonio[origem][destino] += deposito

"""Se: custo = 10

então: 100 / 10 = 10

Se: custo = 20

então: 100 / 20 = 5

Portanto:

ROTA MELHOR -> MAIS FEROMÔNIO -> MAIOR CHANCE DE SER ESCOLHIDA

Esse é o coração do ACO.

**PARTE 9 — Evaporação**

Agora vem a evaporação.

Se uma rota recebeu muito feromônio no começo, devemos confiar nela para sempre?

Não. Por isso existe evaporação.
"""

TAXA_EVAPORACAO = 0.5

def evaporar_feromonio():

    global feromonio

    feromonio *= (1 - TAXA_EVAPORACAO)

"""Se temos: 10 unidades e evaporamos 50%:

10 × 0,5 = 5

Então:

Feromônio antigo -> evapora -> novas experiências podem ganhar importância

Isso evita que uma escolha inicial domine o algoritmo para sempre.

**PARTE 10 — Agora temos uma colônia**
"""

NUM_FORMIGAS = 20
NUM_ITERACOES = 50

melhor_rota = None
melhor_custo = float("inf")

historico = []

for iteracao in range(NUM_ITERACOES):

    rotas = []

    # Cada formiga constrói uma rota
    for _ in range(NUM_FORMIGAS):

        rota = construir_rota()

        if rota is not None:

            custo = calcular_custo(rota)

            rotas.append((rota, custo))

            if custo < melhor_custo:

                melhor_custo = custo
                melhor_rota = rota.copy()

    # Evapora o feromônio antigo
    evaporar_feromonio()

    # Reforça as rotas encontradas
    for rota, custo in rotas:

        depositar_feromonio(
            rota,
            custo
        )

    # Guarda o melhor resultado
    historico.append(melhor_custo)

print("Melhor rota:", melhor_rota)
print("Melhor custo:", melhor_custo)

"""**O que aconteceu durante essas 50 iterações?**

FORMIGAS

↓

exploram caminhos

↓

avaliam as rotas

↓

boas rotas recebem feromônio

↓

feromônio influencia novas escolhas

↓

feromônio antigo evapora

↓

processo se repete

↓

melhores caminhos tendem a ser reforçados

PARTE 11 — Plotagem **negrito**
"""

import matplotlib.pyplot as plt

plt.plot(historico)

plt.xlabel("Iteração")
plt.ylabel("Melhor custo")
plt.title("Convergência do ACO")

plt.grid()
plt.show()

"""Agora estamos vendo a aprendizagem do algoritmo.

No início muitas possibilidades.

Depois, alguns caminhos começam a se destacar

Finalmente, o algoritmo encontra uma solução muito boa

**PARTE 12 — O problema dos algoritmos**

Pergunta: O ACO resolveu nosso problema. Então podemos usar somente ACO para tudo?

... Não necessariamente!

E aí você apresenta:

Cada algoritmo tem pontos fortes e limitações.

Por exemplo:

GA → boa exploração

PSO → rápida busca/refinamento

ACO → excelente para problemas de caminhos e grafos

E...

...se combinarmos algoritmos?

Introdução ao algoritmo híbrido

Imagine:

Um algoritmo encontra uma região promissora e outro tenta melhorar a solução dentro dessa região.

Uma analogia simples:

GA = explorador

Busca Local = especialista

Híbrido = explorador encontra o local
           ↓
           especialista faz o ajuste fino

**A ideia central da Aula 06**

Até aqui aprendemos:

GA -> Evolui uma população de soluções.

ACO - > Aprende quais caminhos são mais promissores através do feromônio.

Algoritmo Híbrido -> Combina estratégias diferentes para aproveitar suas vantagens.

**E se pudermos combinar diferentes estratégias para obter uma solução melhor?**

**É exatamente isso que vamos experimentar no laboratório desta aula.**

Na prática

1 - Implementar o mecanismo básico do ACO.
2 - Visualizar a evolução do feromônio.
3 - Experimentar uma estratégia híbrida.
4 - Comparar GA, PSO e Híbrido.
"""
