column = int(input())
operation = input().lower()

matrix = [[float(input()) for i in range(0, 12)] for j in range(0 , 12)]

cur = [matrix[i][column] for i in range(0, 12)]

sumAll = sum(cur)

print("%.1f" % (sumAll if operation == "s" else (sumAll / 12)))
#