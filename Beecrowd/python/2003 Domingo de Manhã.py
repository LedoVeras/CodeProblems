while...:
    try:
        h = [int(x) for x in input().split(":")]
    except EOFError:
        break
    
    dif = max(0, (h[0] * 60 + h[1]) - 420)
    print(f"Atraso maximo: {dif}")
    