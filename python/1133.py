numbs = (int(input()), int(input()))

X = min(numbs[0], numbs[1])
Y = max(numbs[0], numbs[1])
poss = [2, 3]

for i in range(X + 1 , Y):
    if(i % 5 in poss):
        print(i)