hours_x, hours_y = map(int, input("Enter hours: "))
other_x, other_y = map(int, input("Enter other: "))

# конь ходит буквой Г, проверям что он идет на 2 по х или по y и на 1 по y или по x
# if (abs(hours_x - other_x) == 2 and abs(hours_y - other_y) == 1) or (abs(hours_x - other_x) == 1 and abs(hours_y - other_y) == 2):
# можно проверять легче, если сумма проекций (расстояний) равна 3
if abs(hours_x - other_x) + abs(hours_y - other_y) == 3:
    print("YES")
else:
    print("NO")
