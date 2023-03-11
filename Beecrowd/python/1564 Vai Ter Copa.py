while(True):
    try: 
        re = input()
    except EOFError as e:
        break
    print("vai ter copa!" if re == "0" else "vai ter duas!")