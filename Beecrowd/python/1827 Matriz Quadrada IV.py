
while True:
    try: 
        size = int(input())
    except EOFError as e:
        break
    
    middle = int(size / 2)
    div = int(size / 3)
    oneSize = size - div * 2
    
    for i in range(size):
        
        if i < div:
            lin = ("0" * i) + "2" + ("0" * (size - (2 * (i + 1)))) + "3" + ("0" * i)
        elif i < div + oneSize:
            zeros = "0" * div
            if i == middle:
                half = int(oneSize / 2)
                lin = zeros + "1" * half + "4" + "1" * half + zeros
            else:
                lin = zeros + "1" * oneSize + zeros
        else:
            ii = size - i - 1
            lin = ("0" * ii) + "3" + ("0" * (size - (ii + 1) * 2)) + "2" + ("0" * ii)
       
        print(lin)
    print("")