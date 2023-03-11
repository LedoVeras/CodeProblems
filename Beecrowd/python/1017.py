CAR_CONSUME = 12

time = int(input())
vel = int(input())

total = time * vel
liters = total / CAR_CONSUME

print("%.3f" % liters)