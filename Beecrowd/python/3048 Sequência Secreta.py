n = int(input())

cur = "1"
circles = 1
for i in range(n):
    j = input()
    if j != cur:
        circles += 1
        cur = j
        
print(circles)
    