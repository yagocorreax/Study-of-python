# -*- coding: utf-8 -*-

"""
Exercício 6: Remover Duplicatas de uma Lista

Descrição:
Complete a função 'remover_duplicatas' para que ela retorne uma nova lista
contendo apenas os elementos únicos da lista original, mantendo a ordem original.

Exemplo:
remover_duplicatas([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
remover_duplicatas(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
"""

def remover_duplicatas(lista):
    """
    Esta função deve remover elementos duplicados de uma lista e retornar uma nova lista.
    """
    # Escreva o seu código aqui
    vistos = set()
    resultado= []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
            
            
    return resultado
    pass

# --- Testes Unitários ---
def test_remover_duplicatas():
    assert remover_duplicatas([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5], f"Esperado: [1, 2, 3, 4, 5], Obtido: {remover_duplicatas([1, 2, 2, 3, 4, 4, 5])}"
    assert remover_duplicatas(['a', 'b', 'a', 'c']) == ['a', 'b', 'c'], f"Esperado: ['a', 'b', 'c'], Obtido: {remover_duplicatas(['a', 'b', 'a', 'c'])}"
    assert remover_duplicatas([]) == [], f"Esperado: [], Obtido: {remover_duplicatas([])}"
    assert remover_duplicatas([1, 1, 1, 1]) == [1], f"Esperado: [1], Obtido: {remover_duplicatas([1, 1, 1, 1])}"
    print("Todos os testes para 'remover_duplicatas' passaram!")

if __name__ == "__main__":
    test_remover_duplicatas()

# Resultado esperado:
# Todos os testes para 'remover_duplicatas' passaram!
