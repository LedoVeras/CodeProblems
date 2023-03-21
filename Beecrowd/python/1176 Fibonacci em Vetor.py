numbList = [int(input()) for x in range(int(input()))]

fib = []

pre = 0
cur = 1

for i in range(max(numbList) + 1):
    fib.append(pre)
    
    ne = cur + pre
    pre = cur
    cur = ne

for i in numbList:
    print(f"Fib({i}) = {fib[i]}")
    