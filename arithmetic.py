"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    denominator = num1 - num2
    return denominator

def multiply(num1, num2):
    """Multiply the two inputs together."""
    mulitple = num1 * num2
    return mulitple

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divisor = num1 / num2
    return divisor

def square(num1):
    """Return the square of the input."""
    num_squared = num1 ** 2
    return num_squared

def cube(num1):
    """Return the cube of the input."""
    num_cubed = num1 ** 3
    return num_cubed

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    num_power = num1 ** num2
    return num_power

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modulo = num1 % num2
    return modulo

print(add(1, 2))
print(subtract(10, 5)) 
print(multiply(2, 3))
print(divide(7, 2))
print(square(2))
   