input()

numbList = [float(x) for x in input().split(" ")]
choice = min(numbList)

print(numbList.index(choice) + 1)