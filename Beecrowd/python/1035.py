numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = float(numbList[i])

A, B, C, D = numbList

answer = B > C and D > A and (C + D) > (A + B) and (C > 0 and D > 0) and A % 2 == 0

print("Valores aceitos" if answer else "Valores nao aceitos")