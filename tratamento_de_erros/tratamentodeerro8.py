try:
    dados = {
        "Yago": "20 anos",
        "Anna luiza": "21 anos",
        "João": "22 anos",
        "Lucas": "23 anos"
}
    nome = input("Digite um nome:")
    print(dados[nome])

except KeyError:
    print("O nome digitado não foi encontrado!")