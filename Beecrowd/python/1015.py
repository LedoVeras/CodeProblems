p1 = input().split(" ")
p2 = input().split(" ")

distance = ((float(p2[0]) - float(p1[0])) ** 2 + (float(p2[1]) - float(p1[1])) ** 2) ** 0.5

print("%.4f" % distance)