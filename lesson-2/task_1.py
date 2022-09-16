a, b, c = map(int, input("Enter a b c: ").split())

mx = max(a, b, c)
mn = min(a, b, c)
md = a + b + c - mx - mn

if mx ** 2 > mn ** 2 + md ** 2:
    print("Треугольник тупоугольный")
elif mx ** 2 == mn ** 2 + md ** 2:
    print("Треугольник прямоугольный")
else:
    print("Треугольник остроуголный")
