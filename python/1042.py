numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = int(numbList[i])

noSort = numbList.copy()
numbList.sort()

for cur in numbList:
    print(cur)

print("")

for cur in noSort:
    print(cur)