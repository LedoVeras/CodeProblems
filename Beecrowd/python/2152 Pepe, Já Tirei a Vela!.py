n = int(input())

for i in range(n):
    h, m, o = input().split()
    door = "abriu" if o == "1" else "fechou"
    hour = "0" * (2 - len(h)) + h
    minu = "0" * (2 - len(m)) + m
    print(f"{hour}:{minu} - A porta {door}!")