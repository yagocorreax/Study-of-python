try:
    number = float(input("Digite um número:"))

except ValueError:
    print("valor inválido!")

else:
    print("valor convertido com sucesso!")

finally:
    print("programa finalizado!")
                   