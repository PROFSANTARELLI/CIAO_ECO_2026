# ==============================================================================
# AULA 09 — SPRINT 1 (AC-3): MODELAGEM DAS VARIÁVEIS E CONJUNTO FUZZY
# Objetivo: Construir as Variáveis Linguísticas e Funções de Pertinência
# ==============================================================================

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

def criar_sistema_fuzzy():
    """
    Define o Universo do Discurso, as Variáveis Linguísticas
    e mapear as Funções de Pertinência (Membership Functions) do problema.
    """
    # --------------------------------------------------------------------------
    # ETAPA 1: DEFINIÇÃO DOS UNIVERSOS DO DISCURSO (UNIVERSES OF DISCOURSE)
    # --------------------------------------------------------------------------
    # Antecedente 1: Impacto no Negócio (0 a 100%)
    impacto = ctrl.Antecedent(np.arange(0, 101, 1), 'impacto')
    
    # Antecedente 2: Explorabilidade da Falha (0 a 10)
    explorabilidade = ctrl.Antecedent(np.arange(0, 11, 1), 'explorabilidade')
    
    # Consequente: Urgência de Resposta/Atendimento (0 a 100%)
    urgencia = ctrl.Consequent(np.arange(0, 101, 1), 'urgencia')

    # --------------------------------------------------------------------------
    # ETAPA 2: CONFIGURAÇÃO DO MÉTODO DE DEFUZZIFICAÇÃO
    # --------------------------------------------------------------------------
    urgencia.defuzzify_method = 'centroid'

    # --------------------------------------------------------------------------
    # ETAPA 3: FUNÇÕES DE PERTINÊNCIA DA VARIÁVEL "IMPACTO" (0 a 100)
    # trimf = Triangular [início, topo_máximo, fim]
    # trapmf = Trapezoidal [início_rampa, topo_inicio, topo_fim, fim_rampa]
    # --------------------------------------------------------------------------
    impacto['baixo'] = fuzzy.trimf(impacto.universe, [0, 0, 40])
    impacto['medio'] = fuzzy.trimf(impacto.universe, [20, 50, 80])
    impacto['alto'] = fuzzy.trapmf(impacto.universe, [60, 80, 100, 100])

    # --------------------------------------------------------------------------
    # ETAPA 4: FUNÇÕES DE PERTINÊNCIA DA VARIÁVEL "EXPLORABILIDADE" (0 a 10)
    # --------------------------------------------------------------------------
    explorabilidade['baixa'] = fuzzy.trimf(explorabilidade.universe, [0, 0, 4])
    explorabilidade['moderada'] = fuzzy.trimf(explorabilidade.universe, [2, 5, 8])
    explorabilidade['alta'] = fuzzy.trimf(explorabilidade.universe, [6, 10, 10])

    # --------------------------------------------------------------------------
    # ETAPA 5: FUNÇÕES DE PERTINÊNCIA DA VARIÁVEL "URGÊNCIA" (0 a 100)
    # --------------------------------------------------------------------------
    urgencia['baixa'] = fuzzy.trimf(urgencia.universe, [0, 0, 30])
    urgencia['media'] = fuzzy.trimf(urgencia.universe, [20, 50, 70])
    urgencia['alta'] = fuzzy.trimf(urgencia.universe, [60, 80, 90])
    urgencia['critica'] = fuzzy.trapmf(urgencia.universe, [80, 90, 100, 100])

    return impacto, explorabilidade, urgencia


def gerar_graficos_pertinencia():
    """
    Visualiza graficamente os conjuntos fuzzy e salva a imagem de validação.
    """
    impacto, explorabilidade, urgencia = criar_sistema_fuzzy()
    
    Path("results").mkdir(exist_ok=True)
    
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 8))
    impacto.view(ax=ax0)
    explorabilidade.view(ax=ax1)
    urgencia.view(ax=ax2)
    
    plt.tight_layout()
    plt.savefig('results/membership_functions.png')
    plt.close()
    print("Sucesso: Gráfico 'results/membership_functions.png' gerado com êxito!")


if __name__ == "__main__":
    gerar_graficos_pertinencia()

#ATENÇÃO: Você deve explicar no resultados o que a lógica fuzzy realiza
