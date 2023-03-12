a, b = [float(x) for x in input().split(" ")]

r = int(a % abs(b))
q = int(a / b)

if(a < 0 and r != 0):
    q += -1 * (b / abs(b))

print(int(q), r)