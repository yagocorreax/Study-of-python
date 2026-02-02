try:
    number1 = float(input("Digite um valor:"))
    number2 = float(input("Digite outro valor:"))
    divisao = number1 / number2
except ZeroDivisionError:
    print("Divisão por zero não é permitida, usuário. Divisão inválida!")
else:
    print(f"Divisão bem sucedida, o resultado é {divisao}")