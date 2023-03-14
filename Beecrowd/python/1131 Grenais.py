gre = inter = grem = emp = 0

while True:
    gre += 1
    X, Y = [int(x) for x in input().split(" ")]
    
    if X > Y:
        inter += 1
    elif Y > X:
        grem += 1
    else:
        emp += 1
    
    n = input("Novo grenal (1-sim 2-nao)\n")
    if(n == "2"):
        break



print(f"""{gre} grenais
Inter:{inter}
Gremio:{grem}
Empates:{emp}""")

if inter > grem:
    print("Inter venceu mais")
elif grem > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")