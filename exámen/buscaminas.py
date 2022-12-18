import random

# The size of the grid
GRID_SIZE = 10

# The number of mines on the grid
NUM_MINES = 15

# The grid
grid = []

# Initialize the grid with all zeros
for i in range(GRID_SIZE):
  grid.append([0] * GRID_SIZE)

# Place the mines randomly on the grid
for i in range(NUM_MINES):
  row = random.randint(0, GRID_SIZE - 1)
  col = random.randint(0, GRID_SIZE - 1)
  grid[row][col] = '*'

# Count the number of mines in the 8 cells around each cell
for i in range(GRID_SIZE):
  for j in range(GRID_SIZE):
    if grid[i][j] == '*':
      continue

    count = 0
    for ii in range(i - 1, i + 2):
      for jj in range(j - 1, j + 2):
        if ii >= 0 and ii < GRID_SIZE and jj >= 0 and jj < GRID_SIZE and grid[ii][jj] == '*':
          count += 1

    grid[i][j] = count

# Print the grid
for row in grid:
  print(row)
