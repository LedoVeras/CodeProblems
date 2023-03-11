
caso = 0

while True:
    try: 
        n = int(input())
    except EOFError as e:
        break
    
    caso += 1
    
    if(n == 0):
        print(f"Caso {caso}: 1 numero\n0\n")
        continue
        
    seq = "0 "
    numb = 1
    
    for i in range(n):
        nu = i + 1
        numb += nu
        seq += (str(nu) + " ") * nu
        
    print(f"Caso {caso}: {numb} numeros\n{seq[0:-1]}\n")