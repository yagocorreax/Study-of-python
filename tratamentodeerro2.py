try:
    numbe1 = int(input("Digite o primeiro valor:"))
    number2 = int(input("Digite o segundo valor:"))
    soma = (numbe1 + number2)
    print(soma)
except ValueError:
    print("Entrada inválida!")