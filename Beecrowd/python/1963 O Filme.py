X, Y = [float(x) for x in input().split(" ")]

por = (Y - X) / X
print("%.2f" % (por * 100) + "%")