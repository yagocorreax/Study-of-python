# -*- coding: utf-8 -*-

"""
Exercício 8: Tratamento de Erro - Divisão por Zero

Descrição:
Complete a função 'dividir' para que ela realize a divisão de 'a' por 'b'.
A função deve tratar o erro 'ZeroDivisionError' que ocorre ao tentar dividir por zero.
Se a divisão por zero ocorrer, a função deve retornar a string "Erro: Divisão por zero não é permitida".

Exemplo:
dividir(10, 2) == 5.0
dividir(10, 0) == "Erro: Divisão por zero não é permitida"
"""

def dividir(a, b):
    """
    Esta função deve dividir 'a' por 'b' e tratar a divisão por zero.
    """
    # Dica: use um bloco try...except ZeroDivisionError
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
def test_dividir():
    assert dividir(10, 2) == 5.0, f"Esperado: 5.0, Obtido: {dividir(10, 2)}"
    assert dividir(10, 0) == "Erro: Divisão por zero não é permitida", f"Esperado: 'Erro: Divisão por zero não é permitida', Obtido: {dividir(10, 0)}"
    assert dividir(0, 5) == 0.0, f"Esperado: 0.0, Obtido: {dividir(0, 5)}"
    print("Todos os testes para 'dividir' passaram!")

if __name__ == "__main__":
    test_dividir()

# Resultado esperado:
# Todos os testes para 'dividir' passaram!
