import sys

sys.setrecursionlimit(1500)

goal = 'G'
start = 'S'
wall = '#'
path = '+'
open_path = '.'
bad = 'X'

curr_path = ''
path_list = []
path_lists = [] # Return from the get_commands function

# Mazes for testing
# maze1 = [ ['S','.','.','.','#','#'], \
#          ['#','.','#','.','.','.'], \
#          ['#','.','#','#','.','#'], \
#          ['#','.','#','.','#','#'], \
#          ['#','.','.','.','#','G'], \
#          ['#','.','#','.','.','.'] ]
# maze2 = [
#             ['S','#','G'], \
#             ['.','#','.'], \
#             ['.','.','.']
#         ]
maze_str = 'S1,W,G1,E,W,E,E,E,E,W,W,W,E,E,E,E,W,E,G2,W,S2'
# maze_str = 'S,#,G,.,#,.,.,.,.'

rows = '7'
cols = '3'

def str_to_maze(maze_str, rows, cols):
    curr = 0
    col = cols
    maze = []
    row = []
    maze_str = maze_str.split(',')

    while rows > 0:
        row = maze_str[curr:col]
        maze.append(row)
        curr += cols
        col += cols
        rows -= 1

    return maze

# row & col of goal
def find_path(maze, row, col):
    global path_list
    if col < 0 or col > len(maze[0]) - 1 or row < 0  or row > len(maze) - 1 or maze[row][col] is start\
        or maze[row][col] is wall or maze[row][col] is bad or maze[row][col] is path:
        return False
    if maze[row][col] == goal:
        return True
    
    if maze[row][col] != start:
        maze[row][col] = path
        
    path_list.append('N')
    if find_path(maze, row - 1, col):
        return True
    del path_list[-1]
    path_list.append('W')
    if find_path(maze, row , col - 1):
        return True
    del path_list[-1]
    path_list.append('S')
    if find_path(maze, row + 1, col):
        return True
    del path_list[-1]
    path_list.append('E')
    if find_path(maze, row, col + 1):
        return True
    maze[row][col] = bad
    del path_list[-1]
    return False
            

def show_maze(maze):
    maze_row = ""
    for row in maze:
        for cell in row:
            maze_row += cell
        print(maze_row)
        maze_row = ""

def find_target(maze, target):
    cells = []
    for row in range(len(maze)):
        for cell in range(len(maze[0])):
            if maze[row][cell] == target:
                cells.append([row, cell])
    return cells

# Command to get commands. pass maze, number of rows & columns strings
def get_commands(maze_str, num_rows, num_cols):
    global rows
    global cols
    global path_list
    global path_lists
    global start
    global goal
    global open_path
    global wall

    rows = int(num_rows)
    cols = int(num_cols)
    maze = str_to_maze(maze_str, rows, cols)
    print(maze)

    start = 'S1'
    goal = 'G1'
    open_path = 'E'
    wall = 'W'

    goal_c = find_target(maze, start)
    print(goal_c)
    print(show_maze(maze))
    path = find_path(maze, goal_c[0][0], goal_c[0][1])
    print(show_maze(maze))
    print(path)
    print(maze)
    print(path_list)
    path_lists.append(path_list)

    start = 'S2'
    goal = 'G2'
    path_list = []

    goal_c = find_target(maze, start)
    print(goal_c)
    print(show_maze(maze))
    path = find_path(maze, goal_c[0][0], goal_c[0][1])
    # print(show_maze(maze))
    print(path)
    print(maze)
    print(path_list)
    path_lists.append(path_list)

    print('path lists: ',path_lists)

get_commands(maze_str)
print(path_lists)

# Testing function calls
# print(len(maze1))
# print(len(maze1[0]))

# print(find_target(maze1, start))
# print(find_target(maze1, goal))

# show_maze(maze2)
# print(find_path(maze1, 0, 0))
# show_maze(maze2)


# rows = int(rows)
# cols = int(cols)
# maze = str_to_maze(maze_str, rows, cols)
# print(maze)

# start = 'S1'
# goal = 'G1'
# open_path = 'E'
# wall = 'W'

# goal_c = find_target(maze, start)
# print(goal_c)
# print(show_maze(maze))
# path = find_path(maze, goal_c[0][0], goal_c[0][1])
# print(show_maze(maze))
# print(path)
# print(maze)
# print(path_list)
# path_lists.append(path_list)

# start = 'S2'
# goal = 'G2'
# path_list = []

# goal_c = find_target(maze, start)
# print(goal_c)
# print(show_maze(maze))
# path = find_path(maze, goal_c[0][0], goal_c[0][1])
# # print(show_maze(maze))
# print(path)
# print(maze)
# print(path_list)
# path_lists.append(path_list)

# print('path lists: ',path_lists)