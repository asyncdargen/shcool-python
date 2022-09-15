minutes = int(input())

hours = minutes // 60
minutes -= hours * 60

print(min(hours, 23), min(minutes, 59), sep=":")
