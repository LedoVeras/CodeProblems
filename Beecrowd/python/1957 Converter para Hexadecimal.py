HEX = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

n = int(input())

tt = ""
while round(n) >= 16:
    c = n % 16
    tt += str(HEX[c] if c >= 10 else c)
    n //= 16
    
c = n % 16
tt += str(HEX[c] if c >= 10 else c)   

print(tt[::-1])