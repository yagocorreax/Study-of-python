try:
    nomes = ["Anna luiza", "Yago", "João"]
    indice = int(input("Digite um índice por favor:"))
    print(nomes[indice])

except ValueError:
    print("Digite apenas números para o índice!")

except IndexError:
    print("O índice digitado não se encontra na lista!")