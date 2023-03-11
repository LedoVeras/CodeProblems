x = int(input())

n = [x]

print(f"N[{0}] = {x}")

for i in range(1, 11):
    n.append(n[i - 1] * 2)
    print(f"N[{i}] = {n[i]}")