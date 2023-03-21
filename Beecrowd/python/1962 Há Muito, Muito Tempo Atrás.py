YEAR = 2015

n = int(input())

for i in range(n):
    ye = int(input())
    
    dif = YEAR - ye
    dc = dif > 0
    
    print(abs(dif) + (0 if dc else 1), "D.C." if dc else "A.C.")