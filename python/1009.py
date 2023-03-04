
input()

salary = float(input())
commission = float(input())

total = salary + commission * 0.15

print("TOTAL = R$ " + "%.2f" % round(total, 2))