while(True):
    numbList = [float(x) for x in input().split(" ")]
    
    if(numbList[0] == 0):
        break
    
    A, B, C = numbList
    
    area = A * B
    allowed = area / (C / 100)
    side = int(allowed ** 0.5)
    
    print(side)
    