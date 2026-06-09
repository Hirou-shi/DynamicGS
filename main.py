"""
main.py
-------
Demonstração do fluxo completo:

  1. Carrega os pacientes (dados.py)
  2. Calcula risco e gera alertas (risco.py)
  3. Mostra a fila de triagem            -> GULOSO (triagem.py)
  4. Resolve a alocacao otima            -> DP / knapsack (alocacao.py)
  5. COMPARA guloso x DP com a mesma capacidade

O passo 5 é o argumento central: com o mesmo tempo de plantao, a DP
costuma atender pacientes de MAIOR valor total que o guloso.
"""

from dados import gerar_pacientes
from risco import calcular_risco, gerar_alerta
from triagem import priorizar_fila, atender_guloso
from alocacao import alocar_atendimentos

CAPACIDADE_PLANTAO = 240   

def main() -> None:
    pacientes = gerar_pacientes()

    # 2. Risco + alertas
    alertas = []
    for p in pacientes:
        calcular_risco(p)              
        alerta = gerar_alerta(p)
        if alerta:
            alertas.append(alerta)

    print(f"Total de pacientes: {len(pacientes)}")
    print(f"Alertas gerados:    {len(alertas)}\n")

    # 3. Triagem (guloso) — top 5 mais graves
    fila = priorizar_fila(pacientes)
    print("=== TRIAGEM (5 mais graves) ===")
    for p in fila[:5]:
        print(f"  #{p.id:>2} {p.nome:<9} risco={p.score_risco:>3} "
              f"| {p.tempo_atendimento:>2}min | SpO2 {p.sinais.spo2}%")

    # 4 e 5. Comparacao GULOSO x DP
    g_atendidos, g_valor = atender_guloso(pacientes, CAPACIDADE_PLANTAO)
    d_atendidos, d_valor = alocar_atendimentos(pacientes, CAPACIDADE_PLANTAO)

    print(f"\n=== COMPARATIVO (capacidade = {CAPACIDADE_PLANTAO} min) ===")
    print(f"  GULOSO : {len(g_atendidos):>2} pacientes | valor total = {g_valor}")
    print(f"  DP     : {len(d_atendidos):>2} pacientes | valor total = {d_valor}")

    ganho = d_valor - g_valor
    if ganho > 0:
        print(f"\n  -> A DP atendeu {ganho} pontos de risco A MAIS com o mesmo tempo.")
    elif ganho == 0:
        print("\n  -> Empate neste cenario (acontece quando o guloso ja era otimo).")
    print("     Mude a seed/capacidade para ver a diferenca variar.")


if __name__ == "__main__":
    main()
