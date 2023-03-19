n = int(input())

for i in range(n):
    H, D, G= [int(x) for x in input().split(" ")]
    
    choice = (H >= 200 and H <= 300) & (D >= 50) & (G >= 150)
    print("Sim" if choice else "Nao")