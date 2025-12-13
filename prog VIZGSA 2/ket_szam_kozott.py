a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))

harom = 0
szöveg = "Az alábbi számokat találtam: "
for i in range(a, b+1):
    if i % 3 == 0:
        harom += 1
    szöveg += str(i)
    if i != b: # Nem az utolsó számot vizsgáljuk
        szöveg += ", "


print(szöveg)
print(harom)