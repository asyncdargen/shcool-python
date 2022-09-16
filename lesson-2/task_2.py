x = abs(int(input("Enter nuber: ")))
count = 0

while x > 0:
    if x % 10 % 2 == 0:
        count += 1
    x //= 10

print("Count:", count)
