n, m = [int(x) for x in input().split(" ")]

for i in range(m):
    fe = input() == "fechou"
    
    n += 1 if fe else -1
    
print(n)