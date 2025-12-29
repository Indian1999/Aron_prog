a = int(input())
összeg = 0
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
    összeg += a*i
print("A szorzatok összege:", összeg)