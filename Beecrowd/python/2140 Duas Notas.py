while True:   
    NOTES = [2,5,10,20,50,100]

    X, Y = [int(x) for x in input().split(" ")]

    if(X == Y == 0):
        break

    troco = Y - X

    for i in range(2):
        try:
            troco -= list(filter(lambda a : a <= troco, NOTES))[-1]
        except IndexError:
            troco = 1
            break
        
    print("possible" if troco == 0 else "impossible")