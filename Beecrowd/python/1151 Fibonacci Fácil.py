n = int(input())

print(0, end="")

pre = 0
cur = 1

for i in range(n - 2):
    
    ne = cur + pre
    pre = cur
    cur = ne
    
    print("", pre, end="")
    
ne = cur + pre
pre = cur

print("", pre)