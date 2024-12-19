# This is a comment in Python - it starts with #

# 1. Variables and basic data types
x = 5           # Integer
y = 3.14        # Float (decimal number)
name = "Python" # String (text)
is_true = True  # Boolean (True/False)

# 2. Print something to the screen
print("Hello, World!")
print(x)  # Will print: 5

# 3. Basic math operations
addition = x + 2        # 7
subtraction = x - 2     # 3
multiplication = x * 2  # 10
division = x / 2        # 2.5

# Lists - ordered collections of items
particles = [1, 2, 3, 4, 5]  # A list of numbers
positions = [[0, 0], [1, 1], [2, 2]]  # A list of coordinate pairs

# Accessing list elements (Python starts counting at 0!)
first_particle = particles[0]    # Gets 1
second_position = positions[1]   # Gets [1, 1]

# Loops - doing something repeatedly
# For loop - repeat for each item
for number in particles:
    print(number)  # Will print each number on a new line

# While loop - repeat while a condition is true
count = 0
while count < 5:
    print(f"Count is: {count}")  # f-string for formatting
    count = count + 1  # or count += 1 for short


coordinates = [[1,2], [4,5], [7,8]]  # Note: Using 2D coordinates now
for coord in coordinates:
    print(f"x: {coord[0]}, y: {coord[1]}")  # Prints both x and y on same line

    import numpy as np

# Create a 5x5 grid of zeros
grid = np.zeros((5, 5))

# Place a 1 at position (2,2) (middle of the grid)
grid[2, 2] = 1

# Print the grid
print(grid)

import matplotlib.pyplot as plt
import numpy as np

# Basic plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()  # Actually display the plot

# Different types of plots
# Scatter plot
plt.scatter(x, y)
plt.show()

# Working with grids (will be useful for DLA)
grid = np.random.random((5, 5))  # 5x5 grid of random numbers
plt.imshow(grid)  # Display grid as a heatmap
plt.colorbar()    # Add a color scale
plt.show()