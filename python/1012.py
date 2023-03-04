PI = 3.14159

numbList = input().split(" ")

for i in range(len(numbList)):
  numbList[i] = float(numbList[i])

n1 , n2 , n3 = numbList

tri = n1 * n3 / 2.0
cir = (n3 ** 2.0) * PI
tra = (n1 + n2) * n3 / 2.0
squ = n2 ** 2.0
rec = n1 * n2

print(
f"""TRIANGULO: {"%.3f" % tri}
CIRCULO: {"%.3f" % cir}
TRAPEZIO: {"%.3f" % tra}
QUADRADO: {"%.3f" % squ}
RETANGULO: {"%.3f" % rec}""")