# SpaceHealth — Alocação de Atendimentos com Programação Dinâmica

Módulo de **Dynamic Programming com Python** do projeto de telemedicina para regiões remotas.

## O problema
Um plantão tem **tempo de médico limitado**. Cada paciente tem um custo (tempo de
atendimento) e um valor (score de risco). Queremos escolher o conjunto de pacientes
que **maximiza o valor clínico atendido sem estourar o tempo** — o clássico
**Knapsack 0/1**, resolvido com programação dinâmica.

## Por que DP e não só uma fila de prioridade?
A fila (guloso) atende o mais grave primeiro, mas pode ser subótima quando os
tempos variam. A DP encontra o **ótimo global**. O `main.py` mostra os dois lado a
lado — a DP iguala ou supera o guloso (verificado em `tests/`).

## Estrutura
| Arquivo | Responsabilidade |
|---|---|
| `models.py` | Dataclasses: `Paciente`, `SinalVital`, `Alerta` |
| `risco.py` | `verificar_sinais`, `calcular_risco`, `gerar_alerta` |
| `triagem.py` | `priorizar_fila` (heapq) e baseline guloso |
| `alocacao.py` | **Núcleo DP**: `alocar_atendimentos` (knapsack 0/1) |
| `dados.py` | Gera 32 pacientes (seed fixa, reproduzível) |
| `main.py` | Demo do fluxo completo + comparativo guloso × DP |
| `tests/` | Garante que a DP nunca perde para o guloso |

## Como rodar
```bash
python main.py            # demo completa
python tests/test_alocacao.py   # testes
```
## A recorrência (resumo)
`dp[i][c]` = melhor valor usando os primeiros `i` pacientes com capacidade `c`:
```
dp[i][c] = max(
    dp[i-1][c],                          # não atender o paciente i
    valor_i + dp[i-1][c - tempo_i]       # atender (se couber)
)
```
Complexidade: `O(n * capacidade)`.