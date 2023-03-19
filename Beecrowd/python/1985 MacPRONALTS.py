PRICES = {
"1001" : 1.5,
"1002" : 2.50,
"1003" : 3.50,
"1004" : 4.50,
"1005" : 5.50
}

n = int(input())

total = 0

for i in range(n):
    X, Y = input().split(" ")
    total += PRICES[X] * int(Y)
    
print("%.2f" % total)