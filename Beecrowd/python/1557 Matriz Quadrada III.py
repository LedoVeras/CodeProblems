def getValue(j,i):
    return 2 ** (j + i)

while True:
    size = int(input())
    if(size == 0): break
    
    T = len(str(2 ** (size * 2 - 2))) + 1
    
    matrix = [[str(getValue(j,i)) for j in range(0, size)] for i in range(0 , size)]

    for i in matrix:
        t = 1
        for j in i:
            print(((T - len(j) - t) * " ") + j, end="")
            t = 0
        print("")
    print("")