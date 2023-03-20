n = int(input())

for i in range(n):
    A, B, G1, G2 = [float(x) for x in input().split(" ")]
    
    i = 0
    while A <= B:
        A += int(A * G1 / 100)
        B += int(B * G2 / 100)
        
        i+=1
        if(i > 100):
            break
    print("Mais de 1 seculo." if i > 100 else (f"{i} anos."))