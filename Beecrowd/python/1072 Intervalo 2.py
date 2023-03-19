n = int(input())

inRange = 0

for i in range(n):
    j = int(input())
    if(j >= 10 and j <= 20):
        inRange += 1
        
print(f"""{inRange} in
{n - inRange} out""")
    