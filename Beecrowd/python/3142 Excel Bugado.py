alphabet = [ "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",]
mul = {
    0 : 1,
    1 : 26,
    2 : 676
}

while True:
    try: 
        col = input()
    except EOFError as e:
        break
    
    sz = len(col)
    numb = 0
    
    if(sz >= 4):break
    
    for n in range(sz):
        i = alphabet.index(col[n]) + 1
        
        numb += i * mul[sz - n - 1]
    
    print(numb if numb <= 16384 else "Essa coluna nao existe Tobias!")
