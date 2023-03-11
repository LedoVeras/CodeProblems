numbs = [int(input()), int(input())]

MI = min(numbs[0], numbs[1])
MA = max(numbs[0], numbs[1])

ne = MI + (13 - (MI % 13))
la = MA - (MA % 13)

total = int((MI + MA) * (MA - MI + 1) / 2)

count = int(((la / 13) + 1) - (ne / 13))

total13 = int((ne + la) * count / 2)

print(total - total13)