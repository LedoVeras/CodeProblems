T = int(input())

for i in range(T):
    N, K = [int(x) for x in input().split(" ")]
    print((N % K) + (N // K))