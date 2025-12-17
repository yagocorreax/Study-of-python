# -*- coding: utf-8 -*-

"""
Exercício 1: Soma de Dois Números

Descrição:
Complete a função 'soma' para que ela retorne a soma de dois números, 'a' e 'b'.

Exemplo:
soma(2, 3) == 5
soma(-1, 1) == 0
"""

def soma(a, b):
    """
    Esta função deve retornar a soma dos números 'a' e 'b'.
    """
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
# Você não precisa modificar o código abaixo.
# Ele verifica se a sua função está funcionando corretamente.

def test_soma():
    assert soma(2, 3) == 5, f"Esperado: 5, Obtido: {soma(2, 3)}"
    assert soma(-1, 1) == 0, f"Esperado: 0, Obtido: {soma(-1, 1)}"
    assert soma(0, 0) == 0, f"Esperado: 0, Obtido: {soma(0, 0)}"
    assert soma(10, -5) == 5, f"Esperado: 5, Obtido: {soma(10, -5)}"
    print("Todos os testes para 'soma' passaram!")

if __name__ == "__main__":
    test_soma()

# Resultado esperado:
# Todos os testes para 'soma' passaram!
