def getValue(j, i):
    return abs(j - i)

while True:
    size = int(input())
    if(size == 0): break
    
    matrix = [[str(getValue(j, i) + 1) for j in range(0, size)] for i in range(0 , size)]

    for i in matrix:
        t = 1
        for j in i:
            print(((4 - len(j) - t) * " ") + j, end="")
            t = 0
        print("")
    print("")