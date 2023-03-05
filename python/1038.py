PRICES = {
    "1" : 4.00,
    "2" : 4.50,
    "3" : 5.00,
    "4" : 2.00,
    "5" : 1.50
}

numbList = input().split(" ")

total = PRICES[numbList[0]] * int(numbList[1])

print("Total: R$ " + "%.2f" % total)