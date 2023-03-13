n = int(input())

h5 = (5 ** 0.5)
result = ((0.5 + h5/2) ** n - (0.5 - h5/2) ** n) / h5
print("%.1f" % result)