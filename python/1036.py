numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = float(numbList[i])

A, B, C = numbList

delta = (B ** 2 - 4 * A * C)

if(delta < 0 or A == 0): {print("Impossivel calcular") }

else:

    delta = delta ** 0.5

    R1 = (-B + delta) / (2 * A)
    R2 = (-B - delta) / (2 * A)

    print(f"""R1 = {"%.5f" % R1}
R2 = {"%.5f" % R2}""")
