n = int(input())

for i in range(n):
    A, B, C, D = [x for x in input().split(" ")]
    t = {
        B : A,
        D : C
    }
    su = sum([int(x) for x in input().split(" ")])
    verify = "PAR" if su % 2 == 0 else "IMPAR"
    print(t[verify])