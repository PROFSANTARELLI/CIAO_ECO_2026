import pytest
from sistema_demonstracao import criar_sistema_triagem, calcular_urgencia

@pytest.fixture
def simulador():
    """Instancia o simulador antes de cada teste."""
    return criar_sistema_triagem()

def test_urgencia_para_impacto_baixo(simulador):
    """Testa se impacto baixo (10%) gera urgência baixa (< 30%)."""
    resultado = calcular_urgencia(simulador, 10.0)
    assert resultado < 30.0

def test_urgencia_para_impacto_alto(simulador):
    """Testa se impacto alto (90%) gera urgência alta (> 70%)."""
    resultado = calcular_urgencia(simulador, 90.0)
    assert resultado > 70.0

def test_entrada_invalida_dispara_erro(simulador):
    """Garante que o sistema rejeita valores fora da escala (ex: 150%)."""
    with pytest.raises(ValueError):
        calcular_urgencia(simulador, 150.0)
