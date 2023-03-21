X, Y = [int(x) for x in input().split(" ")]
li = input().strip()
numbList = [int(x) for x in li.split(" ")]

difArr = [numbList[x + 1] - numbList[x] for x in range(len(numbList) - 1)]

print("GAME OVER" if any(filter(lambda x: abs(x) > X , difArr)) else "YOU WIN")