try:
    number = float(input("Digite um número:"))

except ValueError:
    print("valor inválido!")

else:
    print("Conversão realizada com sucesso!")