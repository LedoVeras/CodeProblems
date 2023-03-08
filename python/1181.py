line = int(input())
operation = input().lower()

matrix = [[float(input()) for i in range(0, 12)] for j in range(0 , 12)]

cur = matrix[line]
sumAll = sum(cur)

if operation == "s":
    print("%.1f" % sumAll)
else:
    media = sumAll / 12
    print("%.1f" % media)