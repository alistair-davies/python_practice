Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
python --version
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python --version
NameError: name 'python' is not defined
python version
SyntaxError: invalid syntax
2 + 2
4
hello
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
print(Hello)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(Hello)
NameError: name 'Hello' is not defined
print ('Hello')
Hello
run rpgcharacter.py
SyntaxError: invalid syntax

========== RESTART: /Users/alidavies/Documents/Python/rpgcharacter.py ==========
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○

=========== RESTART: /Users/alidavies/Documents/Python/rpgchamess.py ===========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/rpgchamess.py", line 50, in <module>
    print(create_character('ren', 4, 2, 1))
  File "/Users/alidavies/Documents/Python/rpgchamess.py", line 23, in create_character
    err = validate_name(name)
  File "/Users/alidavies/Documents/Python/rpgchamess.py", line 19, in validate_name
    return none
NameError: name 'none' is not defined. Did you mean: 'None'?

=========== RESTART: /Users/alidavies/Documents/Python/rpgchamess.py ===========
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
SyntaxError: multiple statements found while compiling a single statement
number = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    numbers.append(even_numbers)
NameError: name 'numbers' is not defined. Did you mean: 'number'? Or did you forget to import 'numbers'?
number.append(even_numbers)
print(number)
[1, 2, 3, 4, 5, [6, 8, 10]]
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
program = programming_languages.count('Rust')
print(program)
2
quit
Use quit() or Ctrl-D (end-of-file) to exit

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
Stars
1 shine in the sky
in
2 white and bright
bright
3 until the end of the night
of

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
5
1 shine in the sky
2
2 white and bright
6
3 until the end of the night
2

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
5
1 shine in the sky
2
2 white and bright
6
3 until the end of the night
2

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
5

1 shine in the sky
2
5
2 white and bright
6
52
3 until the end of the night
2
526

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
5

1 shine in the sky
2
5
2 white and
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/code_extractor.py", line 16, in <module>
    pin_extractor(poem)
  File "/Users/alidavies/Documents/Python/code_extractor.py", line 7, in pin_extractor
    print(str(len(words[line_index])))
IndexError: list index out of range

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
0 Stars and the moon
5

1 shine in the sky
2
5
2 white and bright
6
52
3 until the end of the night
2
526

========= RESTART: /Users/alidavies/Documents/Python/code_extractor.py =========
['5202', '3346', '50000']

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 14, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 2, in number_pattern
    if isnotinstance(n, int):
NameError: name 'isnotinstance' is not defined. Did you mean: 'isinstance'?

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Argument must be an integer value.

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 16, in <module>
    print(number_pattern('4'))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 5, in number_pattern
    if n < 1:
TypeError: '<' not supported between instances of 'str' and 'int'

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Argument must be an integer value.

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 16, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 10, in number_pattern
    no_pattern.append(str(x))
AttributeError: 'str' object has no attribute 'append'

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 16, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 10, in number_pattern
    no_pattern.append(x)
AttributeError: 'str' object has no attribute 'append'

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
[1, 2, 3, 4]

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 16, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 10, in number_pattern
    no_pattern += x
TypeError: can only concatenate str (not "int") to str

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 16, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 10, in number_pattern
    no_pattern += x
TypeError: 'int' object is not iterable

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
[1, 2, 3, 4]

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
['1', '2', '3', '4']

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 18, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 11, in number_pattern
    no_pattern.append(str(x))
NameError: name 'no_pattern' is not defined

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
['1', '2', '3', '4']

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
['1', '2', '3', '4']

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 17, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 11, in number_pattern
    no_pattern += xß
NameError: name 'xß' is not defined

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 17, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 11, in number_pattern
    no_pattern += x
TypeError: can only concatenate str (not "int") to str

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
1234

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/number_generator.py", line 19, in <module>
    print(number_pattern(4))
  File "/Users/alidavies/Documents/Python/number_generator.py", line 13, in number_pattern
    nopattern += (str(' '))
UnboundLocalError: cannot access local variable 'nopattern' where it is not associated with a value

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
1 2 3 4

======== RESTART: /Users/alidavies/Documents/Python/number_generator.py ========
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/discount.py", line 16, in <module>
    print (type(price))
NameError: name 'price' is not defined. Did you mean: 'print'?

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

Warning (from warnings module):
  File "/Users/alidavies/Documents/Python/discount.py", line 2
    if type(price) is not 'int' or type(discount) is not 'float':
SyntaxWarning: "is not" with 'str' literal. Did you mean "!="?
>>> 
Warning (from warnings module):
  File "/Users/alidavies/Documents/Python/discount.py", line 2
    if type(price) is not 'int' or type(discount) is not 'float':
SyntaxWarning: "is not" with 'str' literal. Did you mean "!="?
>>> 
============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/discount.py", line 15, in <module>
    print(apply_discount(100, 20))
  File "/Users/alidavies/Documents/Python/discount.py", line 2, in apply_discount
    if not isinstance(int, price) or not isinstance(float, price):
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The discount should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The price should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
The price should be a number

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/discount.py", line 14, in <module>
    calculated_price = apply_discount(100, 20)
  File "/Users/alidavies/Documents/Python/discount.py", line 2, in apply_discount
    if not (isinstance(price, (int,ßfloat))):
NameError: name 'ßfloat' is not defined. Did you mean: 'float'?

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
21.0

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
-19.0

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
80.0

============ RESTART: /Users/alidavies/Documents/Python/discount.py ============
180.0

============ RESTART: /Users/alidavies/Documents/Python/myproject.py ===========
{'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

============ RESTART: /Users/alidavies/Documents/Python/myproject.py ===========
{'Laptop': 792, 'Smartphone': 600, 'Tablet': 250, 'Headphones': 70}
{'Laptop': 792, 'Smartphone': 480, 'Tablet': 250, 'Headphones': 70}
{'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 70}
{'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

========== RESTART: /Users/alidavies/Documents/Python/rpgcharacter.py ==========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 48, in <module>
    print(create_character('ren', 4, 2, 1))
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 42, in create_character
    character_summary.append(f"STR {status_bar(strength)}")
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 36, in status_bar
    return dot_scale * full_dot + dot_scale-10 * empty_dot
TypeError: can only concatenate str (not "int") to str
>>> 
========== RESTART: /Users/alidavies/Documents/Python/rpgcharacter.py ==========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 49, in <module>
    print(create_character('ren', 4, 2, 1))
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 42, in create_character
    f"STR {status_bar(strength)}",
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 36, in status_bar
    return dot_scale * full_dot + dot_scale-10 * empty_dot
TypeError: can only concatenate str (not "int") to str
>>> 
========== RESTART: /Users/alidavies/Documents/Python/rpgcharacter.py ==========
Traceback (most recent call last):
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 49, in <module>
    print(create_character('ren', 4, 2, 1))
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 42, in create_character
    f"STR {status_bar(strength)}",
  File "/Users/alidavies/Documents/Python/rpgcharacter.py", line 36, in status_bar
    return dot_scale * full_dot + 10-dot_scale * empty_dot
TypeError: can only concatenate str (not "int") to str
>>> 
========== RESTART: /Users/alidavies/Documents/Python/rpgcharacter.py ==========
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
