PI = 3.14

while ...:
    try:
        V = float(input())
    except EOFError:
        break
    
    R = float(input()) / 2
    
    area = PI * R ** 2
    height = V / area
    print(f"""ALTURA = {"%.2f" % height}
AREA = {"%.2f" % area}""")