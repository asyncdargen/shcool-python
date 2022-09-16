x, y = int(input("Enter x y: "))

mx = max(x, y)
mn = min(x, y)

for i in range(mx, mn):
    for j in range(3, i - 1):
        if i % j == 0:
print("Factorial:", factorial)
