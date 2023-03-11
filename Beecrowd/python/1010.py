numbList1 = input().split(" ")
numbList2 = input().split(" ")

total = (int(numbList1[1]) * float(numbList1[2])) + (int(numbList2[1]) * float(numbList2[2]))

print("VALOR A PAGAR: R$ " + "%.2f" % total)