MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

while True:
    try: 
        M, D = [int(x) for x in input().split(" ")]
    except EOFError as e:
        break

    t = sum(MONTHS[:M - 1]) + D - 360

    if(t == -1):
        print("E vespera de natal!")
    elif(t < -1):
        print(f"Faltam {abs(t)} dias para o natal!")
    elif(t == 0):
        print("E natal!")
    else:
        print("Ja passou!")