ma = -1
idx = 0

for i in range(100):
    j = int(input())
    
    if(j > ma):
        ma = j
        idx = i + 1
        
print(ma, idx, sep="\n")