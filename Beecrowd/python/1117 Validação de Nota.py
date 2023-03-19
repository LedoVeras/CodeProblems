no = 0

i = 0
while i < 2:
    n = float(input())
    
    if(n >= 0 and n <= 10):
        i += 1
        no += n
        continue
        
    print("nota invalida")
print("media =", "%.2f" % (no / 2))
        
