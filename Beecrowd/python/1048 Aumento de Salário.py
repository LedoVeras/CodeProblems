FAIXAS = [-1, 400, 800, 1200, 2000]
REAJUS = {
    -1 :   0.15,
    400 :  0.12,
    800 :  0.1,
    1200 : 0.07,
    2000 : 0.04
}

sal = float(input())
i = list(filter(lambda a : sal > a, FAIXAS))

por = REAJUS[i[-1]]
rej = sal * por

print(f"""Novo salario: {"%.2f" % (sal + rej)}
Reajuste ganho: {"%.2f" % rej}
Em percentual: {round(por * 100)} %""")
