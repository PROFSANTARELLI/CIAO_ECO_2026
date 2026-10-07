Em vez de um cenário pronto, você vai escolher um problema do mundo real em que o raciocínio "mais ou menos" faz sentido e construir, do zero, um sistema de inferência fuzzy para resolvê-lo.
A ideia é passar pelo processo completo: identificar o problema, modelar, implementar e avaliar o resultado.

Escolher um bom problema: Um problema serve para este projeto se atender a todos os critérios:

1 - Tem pelo menos duas entradas e uma saída numéricas (ex.: sensores, notas, medidas).
2 - As entradas são naturalmente descritas com termos vagos ("pouco", "muito", "perto"), sem um limite exato.
3 - A decisão não é trivial: ao menos 6 regras fazem sentido.
4 - Se o problema puder ser resolvido por um simples if valor > 30, ele não serve.

Banco de sugestões (escolha uma ou proponha a sua)
Área	                    Problema
Saúde e bem-estar	        Intensidade ideal de treino a partir de sono e frequência cardíaca de repouso
Educação	                Risco de evasão de um aluno a partir de frequência e desempenho
Casa e energia	          Potência de um chuveiro ou aquecedor a partir da temperatura da água e da vazão
Mobilidade	              Tempo do semáforo verde a partir do tamanho da fila e do fluxo de pedestres
Jogos	                    Nível de agressividade de um inimigo a partir da vida do jogador e da distância
Agro	                    Dose de fertilizante a partir do tipo de solo (acidez) e da fase da cultura
Finanças pessoais	        Limite de gasto mensal sugerido a partir da renda e do nível de dívidas
Segurança	                Nível de alerta de um alarme a partir de ruído e movimento detectados
Alimentação	              Tempo de cozimento a partir do peso e da espessura do alimento
Meio ambiente	            Alerta de qualidade do ar a partir de partículas e umidade

Dica: problemas ligados ao seu dia a dia costumam gerar projetos melhores.

Etapas:
Etapa 1: Definição do problema (antes de programar): Descreva em até 10 linhas o problema, quem decide hoje, quais são as entradas e a saída, e por que fuzzy é adequado.
Etapa 2: Modelagem: o universo de discurso (com unidade), os termos linguísticos e a forma das funções de pertinência. Escreva a base de regras completa (mínimo de 6 regras, usando E e OU ao menos uma vez cada) e desenhe, à mão ou em código, as funções de pertinência.
Etapa 3: Implementação: Crie o código em Python. Pode usar NumPy e Matplotlib.
Etapa 4: Testes: Teste com no mínimo 4 situações. Registre as entradas, a saída do sistema e a resposta esperada. (coloque tudo no resultados_aula09.md)
Etapa 5: Entrega: Código-fonte (.py) executável.
