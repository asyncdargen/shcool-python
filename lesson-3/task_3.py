n = int(input("Enter max: "))

print("Result:")

for i in range(0, n + 1):
    if str(i ** 2).endswith(str(i)):
        print(i, " ** ", 2, " = ", i ** 2, sep="")
