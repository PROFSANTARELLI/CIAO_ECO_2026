import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

def criar_sistema_triagem():
    """Cria e retorna o simulador fuzzy para triagem de incidentes."""
    impacto = ctrl.Antecedent(np.arange(0, 101, 1), 'impacto')
    urgencia = ctrl.Consequent(np.arange(0, 101, 1), 'urgencia')

    # Funções de pertinência simples
    impacto['baixo'] = fuzzy.trimf(impacto.universe, [0, 0, 50])
    impacto['alto'] = fuzzy.trapmf(impacto.universe, [40, 80, 100, 100])

    urgencia['baixa'] = fuzzy.trimf(urgencia.universe, [0, 0, 50])
    urgencia['alta'] = fuzzy.trapmf(urgencia.universe, [40, 80, 100, 100])

    # Regras básicas
    r1 = ctrl.Rule(impacto['baixo'], urgencia['baixa'])
    r2 = ctrl.Rule(impacto['alto'], urgencia['alta'])

    sistema = ctrl.ControlSystem([r1, r2])
    return ctrl.ControlSystemSimulation(sistema)

def calcular_urgencia(simulador, valor_impacto):
    """Executa a inferência garantindo que a entrada esteja na escala."""
    if not (0 <= valor_impacto <= 100):
        raise ValueError("O impacto deve estar entre 0% e 100%.")

    simulador.input['impacto'] = valor_impacto
    simulador.compute()
    return simulador.output['urgencia']

if __name__ == "__main__":
    simulador = criar_sistema_triagem()
    
    # Casos de teste
    entradas_teste = [20.0, 45.0, 90.0]

    print("=" * 55)
    print("      SIMULAÇÃO FUZZY")
    print("=" * 55)

    for valor in entradas_teste:
        urgencia_calculada = calcular_urgencia(simulador, valor)
        print(f"-> Entrada (Impacto): {valor:5.1f}% | Saída (Urgência): {urgencia_calculada:5.2f}%")

    print("=" * 55)
