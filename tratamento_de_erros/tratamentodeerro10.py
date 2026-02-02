def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: não é possível dividir por zero."
    except TypeError:
        return "Erro: valores inválidos."
Resultado = dividir(10, 0)
print(Resultado)




