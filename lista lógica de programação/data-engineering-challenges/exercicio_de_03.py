# -*- coding: utf-8 -*-

"""
Exercício 3: Maior Número em uma Lista

Descrição:
Complete a função 'encontrar_maior_numero' para que ela retorne o maior número de uma lista.
Se a lista estiver vazia, a função deve retornar None.

Exemplo:
encontrar_maior_numero([1, 2, 3, 4, 5]) == 5
encontrar_maior_numero([-1, -5, -3]) == -1
encontrar_maior_numero([]) == None
"""

def encontrar_maior_numero(numeros):
    """
    Esta função deve encontrar e retornar o maior número na lista 'numeros'.
    """
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
def test_encontrar_maior_numero():
    assert encontrar_maior_numero([1, 2, 3, 4, 5]) == 5, f"Esperado: 5, Obtido: {encontrar_maior_numero([1, 2, 3, 4, 5])}"
    assert encontrar_maior_numero([-1, -5, -3]) == -1, f"Esperado: -1, Obtido: {encontrar_maior_numero([-1, -5, -3])}"
    assert encontrar_maior_numero([10, 5, 8, 12, 3]) == 12, f"Esperado: 12, Obtido: {encontrar_maior_numero([10, 5, 8, 12, 3])}"
    assert encontrar_maior_numero([]) == None, f"Esperado: None, Obtido: {encontrar_maior_numero([])}"
    print("Todos os testes para 'encontrar_maior_numero' passaram!")

if __name__ == "__main__":
    test_encontrar_maior_numero()

# Resultado esperado:
# Todos os testes para 'encontrar_maior_numero' passaram!
