"""
models.py
---------
Modelos de dados do sistema. Usamos `dataclass` para ter classes limpas,
com type hints, sem precisar escrever __init__ na mão.

Separar os MODELOS da LÓGICA (risco, triagem, alocação) é o que deixa o
projeto com cara profissional: cada arquivo tem uma responsabilidade só.
"""


from dataclasses import dataclass, field

@dataclass
class SinalVital:
    temperatura: float
    spo2: int
    freq_cardiaca: int 

    """Le os sinais vitais de um paciente, 
    Temp em C°, 
    Spo2 (Saturação de Óxigênio em %),   
    Freq_card (Batimentos por minuto)
    """
@dataclass
class Paciente:
    id: int
    nome: str
    regiao: str
    idade: int
    tempo_atendimento: int
    score_risco: int = 0

    """É o paciente atendido remotamente
    Atributo-chave:
     - tempo_atendimento seria peso/ custo no knapsack (minutos de médico)
     - score_risco: o valor no knapsnack (o quão importante é atender agora,
     começo no 0 e é preenchido por calcular_risco().
    """
@dataclass
class Alerta:
    paciente_id: int
    nivel: str
    motivo: str

    """Alerta gerado quando paciente entra em situação critica"""