# This program generates a random maze using recursive backtracking and solves it using depth-first search (DFS).cls
import random
import sys
sys.setrecursionlimit(10000)

# Maze dimensions
WIDTH = 41
HEIGHT = 21

# Cells
WALL = 1
PATH = 0
VISITED = 2

# Directions for movement (up, down, left, right)
DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Entry and exit
start_x, start_y = 1, 1
end_x, end_y = HEIGHT - 2, WIDTH - 2

# Check if the coordinates are valid 
def is_valid(x, y):
    return 0 < x < HEIGHT - 1 and 0 < y < WIDTH - 1

# Print the maze
def print_maze(m):
    for i in range(HEIGHT):
        row = ''
        for j in range(WIDTH):
            if (i, j) == (start_x, start_y):
                row += 'S'
            elif (i, j) == (end_x, end_y):
                row += 'E'
            elif m[i][j] == WALL:
                row += '█'
            elif m[i][j] == VISITED:
                row += '░'
            else:
                row += ' '
        print(row)

# DFS logic to generate maze
def generate_maze(x, y, maze):
    maze[x][y] = PATH
    random.shuffle(DIRS)
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and maze[nx][ny] == WALL:
            maze[x + dx // 2][y + dy // 2] = PATH
            generate_maze(nx, ny, maze)

# DFS logic to solve maze
def solve_maze(x, y, end_x, end_y, maze):
    if not is_valid(x, y) or maze[x][y] != PATH:
        return False
    if (x, y) == (end_x, end_y):
        maze[x][y] = VISITED
        return True
    maze[x][y] = VISITED
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        if solve_maze(x + dx, y + dy, end_x, end_y, maze):
            return True
    maze[x][y] = PATH  # Backtrack
    return False

while True:
    maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]
    generate_maze(start_x, start_y, maze)
    print("\nGenerated Maze (S = Start, E = End):")
    print_maze(maze)
    print("\nSolving Maze...")
    if solve_maze(start_x, start_y, end_x, end_y, maze):
        print("\nSolved Maze (░ = Solution Path):")
        print_maze(maze)
    else:
        print("No solution found.")
    again = input("\nGenerate another maze? (y/n): ").lower()
    if again != 'y':
        print("Program ended.")
        break
