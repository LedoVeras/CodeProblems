NOTE_VALUES = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

note_counts = [0] * len(NOTE_VALUES)

value = float(input())
curValue = value

for i in range(len(NOTE_VALUES)):
    count = int(round(curValue, 2) / NOTE_VALUES[i])
    curValue -= count * NOTE_VALUES[i]
    note_counts[i] = count

print(
f"""NOTAS:
{note_counts[0]} nota(s) de R$ 100.00
{note_counts[1]} nota(s) de R$ 50.00
{note_counts[2]} nota(s) de R$ 20.00
{note_counts[3]} nota(s) de R$ 10.00
{note_counts[4]} nota(s) de R$ 5.00
{note_counts[5]} nota(s) de R$ 2.00
MOEDAS:
{note_counts[6]} moeda(s) de R$ 1.00
{note_counts[7]} moeda(s) de R$ 0.50
{note_counts[8]} moeda(s) de R$ 0.25
{note_counts[9]} moeda(s) de R$ 0.10
{note_counts[10]} moeda(s) de R$ 0.05
{note_counts[11]} moeda(s) de R$ 0.01""")