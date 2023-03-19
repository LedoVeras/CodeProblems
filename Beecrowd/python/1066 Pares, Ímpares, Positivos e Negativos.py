po = ne = pa = 0

for i in range(5):
    n = int(input())
    
    if(n > 0):
        po += 1
    elif(n < 0):
        ne += 1
    
    if(n % 2 == 0):
        pa += 1

print(f"""{pa} valor(es) par(es)
{5 - pa} valor(es) impar(es)
{po} valor(es) positivo(s)
{ne} valor(es) negativo(s)\n""")