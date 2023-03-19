n = int(input())

for i in range(n):
    j = int(input())
    
    if j == 0:
        print("NULL")
    else:
        print("EVEN" if j % 2 == 0 else "ODD", "POSITIVE" if j > 0 else "NEGATIVE")
    