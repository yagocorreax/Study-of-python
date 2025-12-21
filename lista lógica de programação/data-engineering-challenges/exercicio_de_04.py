# -*- coding: utf-8 -*-

"""
Exercício 4: Frequência de Palavras

Descrição:
Complete a função 'contar_frequencia_palavras' para que ela retorne um dicionário
com a contagem de cada palavra em uma frase. A função deve ignorar se as letras
são maiúsculas ou minúsculas e remover pontuações básicas (,.!).

Exemplo:
contar_frequencia_palavras("Isso é um teste. Isso é apenas um teste!") == {'isso': 2, 'é': 2, 'um': 2, 'teste': 2, 'apenas': 1}
"""

import re

def contar_frequencia_palavras(frase):
    """
    Esta função deve contar a frequência de cada palavra na 'frase' e retornar um dicionário.
    """
    # Dica: use frase.lower() para converter para minúsculas
    # Dica: use re.sub(r'[^\w\s]', '', frase) para remover pontuação
    # Escreva o seu código aqui
    import re
    from collections import Counter
    
    frase = frase.lower()
    frase = re.sub(r'[,\.\!]', '', frase)
    palavras = frase.split()

    return Counter(palavras)
    pass

# --- Testes Unitários ---
def test_contar_frequencia_palavras():
    frase1 = "Isso é um teste. Isso é apenas um teste!"
    resultado1 = {'isso': 2, 'é': 2, 'um': 2, 'teste': 2, 'apenas': 1}
    assert contar_frequencia_palavras(frase1) == resultado1, f"Esperado: {resultado1}, Obtido: {contar_frequencia_palavras(frase1)}"

    frase2 = "Python, python, python!"
    resultado2 = {'python': 3}
    assert contar_frequencia_palavras(frase2) == resultado2, f"Esperado: {resultado2}, Obtido: {contar_frequencia_palavras(frase2)}"

    frase3 = ""
    resultado3 = {}
    assert contar_frequencia_palavras(frase3) == resultado3, f"Esperado: {resultado3}, Obtido: {contar_frequencia_palavras(frase3)}"
    print("Todos os testes para 'contar_frequencia_palavras' passaram!")

if __name__ == "__main__":
    test_contar_frequencia_palavras()


# Resultado esperado:
# Todos os testes para 'contar_frequencia_palavras' passaram!
