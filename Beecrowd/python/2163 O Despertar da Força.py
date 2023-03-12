X, Y = [int(x) for x in input().split(" ")]

matrix = [input().split(" ") for j in range(0 , X)]

toRt = [0,0]

for i in range(1, X - 1):
    lin = matrix[i]
    li = lin.copy()
    t = 0
    while True:
        try:
            ii = li.index("42") + t
        except ValueError:
            break
        
        print(ii, Y - 1)
        if(ii == 0 or ii == Y - 1):
            break
        
        prev = matrix[i - 1]
        ne = matrix[i + 1]
        
        alll = []
        alll.extend([lin[ii - 1] , lin[ii + 1]] + prev[ii-1:ii+2] + ne[ii-1:ii+2])
        
        if all(f == "7" for f in alll):
            toRt = [i + 1, ii + 1]
            break
        
        t+=1
        del li[ii]
    
    if(toRt != [0,0]):
        break
        
print(toRt[0], toRt[1])    
