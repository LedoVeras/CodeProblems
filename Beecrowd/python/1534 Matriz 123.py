while True:
    try: 
        size = int(input())
    except EOFError as e:
        break
        
    for i in range(size):
        lin = "3" * size
        lin = lin[:i] + "1" + lin[i + 1:]

        to = size - i - 1
        lin = lin[:to] + "2" + lin[to + 1:]
       
        print(lin)