A, B, C = [int(x) for x in input().split(" ")]

va1 = B - A
va2 = C - B

toRt = va1 > 0 if va2 == va1 else va2 > va1
print(":)" if toRt else ":(")