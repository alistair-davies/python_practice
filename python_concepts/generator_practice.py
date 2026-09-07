def numbers():
    for n in range(5):
        print("numbers() produced:", n)
        yield n

def double(gen):
    for n in gen:
        doubled = n * 2
        print("double() received:", n, "→ produced:", doubled)
        yield doubled

def stringify(gen):
    for n in gen:
        text = f"Value: {n}"
        print("stringify() received:", n, "→ produced:", text)
        yield text

pipeline = stringify(double(numbers()))

for item in pipeline:
    print("FINAL OUTPUT:", item)

