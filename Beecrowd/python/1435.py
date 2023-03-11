def getValue(i , j, half):
    return 1 + min(int(half - (j % half) - 1) if j >= half else j, int(half - (i % half) - 1) if i >= half else i)

while True:
    size = int(input())
    if(size == 0): break

    ii = 1

    half = size / 2

    matrix = [[str(getValue(i, j, half)) for j in range(0, size)] for i in range(0 , size)]

    for i in matrix:
        t = 1
        for j in i:
            print(((4 - len(j) - t) * " ") + j, end="")
            t = 0
        print("")
    print("")