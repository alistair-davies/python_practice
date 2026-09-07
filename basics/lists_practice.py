"""mixed = ['Hello', 10, 'WORLD', 5, 'Python']


lowercase_strings = [lower.lower() for lower in mixed if isinstance(lower, str) ]

print(lowercase_strings)
"""

mixed = ['Hello', 10, 'WORLD', 5, 'Python']


lengths = [len(long) for long in mixed if isinstance(long, str)]

print(lengths)
