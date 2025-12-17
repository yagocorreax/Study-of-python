# -*- coding: utf-8 -*-

"""
Exercício 5: Verificar Chave em Dicionário

Descrição:
Complete a função 'chave_existe' que verifica se uma determinada chave existe em um dicionário.
A função deve retornar True se a chave existir e False caso contrário.

Exemplo:
chave_existe({'a': 1, 'b': 2}, 'a') == True
chave_existe({'a': 1, 'b': 2}, 'c') == False
"""

def chave_existe(dicionario, chave):
    """
    Esta função deve verificar se 'chave' existe no 'dicionario'.
    """
    # Escreva o seu código aqui
    pass

# --- Testes Unitários ---
def test_chave_existe():
    d = {'nome': 'Alice', 'idade': 30}
    assert chave_existe(d, 'nome') == True, f"Esperado: True, Obtido: {chave_existe(d, 'nome')}"
    assert chave_existe(d, 'cidade') == False, f"Esperado: False, Obtido: {chave_existe(d, 'cidade')}"
    assert chave_existe({}, 'qualquer') == False, f"Esperado: False, Obtido: {chave_existe({}, 'qualquer')}"
    print("Todos os testes para 'chave_existe' passaram!")

if __name__ == "__main__":
    test_chave_existe()

# Resultado esperado:
# Todos os testes para 'chave_existe' passaram!
