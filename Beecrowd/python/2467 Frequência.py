from collections import Counter

def most_common(lst):
    li = list(lst)
    li.sort(reverse=True)

    data = Counter(li)
    return data.most_common(1)[0][0]

N, Q = [int(x) for x in input().split(" ")]

matrix = [[0 for j in range(N)] for i in range(N)]

for i in range(Q):
    operat = [int(x) for x in input().split(" ")]
    X = operat[1] - 1
    
    if operat[0] == 1:
        matrix[X] = [operat[2] for j in range(N)]
    elif operat[0] == 2:
        for arr in matrix:
            arr[X] = operat[2]
    elif operat[0] == 3:
        print(most_common(matrix[X]))
    else:
        li = []
        for arr in matrix:
            li.append(arr[X])
        print(most_common(li))
        del li