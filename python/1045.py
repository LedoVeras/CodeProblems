numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = float(numbList[i])

numbList.sort()
numbList.reverse()

A, B, C = numbList

if(A >= (B + C)):
    print("NAO FORMA TRIANGULO")
else:
    if pow(A, 2) == pow(B, 2) + pow(C, 2):
        print("TRIANGULO RETANGULO")
        
    if pow(A, 2) > pow(B, 2) + pow(C, 2):
        print("TRIANGULO OBTUSANGULO")
        
    if pow(A, 2) < pow(B, 2) + pow(C, 2):
        print("TRIANGULO ACUTANGULO")
        
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (B == C) or (A == C):
        print("TRIANGULO ISOSCELES")


