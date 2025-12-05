cigarros = int(input("Digite quantos cigarros você fuma por dia:"))
anos = int(input("Digite a quantos anos você fuma:"))
perda = 10 * 365 * cigarros * anos
dias_perdidos = perda / 1440
print(f"você perdeu {dias_perdidos} de vida")