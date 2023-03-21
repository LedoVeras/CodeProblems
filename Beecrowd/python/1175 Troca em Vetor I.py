numbList = [input() for x in range(20)]

numbList.reverse()

for i in range(len(numbList)):
    print(f"N[{i}] = {numbList[i]}")