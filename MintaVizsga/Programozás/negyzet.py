a = int(input("Adj meg egy egész számot: "))

print("#" * a)
for i in range(a-2):
    print("#" + " " * (a-2) + "#")

if a != 1:
    print("#" * a)