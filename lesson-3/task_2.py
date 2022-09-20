from typing import List


def slice_parts(number) -> List:
    x = number
    parts = []

    while x > 0:
        parts.append(x % 10)
        x //= 10

    return parts


def parts_quadro_sum(parts: List) -> int:
    sum = 0

    for j in parts:
        sum += j ** len(parts)

    return sum


result = []

for i in range(100, 1000):
    if parts_quadro_sum(slice_parts(i)) == i:
        result.append(i)

print("Result:", result)
