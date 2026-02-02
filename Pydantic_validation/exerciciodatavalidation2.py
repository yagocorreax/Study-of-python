from pydantic import BaseModel, Field, model_validator
from datetime import datetime

class Evento(basemodel):
    titulo: str
    data_inicio: datetime
    data_fim: datetime

    @model_validator(mode = 'after')
    def intervalo_datas(self) -> 'Evento':
        if self.data_inicio >= self.data_fim:
            raise ValueError("A data de ínicio deve ser anterior a data de término")
        return self
    
    #SCRIPT TESTE
    def testar_evento():
        print("--- Teste 1: Datas Corretas ---")
    try:
        ev1 = Evento(
            titulo="Workshop Python",
            data_inicio=datetime(2023, 10, 1, 10, 0),
            data_fim=datetime(2023, 10, 1, 18, 0)
        )
        print(f"✅ Sucesso: {ev1.titulo} criado.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    print("\n--- Teste 2: Data Início após Fim ---")
    try:
        ev2 = Evento(
            titulo="Festa de Ano Novo",
            data_inicio=datetime(2024, 1, 1, 0, 0),
            data_fim=datetime(2023, 12, 31, 23, 59) # Erro aqui
        )
    except ValueError as e:
        print(f"✅ Erro capturado corretamente: {e}")

    testar_evento()