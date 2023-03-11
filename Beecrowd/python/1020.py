years = 0
months = 0

days = int(input())

years = int(days / 365)
days -= years * 365

months = int(days / 30)
days -= months * 30

print(
f"""{years} ano(s)
{months} mes(es)
{days} dia(s)""")