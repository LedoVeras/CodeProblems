n = int(input())

for i in range(n):
    X, Y, Z = [float(x) for x in input().split(" ")]
    
    me = (X * 2 + Y * 3 + Z * 5) / 10
    print("%.1f" % me)
