operation = input().lower()

matrix = [[float(input()) for i in range(0, 12)] for j in range(0 , 12)]

cur = [matrix[i][:(5 - (i % 6)) if i > 5 else i] for i in range(0, 12)]

newlist = []

for x in cur:
    newlist.extend(x)

sumAll = sum(newlist)

print("%.1f" % (sumAll if operation == "s" else (sumAll / len(newlist))))