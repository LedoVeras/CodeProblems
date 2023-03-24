input()

res = [0,0,0,0]

for x in input().split(" "):
    x = int(x)
    for i in range(4):
        res[i] += 1 if x % (i + 2) == 0 else 0
    
print(f"""{res[0]} Multiplo(s) de 2
{res[1]} Multiplo(s) de 3
{res[2]} Multiplo(s) de 4
{res[3]} Multiplo(s) de 5""")