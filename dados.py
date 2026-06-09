"""
dados.py
--------
Gera a base de pacientes (atende o requisito de "30+ informações" do doc).
Usamos uma seed fixa para que os resultados sejam reproduzíveis em toda
execução — importante para apresentar o trabalho sempre igual.
"""

import random
from models import Paciente, SinalVital

REGIOES = ["Amazonas", "Para", "Acre", "Roraima", "Ribeirinha-RJ", "Rural-MG"]
NOMES = [
    "Ana", "Bruno", "Carla", "Diego", "Elaine", "Fabio", "Gisele", "Hugo",
    "Iara", "Joao", "Kelly", "Lucas", "Marta", "Nelson", "Olivia", "Paulo",
    "Quezia", "Rafael", "Sonia", "Tiago", "Ursula", "Vitor", "Wanda", "Xavier",
    "Yara", "Zeca", "Bia", "Caio", "Dora", "Edu", "Fernanda", "Gabriel",
]


def gerar_pacientes(n: int = 32, seed: int = 42) -> list[Paciente]:
    random.seed(seed)
    pacientes: list[Paciente] = []

    for i in range(n):
        sinais = SinalVital(
            temperatura=round(random.uniform(36.0, 40.5), 1),
            spo2=random.randint(82, 99),
            freq_cardiaca=random.randint(60, 150),
        )
        paciente = Paciente(
            id=i + 1,
            nome=NOMES[i % len(NOMES)],
            regiao=random.choice(REGIOES),
            sinais=sinais,
            tempo_atendimento=random.randint(15, 60),  # minutos
        )
        pacientes.append(paciente)

    """Cria n pacientes com sinais vitais aleatórios mas plausíveis."""

    return pacientes
