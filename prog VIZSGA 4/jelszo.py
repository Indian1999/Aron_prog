jelszo = input("Adj meg egy jelszót: ")

erosseg = 0
if len(jelszo) >= 8:
    erosseg += 1

for char in jelszo:
    if char == "1" or char == "0" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
        erosseg += 1
        break

if erosseg == 0:
    print("Gyenge!")
elif erosseg == 1:
    print("Közepes!")
else:
    print("Erős!")