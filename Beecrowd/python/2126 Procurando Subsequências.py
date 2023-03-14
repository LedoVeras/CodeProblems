caso = 0
while True:
    try: 
        nu = input()
    except EOFError as e:
        break
    
    caso += 1
    
    len1 = len(nu)
    N2 = input()

    qtd = 0
    
    try: 
        index = N2.rindex(nu)
    except ValueError:
        print(f"""Caso #{caso}:
Nao existe subsequencia\n""")
        continue    
    
    while True:
        try: 
            idx = N2.index(nu)
        except ValueError:
            break
        
        qtd += 1
        
        N2 = N2[:idx] + N2[idx + len1:]

    print(f"""Caso #{caso}:
Qtd.Subsequencias: {qtd}
Pos: {index + 1}\n""")