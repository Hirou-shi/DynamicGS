"""
risco.py
--------
Transforma sinais vitais em informação clínica útil:

  verificar_sinais()  -> aponta QUAIS sinais estão fora do normal
  calcular_risco()    -> resume tudo num score numérico (0 a 100)
  gerar_alerta()      -> dispara um Alerta quando o quadro é grave

Regra de negócio do documento: SpO2 < 90% gera alerta crítico.
"""

from models import Paciente, Alerta

# Faixas de referência (limites simplificados para fins didáticos)
SPO2_CRITICO = 90        # abaixo disso = crítico
FC_ALTA = 120            # taquicardia
FEBRE = 38.0             # °C


def verificar_sinais(paciente: Paciente) -> dict[str, bool]:
    s = paciente.sinais

    """Retorna um dicionário dizendo quais sinais estão alterados.
    Manter isso separado do score facilita testar e exibir no relatório.
    """

    return {
        "oxigenacao_baixa": s.spo2 < SPO2_CRITICO,
        "taquicardia": s.freq_cardiaca > FC_ALTA,
        "febre": s.temperatura >= FEBRE,
    }


def calcular_risco(paciente: Paciente) -> int:
    sinais = verificar_sinais(paciente)
    s = paciente.sinais

    score = 0
    if sinais["oxigenacao_baixa"]:
        score += 40 + (SPO2_CRITICO - s.spo2) * 2  
    if sinais["taquicardia"]:
        score += 25 + (s.freq_cardiaca - FC_ALTA)
    if sinais["febre"]:
        score += 15 + int((s.temperatura - FEBRE) * 5)

    score = max(0, min(score, 100))
    paciente.score_risco = score

    """Converte os sinais num score de 0 a 100. Pesos maiores para o que é
    mais perigoso (oxigenação). Também ESCREVE o resultado no paciente,
    porque a DP vai usar paciente.score_risco como "valor".
    """

    return score


def gerar_alerta(paciente: Paciente) -> Alerta | None:

    sinais = verificar_sinais(paciente)

    if sinais["oxigenacao_baixa"]:
        return Alerta(paciente.id, "CRITICO",
                      f"Oxigenacao {paciente.sinais.spo2}% (< {SPO2_CRITICO}%)")
    if paciente.score_risco >= 60:
        return Alerta(paciente.id, "ALTO",
                      f"Score de risco elevado ({paciente.score_risco})")
    
    """Cria um Alerta se o paciente estiver crítico. Retorna None se estável.
    A regra principal (SpO2 < 90%) vem direto do documento do projeto.
    """

    return None
