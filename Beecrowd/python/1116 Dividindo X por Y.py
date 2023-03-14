n = int(input())

for i in range(n):
    X, Y = [int(x) for x in input().split(" ")]
    
    print("divisao impossivel" if Y == 0 else "%.1f" % (X / Y))