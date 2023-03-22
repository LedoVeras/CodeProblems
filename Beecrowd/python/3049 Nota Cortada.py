NOTEAREA = 70 * 160

B = int(input())
T = int(input())

Feli = (B + T) * 70 / 2
Mazi = NOTEAREA - Feli

if Feli > Mazi:
    print(1)
elif Mazi > Feli:
    print(2)
else:
    print(0)