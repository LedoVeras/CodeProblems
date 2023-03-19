sal = float(input())

sal = max(0, sal - 2000)

if(sal != 0):
    inpost = 0

    inpost += min(1000, sal) * 0.08

    sal = max(0, sal - 1000)
    inpost += min(1500, sal) * 0.18
    
    sal = max(0, sal - 1500)
    inpost += sal * 0.28
    
    print("R$ " + "%.2f" % inpost)
else:
    print("Insento")
    