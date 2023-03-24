import math

n = int(input())

div = n / math.log1p(n - 1)

maxi = 1.25506 * div

print("%.1f" % div, "%.1f" % maxi)
