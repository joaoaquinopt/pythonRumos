two_integer = 2
four_integer = 4
three_float = 3.1
four_float = 4.0
zero = 0
hello = "Hello"
hi = "Hi"

# Arithmetic Operators
# Addition
addition = two_integer + four_integer
print("Addition: " + str(addition))

# Subtraction
subtraction = four_integer - two_integer
print("Subtraction: " + str(subtraction))

# Multiplication
multiplication = two_integer * four_integer
print("Multiplication: " + str(multiplication))

# Division
division = four_integer // two_integer
print("Division: " + str(division))

# Modulus
modulus = four_float % three_float
print("Modulus: " + str(modulus))

# Exponential
exponential = two_integer ** two_integer
print("Exponential: " + str(exponential))

# Floor Division
floor_division = four_float / three_float
print("Floor Division: " + str(floor_division))

# Simplified Operation
simplified_operation = 6
simplified_operation -= two_integer
print("Simplified: " + str(simplified_operation))

# Comparison Operators
# Greater than
greater_than = four_integer > two_integer
print("Greater than: " + str(greater_than))

# Less than
less_than = four_integer < two_integer
print("Less than: " + str(less_than))

# Greater or Equal to
greater_or_equal_to = four_float >= three_float
print("Greater or Equal to: " + str(greater_or_equal_to))

# Less or Equal to
less_or_equal_to = four_float <= three_float
print("Less or Equal to: " + str(less_or_equal_to))

# Equal to
equal_to = four_integer == exponential
print("Equal to: " + str(equal_to))

# Not Equal to
not_equal_to = two_integer != exponential
print("Not Equal to: " + str(not_equal_to))

# Logical Operators
# And
and_operator = hi == 'Hi' and hello == 'Hello'
print("And: " + str(and_operator))

# Or
or_operator = hi == 'Hi' or hello == 'Hello'
print("Or: " + str(or_operator))

# Not
not_operator = not hi == 'Hi'
print("Not: " + str(not_operator))