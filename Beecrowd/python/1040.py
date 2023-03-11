notaList = input().split(" ")

for i in range(len(notaList)):
  notaList[i] = float(notaList[i])

A, B, C, D = notaList

media = round((A * 2 + B * 3 + C * 4 + D) / 10, 1)

if(media >= 7):
    print(f"Media: {media}")
    print("Aluno aprovado.")
elif(media >= 5 and media <= 6.9):
    
    print(f"""Media: {media}
Aluno em exame.""")
    
    exam = float(input())
    final = (media + exam) / 2
    
    print(f"Nota do exame: {exam}")
    print("Aluno aprovado.") if final >= 5.0 else print("Aluno reprovado.")
    print(f"Media final: {final}")

else:
    print(f"Media: {media}")
    print("Aluno reprovado.")