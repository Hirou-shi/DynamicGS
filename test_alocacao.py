"""
test_alocacao.py
----------------
Teste central do projeto: a DP NUNCA pode dar um valor menor que o guloso,
porque ela encontra o otimo global. Rode com:  python -m pytest
(ou simplesmente: python tests/test_alocacao.py)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dados import gerar_pacientes
from risco import calcular_risco
from triagem import atender_guloso
from alocacao import alocar_atendimentos


def test_dp_nunca_pior_que_guloso():
    for seed in range(10):
        pacientes = gerar_pacientes(n=32, seed=seed)
        for p in pacientes:
            calcular_risco(p)

        _, valor_guloso = atender_guloso(pacientes, capacidade=240)
        _, valor_dp = alocar_atendimentos(pacientes, capacidade=240)

        assert valor_dp >= valor_guloso, (
            f"seed={seed}: DP ({valor_dp}) ficou abaixo do guloso ({valor_guloso})"
        )


def test_respeita_capacidade():
    pacientes = gerar_pacientes(seed=1)
    for p in pacientes:
        calcular_risco(p)
    escolhidos, _ = alocar_atendimentos(pacientes, capacidade=240)
    tempo_total = sum(p.tempo_atendimento for p in escolhidos)
    assert tempo_total <= 240


if __name__ == "__main__":
    test_dp_nunca_pior_que_guloso()
    test_respeita_capacidade()
    print("OK: todos os testes passaram.")
