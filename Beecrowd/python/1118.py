while(True):
    
    numb = [0,0]
    
    i = 0
    while(i < 2):
        cur = float(input())
        if(cur < 0 or cur > 10):
            print("nota invalida")
            continue
        
        numb[i] = cur
        i += 1
    
    A , B = numb
    
    media = (A + B) / 2 
    
    print("media = " + str("%.2f" % media))
    stop = False
    
    while(True):
        print("novo calculo (1-sim 2-nao)")
        next = int(input())
        if next == 1:
            break
        elif next == 2:
            stop = True
            break
        else:
            continue
    
    if stop : break