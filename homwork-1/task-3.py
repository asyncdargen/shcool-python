count = int(input("Enter cow count: "))

if 11 <= count <= 14:
    postfix = "коров"
elif count % 10 == 1:
    postfix = "корова"
elif 2 <= count % 10 <= 4:
    postfix = "коровы"
else:
    postfix = "коров"

print("На лугу посется", count, postfix)
