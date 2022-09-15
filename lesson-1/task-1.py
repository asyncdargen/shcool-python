from random import randint

x = randint(1000, 9999)

print("Number:", x)

x_1 = x // 1000
x_2 = (x % 1000) // 100
x_3 = x % 100 // 10
x_4 = x % 10

print("Numbers: ", end="")
print(x_1, x_2, x_3, x_4, sep=", ")
print("Pow: ", x_1 * x_2 * x_3 * x_4)
print("Sum: ", x_1 * x_2 * x_3 * x_4)
print("Middle swap:", x_1 * 1000 + x_3 * 100 + x_2 * 10 + x_4)
