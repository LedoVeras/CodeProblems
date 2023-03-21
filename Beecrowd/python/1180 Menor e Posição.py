input()
st = ""
while True:
    try: 
        s = input()
    except EOFError:
        break
    
    if(s == ""):
        break
    
    st += s
    
st = " ".join(st.split()).split(" ")

numbList =  [int(x) for x in st]
mi = min(numbList)
print(f"""Menor valor: {mi}
Posicao: {numbList.index(mi)}""")