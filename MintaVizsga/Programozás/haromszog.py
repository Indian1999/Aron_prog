a = int(input("a oldal: "))
b = int(input("b oldal: "))
c = int(input("c oldal: "))

if a+b > c and b+c > a and a+c > b:
    print("Szerkeszthető a háromszög!")
    print("A háromszög kerület:", a+b+c)
else:
    print("Nem szerkeszthető háromszög!")