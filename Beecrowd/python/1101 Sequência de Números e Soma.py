while ...:
    li = [int(x) for x in input().split(" ")]
    li.sort()
    X, Y = li

    if(X <= 0 or Y <= 0):
        break
    
    for i in range(X, Y + 1):
        print(i, end=" ")
        
    print(f"Sum={((X + Y) * (Y - X + 1)) // 2}")
    