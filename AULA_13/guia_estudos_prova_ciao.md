# Sistemas Especialistas, Regras de Produção e Representação do Conhecimento

1. Sistema Especialista

Programa de computador projetado para imitar a tomada de decisão de um especialista humano em uma área específica (como um médico diagnosticando uma doença ou um engenheiro analisando uma falha de rede).

Enquanto o Machine Learning aprende padrões sozinho a partir de milhares de dados históricos, o Sistema Especialista recebe o conhecimento pronto, estruturado diretamente por humanos.

---

2. Como o Sistema Funciona por Dentro - Arquitetura

Todo sistema especialista clássico é dividido em 3 partes principais:

 - Base de Conhecimento: O "manual de instruções" do especialista. Guarda as regras fixas do domínio.

 - Base de Fatos (Memória de Trabalho): Os dados da situação atual (ex: os sintomas do paciente agora ou os alertas do servidor hoje).

 - Motor de Inferência: O "cérebro" que compara os Fatos com as Regras para chegar a uma conclusão.

---

3. Representação do Conhecimento: Regras de Produção

É a forma mais comum de traduzir a experiência humana para o computador. Elas seguem sempre a estrutura condicional:

SE <condição / premissa> ENTÃO <conclusão / ação>

Exemplo Prático (Segurança Cibernética):

 - Regra 1: SE tentativas de login falhas > 5 E origem é IP externo ENTÃO suspeita de ataque de força bruta.

 - Regra 2: SE suspeita de ataque de força bruta ENTÃO bloquear IP por 30 minutos.

---

 4. Como o Motor de Inferência Pensa.
 
Existem duas estratégias clássicas para o motor navegar pelas regras:

<img width="989" height="342" alt="image" src="https://github.com/user-attachments/assets/12a2116d-47bd-40b5-869c-b06fcbee30ba" />


---

## Fundamentos de Lógica Fuzzy

### 1. Lógica Booleana vs. Lógica Fuzzy

* **Lógica Booleana (Clássica):** Trabalha com extremos binários (`0` ou `1`, `Falso` ou `Verdadeiro`). Cria "degraus" abruptos: se o limite de alerta é $90\%$, uma leitura de $89.9\%$ é tratada como $100\%$ crítica e $90.1\%$ como $100\%$ normal.
* **Lógica Fuzzy (Difusa):** Trabalha com **graus de pertinência ($\mu$)** contínuos no intervalo $[0.0, 1.0]$. Permite que um mesmo valor numérico pertença parcialmente a dois conjuntos vizinhos (ex: *30°C é 0.7 Quente e 0.3 Ameno*), garantindo transições suaves.

### 2. Conceitos Estruturais

* **Universo do Discurso ($U$):** O intervalo numérico total possível para uma variável (ex: `Impacto` de $0$ a $100\%$, `SpO2` de $70\%$ a $100\%$).
* **Fuzzificação:** Etapa que converte um número exato (*crisp*) vindo de um sensor em graus de pertinência para os termos linguísticos.
* **Funções de Pertinência (`scikit-fuzzy`):**
* **Triangular (`fuzz.trimf`):** Definida por 3 pontos $[a, b, c]$, onde $b$ é o pico ($\mu = 1.0$). Ideal para conceitos intermediários (ex: `"Médio"`).
* **Trapezoidal (`fuzz.trapmf`):** Definida por 4 pontos $[a, b, c, d]$, criando um platô de saturação ($\mu = 1.0$) entre $b$ e $c$. Ideal para extremos críticos (ex: `"Impacto Alto"` acima de $80\%$).


---

## Motor de Inferência Mamdani e Defuzzificação

### 1. Pipeline de Mamdani (4 Etapas)

1. **Fuzzificação:** Converte entradas numéricas em graus de pertinência ($\mu$).
2. **Avaliação das Regras (Implicação):** Aplica os operadores lógicos Fuzzy sobre os antecedentes:
* Operador **AND (`&`)** $\rightarrow$ Utiliza o **Mínimo**: $\min(\mu_A, \mu_B)$.
* Operador **OR (`|`)** $\rightarrow$ Utiliza o **Máximo**: $\max(\mu_A, \mu_B)$.
* *Recorte (Clipping):* A altura resultante da regra corta o topo do conjunto de saída.


3. **Agregação:** Une todas as áreas recortadas das regras ativadas usando o **Máximo** (união geométrica).
4. **Defuzzificação:** Converte a forma geométrica resultante de volta em um único número exato (*crisp*).

### 2. Centroide vs. MOM (O Desafio dos Extremos)

* **Centroide (`centroid`):** Calcula o centro de massa geométrico da figura agregada. Garante curvas suaves e contínuas, mas **nunca atinge exatamente $0\%$ ou $100\%$** nos extremos porque qualquer figura geométrica com largura tem seu centro de gravidade deslocado para dentro.
* **MOM (*Mean of Maximum*):** Calcula a média dos pontos onde a pertinência atinge o valor máximo. Atinge os extremos, mas gera saltos bruscos no meio da escala.

### 3. Superfície de Decisão 3D

É o gráfico gerado ao simular todas as combinações possíveis de duas entradas. Se a superfície apresentar "buracos" ou quedas abruptas para `0.0` (ou erro de chave no código), significa que **faltam regras na matriz** (ex: matriz $3 \times 3$ incompleta) ou falta sobreposição entre os conjuntos de pertinência.

---

## Qualidade de Software e Testes Automatizados em IA

Modelos de Inteligência Computacional em produção exigem validação rigorosa com frameworks como o **`pytest`**.

### Os 4 Pilares de Teste em Sistemas Fuzzy

1. **Sanidade / Limites de Universo:** Garantir que a saída *crisp* nunca ultrapasse os limites físicos definidos (ex: $0 \le \text{Urgência} \le 100$).
2. **Monotonicidade:** Garantir que a lógica de negócio é coerente (ex: aumentar o *Impacto* mantendo a *Explorabilidade* fixa **nunca** pode diminuir a *Urgência*).
3. **Robustez / Exceções de Borda:** Validar se entradas impossíveis ou fora de escala (ex: `SpO2 = 105%` ou `Impacto = -5%`) disparam `ValueError` antes de quebrar o motor.
4. **SLA de Latência:** Medir o tempo médio por inferência para assegurar resposta em tempo real (ex: $< 10\text{ ms}$).

---

## Otimização Multiobjetivo, Fronteira de Pareto e NSGA-II

### 1. O Problema dos Objetivos Conflitantes

Na vida real, melhorar um critério frequentemente piora outro (ex: *reduzir a latência de um servidor exige aumentar o custo financeiro*). Como não existe uma única solução perfeita para tudo, buscamos o melhor conjunto de **compromissos (*trade-offs*)**.

### 2. Dominância de Pareto e Fronteira de Pareto

* **Dominância de Pareto:** Uma solução $A$ domina uma solução $B$ ($A \succ B$) se $A$ **não é pior** que $B$ em nenhum objetivo e é **estritamente melhor** em pelo menos um objetivo.
* **Fronteira de Pareto:** É o conjunto de todas as soluções **não-dominadas** entre si. Escolher qual ponto da fronteira adotar é uma decisão estratégica de negócio, não matemática.

### 3. Algoritmo NSGA-II (*Non-dominated Sorting Genetic Algorithm II*)

É o algoritmo evolucionário padrão para encontrar a Fronteira de Pareto, equilibrando dois mecanismos:

1. **Fast Non-Dominated Sorting (Convergência):** Classifica a população em camadas/frentes ($F_1, F_2, \dots$). A Frente $F_1$ (soluções não-dominadas) tem prioridade absoluta para sobreviver, empurrando a evolução rumo ao ótimo.
2. **Crowding Distance (Diversidade):** Mede a distância de uma solução até seus vizinhos na mesma frente. Prioriza soluções mais isoladas para manter a fronteira bem espalhada e evitar que a população se concentre em um único ponto.

### 4. Convenções Obrigatórias no Framework `pymoo`

Ao modelar uma classe herdando de `ElementwiseProblem`:

* **Minimização Padrão (`out["F"]`):** O `pymoo` **sempre minimiza** todos os objetivos. Para **maximizar** um objetivo (ex: Lucro ou Vazão), basta multiplicar sua equação por `-1`.
* **Restrições de Desigualdade (`out["G"]`):** Toda restrição deve ser escrita no formato $g(x) \le 0$. Por exemplo, se a latência não pode ultrapassar $25\text{ ms}$, escreve-se `g1 = latencia - 25.0`.


```
