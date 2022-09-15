from random import randint

n = randint(100, 9999)

n_1 = n // 1000
n_2 = (n % 1000) // 100
n_3 = n % 100 // 10
n_4 = n % 10

print("Number", n)
print(n_1 - n_4 + n_2 - n_3 + 1)
