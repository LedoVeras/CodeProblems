import functools

numbList = [x+1 for x in range(int(input()))]
print(functools.reduce(lambda a , b: a * b, numbList))