result = []

for i in range(10000, 1000000):
    if i % 133 == 125 and i % 134 == 111:
        result.append(i)

print("Result:", result)
