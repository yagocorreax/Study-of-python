# -*- coding: utf-8 -*-

"""
Exercício 2: Média de uma Lista

Descrição:
Complete a função 'calcular_media' para que ela retorne a média de uma lista de números.
Se a lista estiver vazia, a função deve retornar 0.

Exemplo:
calcular_media([1, 2, 3, 4, 5]) == 3.0
calcular_media([10, 20, 30]) == 20.0
calcular_media([]) == 0
"""

def calcular_media(numeros):
    """
    Esta função deve calcular e retornar a média dos números na lista 'numeros'.
    """
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
def test_calcular_media():
    assert calcular_media([1, 2, 3, 4, 5]) == 3.0, f"Esperado: 3.0, Obtido: {calcular_media([1, 2, 3, 4, 5])}"
    assert calcular_media([10, 20, 30]) == 20.0, f"Esperado: 20.0, Obtido: {calcular_media([10, 20, 30])}"
    assert calcular_media([]) == 0, f"Esperado: 0, Obtido: {calcular_media([])}"
    assert calcular_media([5, 5, 5, 5]) == 5.0, f"Esperado: 5.0, Obtido: {calcular_media([5, 5, 5, 5])}"
    print("Todos os testes para 'calcular_media' passaram!")

if __name__ == "__main__":
    test_calcular_media()

# Resultado esperado:
# Todos os testes para 'calcular_media' passaram!
