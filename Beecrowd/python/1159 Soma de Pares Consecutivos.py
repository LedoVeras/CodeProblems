import functools

while ...:
    n = int(input())
    
    if(n == 0):
        break
    
    nePair = n + (n % 2)
    arr = [nePair + 2 * i for i in range(5)]
    print(functools.reduce(lambda a, b: a + b, arr))