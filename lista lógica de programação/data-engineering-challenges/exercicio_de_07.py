# -*- coding: utf-8 -*-

"""
Exercício 7: Juntar Dicionários

Descrição:
Complete a função 'juntar_dicionarios' para que ela junte dois dicionários em um novo.
Se houver chaves duplicadas, os valores do segundo dicionário devem prevalecer.

Exemplo:
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
juntar_dicionarios(d1, d2) == {'a': 1, 'b': 3, 'c': 4}
"""

def juntar_dicionarios(d1, d2):
    """
    Esta função deve juntar os dicionários d1 e d2.
    """
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
def test_juntar_dicionarios():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    resultado = {'a': 1, 'b': 3, 'c': 4}
    assert juntar_dicionarios(d1, d2) == resultado, f"Esperado: {resultado}, Obtido: {juntar_dicionarios(d1, d2)}"

    d3 = {'nome': 'Carlos'}
    d4 = {'idade': 25}
    resultado2 = {'nome': 'Carlos', 'idade': 25}
    assert juntar_dicionarios(d3, d4) == resultado2, f"Esperado: {resultado2}, Obtido: {juntar_dicionarios(d3, d4)}"

    d5 = {}
    d6 = {'x': 10, 'y': 20}
    resultado3 = {'x': 10, 'y': 20}
    assert juntar_dicionarios(d5, d6) == resultado3, f"Esperado: {resultado3}, Obtido: {juntar_dicionarios(d5, d6)}"
    print("Todos os testes para 'juntar_dicionarios' passaram!")

if __name__ == "__main__":
    test_juntar_dicionarios()

# Resultado esperado:
# Todos os testes para 'juntar_dicionarios' passaram!
