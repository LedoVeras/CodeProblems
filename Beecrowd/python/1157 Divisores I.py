n = int(input())

if(n != 0):
    li = [1]

    for i in range(2, n + 1):
        if(n % i == 0):
            li.append(i)
            
    for l in li:
        print(l)