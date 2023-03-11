import re

#codigo fei

numbList = [input(), input(), input(), input()]

for i in range(len(numbList)):
    hand = re.compile(r'[$0-9]').findall(numbList[i])
    numbList[i] = ''.join(str(x) for x in hand)

numbList[0] = int(numbList[0])
numbList[2] = int(numbList[2])
TIME_SCALE = [60, 3600, 3600 * 24]

st1 = numbList[1]
hhmmss1 = [int(st1[0:2]), int(st1[2:4]), int(st1[4:6])]
seconds1 = numbList[0] * TIME_SCALE[2] + hhmmss1[0] * TIME_SCALE[1] + hhmmss1[1] * TIME_SCALE[0] + hhmmss1[2]

st2 = numbList[3]
hhmmss2 = [int(st2[0:2]), int(st2[2:4]), int(st2[4:6])]
seconds2 = numbList[2] * TIME_SCALE[2] + hhmmss2[0] * TIME_SCALE[1] + hhmmss2[1] * TIME_SCALE[0] + hhmmss2[2]

total_seconds = seconds2 - seconds1

total_minutes = total_seconds / 60

hours = int(total_minutes / 60)
minutes = int(total_minutes % 60)
seconds = total_seconds % 60

days = int(hours / 24)
hours = hours % 24

print(f"""{days} dia(s)
{hours} hora(s)
{minutes} minuto(s)
{seconds} segundo(s)""")

