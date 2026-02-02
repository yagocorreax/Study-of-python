from pydantic import BaseModel, Field, field_validator, ValidationError

class my_model(BaseModel):
    nomes: list[str] = Field(..., min_length = 1)

    @field_validator('nomes')
    @classmethod

    def lista_não_vazia(cls, v: list[str]):
        if len(v) == 0:
            raise ValueError("A lista não pode estar vazia, envie pelo menos um item.")
        return v
    
    #SCRIPT TESTE
def executar_teste(dados):
    try:
        modelo = my_model(**dados)
        print(f"✅ Sucesso! Dados validados: {modelo.nomes}")
    except ValidationError as e:
        # Aqui pegamos apenas a mensagem de erro que definimos
        mensagem_erro = e.errors()[0]['msg']
        print(f"❌ Erro de Validação: {mensagem_erro}")

print("Teste 1: Enviando lista com dados")
executar_teste({"nomes": ["Alice", "Bob"]})

print("\nTeste 2: Enviando lista vazia")
executar_teste({"nomes": []})

print("\nTeste 3: Enviando campo ausente")
executar_teste({})

