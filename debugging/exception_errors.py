#Looking at different exception errors
try:
    1 / 0
except ZeroDivisionError as e:
    print("Caught:", e)

try:
    int("hello")
except ValueError as e:
    print("Caught:", e)

try:
    print(does_not_exist)
except NameError as e:
    print("Caught:", e)
