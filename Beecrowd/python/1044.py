numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = int(numbList[i])

A, B = numbList

print("Sao Multiplos" if (B % A == 0) | (A % B == 0) else "Nao sao Multiplos")

