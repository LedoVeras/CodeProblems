while True:     
    try: 
        ct = int(input())
    except EOFError as e:
        break
    
    ma = max([int(x) for x in input().split(" ")])
    
    ni = 3 if ma >= 20 else (2 if ma >= 10 else 1)
    
    print(ni)  