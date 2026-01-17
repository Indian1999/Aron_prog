import os
path = os.path.join(os.path.dirname(__file__), "telefonok-adatok.txt")
telefonok = []
with open(path, "r", encoding = "utf-8") as f:
    sor = f.readline()
    for line in f:
        sor = line.strip().split(";") #["Redmi Note 12 Pro","Xiaom","80000","2023","igen"]
        adatok = {
            "modell": sor[0],
            "gyarto": sor[1],
            "ar": int(sor[2]),
            "ev": int(sor[3])
        }
        if sor[4] == "igen":
            adatok["5g"] = True
        else:
            adatok["5g"] = False
        telefonok.append(adatok)


# 1. feladat
összeg = 0
for i in telefonok:
    összeg += i["ar"]

atlag = összeg / len(telefonok)
print(f"A telefonok átlagára {round(atlag)} Ft")
    
# 2. feladat (gyártó, név, ár)
max_index = 0
for i in range(len(telefonok)):
    if telefonok[i]["ar"] > telefonok[max_index]["ar"]:
        max_index = i

print(f"A legdrágább telefon adatai: Gyártó: {telefonok[max_index]['gyarto']} Modell: {telefonok[max_index]['modell']} Ár: {telefonok[max_index]['ar']}")

# 3. feladat: Van-e adott gyártónak 5g képes telefonja?
gyarto = input("Add meg egy gyártó nevét: ")
van_5g = False
for i in range(len(telefonok)):
    if telefonok[i]["5g"] == True and telefonok[i]["gyarto"] == gyarto:
        van_5g = True
        break

if van_5g:
    print("Ennek a gyártónak van 5G képes telefonja.")
else:
    print("Ennek a gyártónak nincs 5G képes telefonja.")