x = 10

def f():
    y = x + 5
    print("Inside f, y =", y)

print("Before calling f")
f()
print("After calling f")
print("Trying to print y outside f...")
try:
    print(y)
except NameError as e:
    print("Error:", e)
