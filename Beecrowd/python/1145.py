numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = int(numbList[i])

X, Y = numbList

for i in range(1, Y + 1):
    toPt = str(i)
    if(i % X == 0): toPt += "\n"
    else: toPt += " "
    print(toPt, end="")