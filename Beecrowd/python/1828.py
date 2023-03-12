intHandle = {
    "pedra" : 0,
    "papel" : 1,
    "tesoura": 2,
    "lagarto": 3,
    "Spock": 4
}

win = {
    0 : [3,2],
    1 : [0,4],
    2 : [1,3],
    3 : [4,1],
    4 : [2,0]
}

n = int(input())

for i in range(n):
    X, Y = [intHandle[x] for x in input().split(" ")]
    
    if(X == Y):
        print(f"Caso #{i + 1}: De novo!")
    elif win[X].__contains__(Y):
        print(f"Caso #{i + 1}: Bazinga!")
    else:
        print(f"Caso #{i + 1}: Raj trapaceou!")

