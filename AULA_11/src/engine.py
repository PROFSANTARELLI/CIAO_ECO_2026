from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from skfuzzy import control as ctrl

# Importa a função de modelagem construída na Sprint 1 (Aula 09)
from src.model import criar_sistema_fuzzy


def construir_motor_inferencia():
    """
    Instancia o sistema fuzzy e mapeia as 9 regras de inferência (Mamdani)
    garantindo cobertura total da matriz 3x3.
    """
    # Recupera os antecedentes e consequentes configurados na Aula 09
    impacto, explorabilidade, urgencia = criar_sistema_fuzzy()

    # --------------------------------------------------------------------------
    # BASE DE REGRAS FUZZY (Mapeamento 3 x 3 = 9 Combinações)
    # Operador '&' no scikit-fuzzy representa o Fuzzy AND (Mínimo de Mamdani)
    # --------------------------------------------------------------------------
    
    # Bloco 1: Impacto Baixo
    regra1 = ctrl.Rule(impacto['baixo'] & explorabilidade['baixa'], urgencia['baixa'])
    regra2 = ctrl.Rule(impacto['baixo'] & explorabilidade['moderada'], urgencia['baixa'])
    regra3 = ctrl.Rule(impacto['baixo'] & explorabilidade['alta'], urgencia['media'])
    
    # Bloco 2: Impacto Médio
    regra4 = ctrl.Rule(impacto['medio'] & explorabilidade['baixa'], urgencia['media'])
    regra5 = ctrl.Rule(impacto['medio'] & explorabilidade['moderada'], urgencia['alta'])
    regra6 = ctrl.Rule(impacto['medio'] & explorabilidade['alta'], urgencia['alta'])
    
    # Bloco 3: Impacto Alto (Risco Crítico Garante Resposta Máxima)
    regra7 = ctrl.Rule(impacto['alto'] & explorabilidade['baixa'], urgencia['critica'])
    regra8 = ctrl.Rule(impacto['alto'] & explorabilidade['moderada'], urgencia['critica'])
    regra9 = ctrl.Rule(impacto['alto'] & explorabilidade['alta'], urgencia['critica'])

    # Agrupa as 9 regras no Sistema de Controle
    sistema_controle = ctrl.ControlSystem([
        regra1, regra2, regra3, 
        regra4, regra5, regra6, 
        regra7, regra8, regra9
    ])
    
    # Retorna o Simulador pronto para inferência ponta a ponta
    return ctrl.ControlSystemSimulation(sistema_controle)


def gerar_superficie_3d(simulador):
    """
    Varre todo o espaço de busca (Grid 20x20) calculando a saída de urgência
    para renderizar a Superfície de Decisão 3D em formato PNG.
    """
    # Garante que o diretório de resultados exista
    Path("results").mkdir(exist_ok=True)
    
    # Cria uma malha/grid numérica 20x20 cobrindo todo o universo do discurso
    # x = Impacto (0 a 100), y = Explorabilidade (0 a 10)
    x, y = np.meshgrid(np.linspace(0, 100, 20), np.linspace(0, 10, 20))
    z = np.zeros_like(x)

    # Itera sobre cada ponto do grid computando a inferência fuzzy
    for i in range(20):
        for j in range(20):
            simulador.input['impacto'] = x[i, j]
            simulador.input['explorabilidade'] = y[i, j]
            simulador.compute()
            z[i, j] = simulador.output['urgencia']

    # Configuração da figura e do eixo tridimensional 3D
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plota a superfície contínua com mapa de cores 'viridis'
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', alpha=0.9)
    
    # Personalização de títulos e eixos
    ax.set_xlabel('Impacto no Negócio (%)')
    ax.set_ylabel('Explorabilidade (0-10)')
    ax.set_zlabel('Urgência Calculada (%)')
    plt.title('Superfície de Decisão Fuzzy — SOC Autônomo')
    
    # Barra de cores lateral
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.savefig('results/superficie_decisao.png')
    plt.close()
    print("Sucesso: Imagem 'results/superficie_decisao.png' gerada com êxito!")


def simular_casos_teste(simulador):
    """
    Executa testes rápidos no console para validar a saída do sistema.
    """
    casos = [
        ("Mínimo Absoluto", 0.0, 0.0),
        ("Baixo Impacto + Alta Explorabilidade (Transição)", 10.0, 9.0),
        ("Médio Impacto + Moderado", 50.0, 5.0),
        ("Máximo Absoluto", 100.0, 10.0)
    ]
    
    print("\n=== SIMULAÇÕES DE TESTE DE INFERÊNCIA ===")
    for nome, imp, exp in casos:
        simulador.input['impacto'] = imp
        simulador.input['explorabilidade'] = exp
        simulador.compute()
        res = simulador.output['urgencia']
        print(f"[{nome}] -> Imp: {imp}% | Exp: {exp} => Urgência: {res:.2f}%")


if __name__ == "__main__":
    sim = construir_motor_inferencia()
    simular_casos_teste(sim)
    gerar_superficie_3d(sim)
