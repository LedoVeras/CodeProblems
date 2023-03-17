while True:
    try: 
        n, l = input().split(" ")
    except EOFError:
        break
    
    total = 0
    for t in range(int(n)):
        i, j = input().split(" ")
        
        if(j == "0" and i == l):
            total += 1

    print(total)