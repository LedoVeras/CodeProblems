INTERVALS = [[0,25], [25,50], [50,75], [75,100]]
INTERVALSSTR = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]

numb = float(input())

answer = 0

if(numb < 0 or numb > 100): print("Fora de intervalo")
else:
    for interval in INTERVALS:
        if(numb > interval[0] and numb <= interval[1]):
            answer = INTERVALS.index(interval)
            break
        
    print("Intervalo " + INTERVALSSTR[answer])