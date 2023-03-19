import functools

N, M = [int(x) for x in input().split(" ")]

fruits = []
for i in range(N):
   fruits.append(input().lower())

virused = functools.reduce(lambda x, y: x+y, [input() for j in range(M)]).lower()

for f in fruits:
    likes = f in virused or f[::-1] in virused
    
    print("Sheldon" , "come" if likes else "detesta" , "a fruta", f)
   
