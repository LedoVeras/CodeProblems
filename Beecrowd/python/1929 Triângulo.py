A, B, C, D = [float(x) for x in input().split(" ")]

def verify(a,b,c):
    return abs(b - c) < a < b + c

toRt = verify(A, B, C) or verify(A, B, D) or verify(A, C, D) or verify(B, C, D)
print("S" if toRt else "N")