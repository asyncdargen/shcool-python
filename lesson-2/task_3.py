x, y = map(int, input("Enter x y: ").split())

while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y %= x

print("Min divider:", max(x, y))
