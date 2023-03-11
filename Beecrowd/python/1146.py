while(True):
    cur = int(input())
    if cur == 0: break
    
    toPr = ""
    
    for i in range(1, cur + 1):
        toPr += str(i) + " "
        
    print(toPr.strip())