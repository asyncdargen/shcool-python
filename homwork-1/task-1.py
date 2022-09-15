a_x, a_y = map(int, input("Enter A: ").split())
b_x, b_y = map(int, input("Enter B: ").split())
c_x, c_y = map(int, input("Enter C: ").split())

# считаем модули (длины) сторон треугольника
a = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** .5
b = ((b_x - c_x) ** 2 + (b_y - c_y) ** 2) ** .5
c = ((c_x - a_x) ** 2 + (c_y - a_y) ** 2) ** .5

# считаем периметр и полу-периметр
perimeter = a + b + c
half_perimeter = perimeter / 2

# считаем площадь по формуле герона
squire = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** .5

print("Length: a -", int(a), ", b -", int(b), ", c -", int(c))
print("Perimeter:", int(half_perimeter))
print("Square:", int(squire))
