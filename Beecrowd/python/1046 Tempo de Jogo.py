X, Y = [float(x) for x in input().split(" ")]
hours = int((24 - (X - Y)) % 24)

print(f"O JOGO DUROU {24 if hours == 0 else hours} HORA(S)")