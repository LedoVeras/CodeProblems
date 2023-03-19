po = 0
ct = 0

for i in range(6):
    n = float(input())
    if(n > 0):
        po += 1
        ct += n
        
med = (ct / po)  

print(f"""{po} valores positivos
{"%.1f" % med}""")