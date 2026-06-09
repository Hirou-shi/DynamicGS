import heapq
from models import Paciente

def priorizar_fila(pacientes: list[Paciente]) -> list[Paciente]:
    heap: list[tuple[int, int, Paciente]] = []
    for x in pacientes:
        heapq.heappush(heap, (-x.score_risco, x.id, x))
    
    ordenados: list[Paciente] = []
    while heap:
        _, _, paciente = heapq.heappop(heap)
        ordenados.append(paciente)
    
    """Retorna uma lista ordenada por gravidade, pelo score

    heapq é um min-heap (menor no topo). Como queremos o maior no topo
    colocamos o score negativo. O 'id' entra como desempate para evitar
    comparar objetos Pacientes diretamente
    """

    return ordenados

def atender_guloso(pacientes: list[Paciente], capacidade: int) -> tuple[list[Paciente], int]:
    fila = priorizar_fila(pacientes)
    tempo_usado = 0
    atendidos: list[Paciente]  = []

    for x in fila:
        if tempo_usado + x.tempo_atendimento <= capacidade:
            atendidos.append(x)
            tempo_usado += x.tempo_atendimento

    valor_total = sum(x.score_risco for x in atendidos)

    """Baseline guloso que compara com a DP:
    percorre fila de prioridade e atende enquanto tem tempo.

    retorna: pacientes atendidos e valor total
    """

    return atendidos, valor_total
