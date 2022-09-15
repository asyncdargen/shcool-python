# Set and print variable
# a = 2
# print("a =", a)

# Simple calculator
# while True:
#     print(eval(input()))


# Write file
# file = open("text.txt", "w")
#
# file.write(input("To write: "))
#
# file.close()

# Mappings
# values_map = {
#     "first_value": 10,
#     "second_value": 22.33
# }
#
# print("Values sum =", values_map["first_value"] + values_map["second_value"])

# Sum or multiply numbers
# x = int(input("Enter x: "))
# y = float(input("Enter y: "))
# operator = input("Enter operation: ")
#
# result = 0
#
# if operator == "*":
#     result = x * y
# elif operator == "+":
#     result = x + y
#
# print(x, operator, y, "=", result)

# Task 1
# x = input("Enter x: ")
# int_x = int(x)
#
# # Check x is int and this length
# if int_x > 9999 or int_x < 1000:
#     print("Invalid input")
# else:
#     print("Numbers: [", end="")
#     for i in range(0, 4):
#         print(x[i], end="")
#         if i < 3:
#             print(", ", end="")
#     print("]")

# Task 2
# minutes = int(input("Enter left time: "))
# hour = int(minutes / 60)
# minutes /= 60
# minute = int(minutes)
#
# print("Time: ", hour, ":", minute, sep="")

while True:
    task_id = input("Enter task-id: ")
    task_name = f"lesson-1/task_{task_id}.py"

    task_file = open(task_name, "r")
    task_code = ""
    for line in task_file.readlines():
        task_code += line

    print(task_code)
    print(eval(task_code))
