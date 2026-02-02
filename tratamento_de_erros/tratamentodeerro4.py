try:
    number1 = float(input("Digite um número:"))
    number2 = float(input("Digite outro número:"))
    divisao = number1 / number2

except ValueError:
    print("Digite um número, usuário! palavras não são permitidas.")
except ZeroDivisionError:
    print("Usuário, divisões por zero não são permitidas!")

else:
    print(f"O resultado é {divisao}")