distancia_metros = float(input("Digite uma distância em metros:"))
km = distancia_metros / 1000
hm = distancia_metros / 100
dam = distancia_metros / 10
dm = distancia_metros * 10
cm = distancia_metros * 100
mm = distancia_metros * 1000
print(f"A distância de {distancia_metros} corresponde a:")
print(f"{km} km")
print(f"{hm} hm")
print(f"{dam} dam")
print(f"{dm} dm")
print(f"{cm} cm")
print(f"{mm} mm")