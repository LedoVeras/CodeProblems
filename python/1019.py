total_seconds = int(input())

total_minutes = total_seconds / 60

hours = int(total_minutes / 60)
minutes = int(total_minutes % 60)
seconds = total_seconds % 60

print(f"{hours}:{minutes}:{seconds}")