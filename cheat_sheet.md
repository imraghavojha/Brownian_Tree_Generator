# Python Basics Cheat Sheet

## 1. Comments and Basic Syntax
```python
# This is a single line comment
"""
This is a 
multi-line comment
"""
```

## 2. Variables and Data Types
```python
# Python automatically determines the type of variable
x = 5           # Integer (whole number)
y = 3.14        # Float (decimal number)
name = "Python" # String (text)
is_true = True  # Boolean (True/False)

# Print values to console
print("Hello, World!")  # Prints: Hello, World!
print(x)               # Prints: 5
```

## 3. Basic Math Operations
```python
addition = x + 2        # Addition
subtraction = x - 2     # Subtraction
multiplication = x * 2  # Multiplication
division = x / 2        # Division (returns float)
power = x ** 2         # Exponentiation (x squared)
```

## 4. Lists and List Operations
```python
# Lists can store multiple items
numbers = [1, 2, 3, 4, 5]              # Simple list
positions = [[0, 0], [1, 1], [2, 2]]   # Nested list (2D coordinates)

# Accessing list elements (index starts at 0)
first_item = numbers[0]      # Gets first item
last_item = numbers[-1]      # Gets last item
sub_list = numbers[1:3]      # Gets items from index 1 to 2

# Modifying lists
numbers.append(6)            # Adds item to end
numbers.pop()               # Removes last item
numbers.insert(0, 0)        # Inserts 0 at index 0
```

## 5. Loops
```python
# For loop - iterate over a sequence
for number in numbers:
    print(number)

# For loop with range
for i in range(5):    # 0 to 4
    print(i)

# While loop - repeat while condition is true
count = 0
while count < 5:
    print(f"Count is: {count}")  # f-string formatting
    count += 1                   # increment counter
```

## 6. NumPy Basics
```python
import numpy as np

# Create arrays
grid = np.zeros((5, 5))         # 5x5 grid of zeros
array = np.array([1, 2, 3])     # Convert list to numpy array

# Random numbers
random_num = np.random.random()  # Random float between 0 and 1
random_int = np.random.randint(0, 10)  # Random int between 0 and 9
```

## 7. Matplotlib Plotting
```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Title")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.show()

# Grid/Image plot
grid = np.random.random((5, 5))
plt.imshow(grid)
plt.colorbar()
plt.show()
```

## 8. Functions
```python
# Basic function
def say_hello():
    print("Hello!")

# Function with parameters
def add_numbers(a, b):
    return a + b

# Function with default parameters
def create_point(x=0, y=0):
    return [x, y]

# Using functions
say_hello()                    # Prints: Hello!
result = add_numbers(5, 3)     # Returns: 8
point = create_point(2, 3)     # Returns: [2, 3]
```

## 9. Classes and Objects
```python
class Particle:
    # Constructor - runs when creating new object
    def __init__(self, x=0, y=0):
        self.x = x          # Instance variable
        self.y = y
        self.stuck = False
    
    # Method - function belonging to class
    def move(self):
        self.x += 1
    
    def is_stuck(self):
        return self.stuck

# Using classes
particle1 = Particle(3, 4)     # Create new particle object
particle1.move()               # Call method
print(particle1.x)             # Access property
```

## 10. Imports and Modules
```python
# Import entire module
import numpy as np
import matplotlib.pyplot as plt

# Import specific items
from random import randint, choice

# Import from local file
from particle import Particle  # Imports Particle class from particle.py
```

## Tips for Good Python Code:
1. Use clear variable names
2. Add comments to explain complex logic
3. Use consistent indentation (Python requires it!)
4. Break complex operations into smaller functions
5. Use classes to organize related data and functions
6. Keep code modular using separate files/modules