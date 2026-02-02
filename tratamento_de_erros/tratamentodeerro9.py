while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print("Número digitado:", numero)
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

