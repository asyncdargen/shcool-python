mx = 0
mn = 0

x = int(input("Enter next: "))

while x != 0:
    mx = max(mx, x)
    mn = min(mn, x)

    x = int(input("Enter next: "))

print("Min:", mn)
print("Max:", mx)
