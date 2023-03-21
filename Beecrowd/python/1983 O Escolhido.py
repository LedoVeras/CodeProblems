n = int(input())

curMax = [0,0]
for i in range(n):
    X , Y = input().split(" ")
    note = float(Y)
    if(note > curMax[1]):
        curMax = [X, note]

print(curMax[0] if curMax[1] >= 8 else "Minimum note not reached")