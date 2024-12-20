# 1. INITIALIZATION
import numpy as np

# Set simulation parameters
GRID_SIZE = 200
TOTAL_PARTICLES = 1000
MAX_STEPS = 1000
KILL_RADIUS = 100  # If particle goes beyond this distance from center, restart it
CENTER = GRID_SIZE // 2

# Create empty grid and place initial particle in center
grid = np.zeros((GRID_SIZE, GRID_SIZE))
grid[CENTER, CENTER] = 1  # Center particle

def distance_from_center(x, y):
    return np.sqrt((x - CENTER)**2 + (y - CENTER)**2)

# 2. MAIN SIMULATION LOOP
particles_created = 0
while particles_created < TOTAL_PARTICLES:
    # a. Create new particle at random position on circle
    angle = np.random.random() * 2 * np.pi
    start_radius = 50  # Start closer to center
    x = int(CENTER + start_radius * np.cos(angle))
    y = int(CENTER + start_radius * np.sin(angle))
    
    stuck = False
    steps = 0
    
    while not stuck and steps < MAX_STEPS:
        # Move randomly
        direction = np.random.randint(1, 5)
        dx = dy = 0
        
        if direction == 1: dy = -1  # up
        elif direction == 2: dx = 1  # right
        elif direction == 3: dy = 1  # down
        elif direction == 4: dx = -1  # left

        new_x = x + dx
        new_y = y + dy
        
        # Check boundaries
        if new_x < 0 or new_x >= GRID_SIZE or new_y < 0 or new_y >= GRID_SIZE:
            continue
            
        # Check if too far from center
        if distance_from_center(new_x, new_y) > KILL_RADIUS:
            break  # Start a new particle
            
        x, y = new_x, new_y
        steps += 1
        
        # Only check for collisions if we're close to an existing particle
        if (grid[max(0, y-1):min(GRID_SIZE, y+2), max(0, x-1):min(GRID_SIZE, x+2)]).any():
            # Check for collisions
            if (y < GRID_SIZE-1 and grid[y+1, x] == 1) or \
               (y > 0 and grid[y-1, x] == 1) or \
               (x < GRID_SIZE-1 and grid[y, x+1] == 1) or \
               (x > 0 and grid[y, x-1] == 1):
                grid[y, x] = 1
                stuck = True
                particles_created += 1
                if particles_created % 10 == 0:  # Print every 10 particles
                    print(f"Particles created: {particles_created}")

# 3. VISUALIZATION
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
plt.imshow(grid, cmap='binary')
plt.axis('off')
plt.show()