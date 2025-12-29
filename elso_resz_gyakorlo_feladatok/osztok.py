# Írj egy prgramot, amely bekér egy pozitív egész számot.
# a, és kiírja a szám összes osztóját
a = int(input("Adj meg egy számot: "))

for i in range(1, a+1):
    if a % i == 0:
        print(i, end = " ")
print()

# Tökéletes szám: Az osztóinak az összege (önmagát kivéve) egyenlő a számmal
# pl.: 6 egy tökéletes szám, mert 1 + 2 + 3 = 6

# Írj egy programot ami 10000-nél kisebb tökéletes számokat keres
print("Tökéletes számok:")
for i in range(1, 10000):
    osztó_összeg = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            osztó_összeg += j
    if i == osztó_összeg:
        print(i)
    