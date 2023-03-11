axisList = input().split(" ")

for i in range(len(axisList)):
  axisList[i] = float(axisList[i])

X, Y = axisList

"""
    1 = x > 0
    2 = x < 0
    4 = y > 0
    8 = y < 0
"""

sum = (0 if X == 0 else (1 if X > 0 else 2)) + (0 if Y == 0 else (4 if Y > 0 else 8)) 

answer = {
    0 : "Origem",
    1 : "Eixo X",
    2 : "Eixo X",
    4 : "Eixo Y",
    8 : "Eixo Y",
    5 : "Q1",
    6 : "Q2",
    9 : "Q4",
    10 : "Q3"
}

print(answer[sum])
