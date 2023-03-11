x = float(input())

print("N[0] = " + "%.4f" % x)
prev = x

for i in range(1, 100):
    prev /= 2
    print(f"N[{i}] = " + "%.4f" % prev)