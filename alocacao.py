"""
alocacao.py  —  Núcleo de Programação Dinâmica
================================================

PROBLEMA: Mochila 0/1 (0/1 Knapsack)
  Plantão com tempo limitado de médico (ex.: 240 min). Cada paciente
  custa um tempo de atendimento e tem um valor (score de risco).
  Objetivo: escolher o SUBCONJUNTO de pacientes que MAXIMIZA o valor
  total sem estourar o tempo.

  Mapeamento:
    peso       = tempo_atendimento (min)
    valor      = score_risco
    capacidade = tempo do plantão
    0/1        = atende (1) ou não (0), nunca fração.

POR QUE DP, E NÃO GULOSO?
  "Atender o mais grave primeiro" pode desperdiçar tempo: um caso
  gravíssimo que consome o plantão inteiro pode valer menos que vários
  casos graves que cabem juntos. A DP acha o ÓTIMO GLOBAL.

RECORRÊNCIA:
  dp[i][c] = melhor valor com os i primeiros pacientes e capacidade c.
  Para cada paciente i:
    (a) não atende -> dp[i-1][c]
    (b) atende     -> valor_i + dp[i-1][c - tempo_i]   (se couber)
  dp[i][c] = max(a, b). Tabela bottom-up; ao final, reconstrói quais
  pacientes entraram.

  Complexidade: O(n * capacidade) — tempo e memória (pseudo-polinomial).
"""

from models import Paciente

def alocar_atendimentos( pacientes: list[Paciente], capacidade: int) -> tuple[list[Paciente], int]:
    n = len(pacientes)
    dp = [[0] * (capacidade + 1) for _ in range(n+1)]

    for i in range(1, n + 1):
        paciente = pacientes[ i - 1 ]
        custo = paciente.tempo_atendimento
        valor = paciente.score_risco

        for c in range(capacidade + 1):
            sem_paciente = dp[ i - 1 ][c]

            if custo <= c:
                com_paciente = valor + dp[ i - 1 ][ c - custo ]
                dp[i][c] = max(sem_paciente, com_paciente)
            else:
                dp[i][c] = sem_paciente

    valor_total = dp[n][capacidade]

    escolhidos: list[Paciente] = []
    c = capacidade
    for i in range(n, 0, -1):
        if dp[i][c] != dp[ i - 1 ][c]:
            paciente = pacientes[ i - 1 ]
            escolhidos.append(paciente)
            c -= paciente.tempo_atendimento

    escolhidos.reverse()
    return escolhidos, valor_total