numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = int(numbList[i])

X, Y = numbList

for i in range(1, Y, X):
    if(i + 2 > Y):break
    print(f"{i} {i + 1} {i + 2}")