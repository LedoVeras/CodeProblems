
while ...:
    X, Y = [int(x) for x in input().split(" ")]

    sum = (0 if X == 0 else (1 if X > 0 else 2)) + (0 if Y == 0 else (4 if Y > 0 else 8)) 

    answer = {
        5 : "primeiro",
        6 : "segundo",
        9 : "quarto",
        10 : "terceiro"
    }

    if(sum == 0):break

    try:   
        print(answer[sum])
    except ValueError:
        break
