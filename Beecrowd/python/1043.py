numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = float(numbList[i])

A, B, C = numbList

isTriangle = (abs(B - C) < A < B + C)

if(isTriangle):
    print("Perimetro = " + str("%.1f" % (A + B + C)))
else:
    print("Area = " + str("%.1f" % ((A + B) * C / 2)))
