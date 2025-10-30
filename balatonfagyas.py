n = int(input())

lista = []
for i in range(n):
    szam = int(input())
    lista.append(szam)

szamlalo = 0
for i in range(len(lista)):
    if lista[i] > 0:
        szamlalo += 1

print(szamlalo)