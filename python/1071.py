X = int(input())
Y = int(input())

sum = 0

for i in range(Y + 1, X):
    if(i % 2 == 1):
        sum += i

print(sum)