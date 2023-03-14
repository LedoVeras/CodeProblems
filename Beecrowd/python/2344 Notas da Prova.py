GRADES = [0, 1, 36, 61, 86]
CONCEITO = ["E", "D", "C", "B", "A"]

n = int(input())
print(CONCEITO[len(list(filter(lambda a : a <= n, GRADES))) - 1])  