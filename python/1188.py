operation = input().lower()

matrix = [[float(input()) for i in range(0, 12)] for j in range(0 , 12)]

cur = [matrix[i][(12 - i): (i)] for i in range(0, 12)]

newlist = []

for x in cur:
    newlist.extend(x)
    
sumAll = sum(newlist)

print("%.1f" % (sumAll if operation == "s" else (sumAll / len(newlist))))