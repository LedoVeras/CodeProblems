NOTE_VALUES = [100, 50, 20, 10, 5, 2, 1]

note_counts = [0,0,0,0,0,0,0]

value = int(input())
curValue = value

for i in range(len(NOTE_VALUES)):
    count = int(curValue / NOTE_VALUES[i])
    curValue -= count * NOTE_VALUES[i]
    note_counts[i] = count

print(
f"""{value}
{note_counts[0]} nota(s) de R$ 100,00
{note_counts[1]} nota(s) de R$ 50,00
{note_counts[2]} nota(s) de R$ 20,00
{note_counts[3]} nota(s) de R$ 10,00
{note_counts[4]} nota(s) de R$ 5,00
{note_counts[5]} nota(s) de R$ 2,00
{note_counts[6]} nota(s) de R$ 1,00""")