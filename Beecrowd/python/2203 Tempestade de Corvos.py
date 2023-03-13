import math

while True:
    try: 
        n = [int(x) for x in input().split(" ")]
    except EOFError as e:
        break
        
    X1, Y1, X2, Y2, V, R1, R2 = n

    t = [X2 - X1, Y2 - Y1]
    s = sum(map(abs, t))    
    
    try: 
        dir = list(map(lambda i : i / s, t))
    except ZeroDivisionError as e:
        dir = [0,0]
        
    X2 += dir[0] * 1.5 * V
    Y2 += dir[1] * 1.5 * V
    
    dist1 = ((X1 - X2) ** 2 + (Y1 - Y2) ** 2)  ** 0.5

    if(dist1 <= R1):
        point = [X2, Y2]
    else:
        dirR = math.atan2(dir[1], dir[0])
        point = [math.cos(dirR) * R1 + X1, math.sin(dirR) * R1 + Y1]

    dist2 = ((point[0] - X2) ** 2 + (point[1] - Y2) ** 2)  ** 0.5
    
    print("Y" if dist2 <= R2 else "N")