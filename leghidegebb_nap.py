n = int(input())

lista = []
for i in range(n):
    szam = int(input())
    lista.append(szam)

min_index = 0
for i in range(1, len(lista)):
    if lista[i] < lista[min_index]:
        min_index = i

print(lista[min_index])