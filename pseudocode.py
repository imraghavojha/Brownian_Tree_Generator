# Pseudocode for DLA Simulation

# 1. INITIALIZATION
- Create empty grid (numpy array of zeros)
- Place initial particle in center of grid
- Set simulation parameters:
    * Grid size (N x N)
    * Number of particles to simulate
    * Distance from cluster to spawn new particles

# 2. MAIN SIMULATION LOOP
- While particles_created < total_particles:
    a. Create new particle at random position on perimeter
    b. While particle is not stuck:
        - Move particle randomly (up, down, left, or right)
        - Check if particle touches cluster
        - Check if particle is out of bounds
    c. If particle touches cluster:
        - Add it to the grid (mark as 1)
        - Update cluster

# 3. VISUALIZATION
- Display/update grid showing cluster growth