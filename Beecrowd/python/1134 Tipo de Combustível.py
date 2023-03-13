t = [0,0,0]

while True:
    n = int(input())
    if(n == 4): break
    
    if(n < 4):
        t[n - 1] = t[n - 1] + 1
        
    
print(f"""MUITO OBRIGADO
Alcool: {t[0]}
Gasolina: {t[1]}
Diesel: {t[2]}""")