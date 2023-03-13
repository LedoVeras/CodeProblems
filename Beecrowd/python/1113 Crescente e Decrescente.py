while True:
    X, Y = [float(x) for x in input().split(" ")]
    
    if(X == Y):
        break
    elif(X > Y):
        print("Decrescente")
    else:
        print("Crescente")
        