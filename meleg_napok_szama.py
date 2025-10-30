elso_sor = input() # "7 30"
elso_sor = elso_sor.split(" ") # ["7", "30"]

n = int(elso_sor[0])
k = int(elso_sor[1])

lista = []
for i in range(n):
    szam = int(input())
    lista.append(szam)

szamlalo = 0
for i in range(len(lista)):
    if lista[i] > k:
        szamlalo += 1

print(szamlalo)

