IDXTYPE = ["C", "R", "S"]

n = int(input())

typeCount = [0,0,0]

for i in range(n):
    C, T = input().split(" ")
    
    idx = IDXTYPE.index(T)
    typeCount[idx] = typeCount[idx] + int(C)
    
total = sum(typeCount)

print(f"""Total: {total} cobaias
Total de coelhos: {typeCount[0]}
Total de ratos: {typeCount[1]}
Total de sapos: {typeCount[2]}
Percentual de coelhos: {"%.2f" % (100 * typeCount[0] / total)} %
Percentual de ratos: {"%.2f" %   (100 * typeCount[1] / total)} %
Percentual de sapos: {"%.2f" %   (100 * typeCount[2] / total)} %""")