x, y = map(int, input("Enter x y: ").split())

mx = max(x, y)
mn = min(x, y)

for i in range(mn, mx):
    simple = True
    for j in range(2, i - 1):
        if i % j == 0:
            simple = False
    if simple:
        print(i)
