from collections import deque

# ! not actually bfs; changed to dfs but didn't change names or comments !

# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# maze = [[0 ,0], [0, 0]]
# maze = [[0, 1], [1, 0]]
# maze = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
maze = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# maze = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0]]

for x in maze:
    print x



def memodict(f):
     """ Memoization decorator for a function taking a single argument """
     class memodict(dict):

        def __missing__(self, key):
           ret = self[key] = f(key)
           return ret
     return memodict().__getitem__


# get all neighbors of a point (x, y)
# lh - [row_max, col_max, x, y]
@memodict
def get_neighbors((bounds, point)):
    neighbors = ((point[0]-1, point[1]), (point[0]+1, point[1]), (point[0], point[1]-1), (point[0], point[1]+1))

    return [p for p in neighbors if 0 <= p[0] < bounds[0] and 0 <= p[1] < bounds[1]]


# checks if wall is removable
# a wall is removable if it's a wall (=1) and surrounded by at least 2 zeroes
def remove_wall_m(maze, len_table, len_table2, x_max, y_max, pos_x, pos_y):
    short1 = 9999
    short2 = 9999
    num_zeros = 0

    listholder = ((x_max, y_max), (pos_x, pos_y))

    for p in get_neighbors(listholder):
        if (maze[p[0]][p[1]] == 0):
            num_zeros += 1
            
            if len_table[p[0]][p[1]] < short1 and len_table[p[0]][p[1]] != -1:
                short1 = len_table[p[0]][p[1]]
            if len_table2[p[0]][p[1]] < short2 and len_table2[p[0]][p[1]] != -1:
                short2 = len_table2[p[0]][p[1]]  
    
    if num_zeros < 2:
        return -1

    return short1 + short2 + 1

def remove_wall_c(maze, len_table, converter, x_max, y_max, pos_x, pos_y): 
    num_zeros = 0
    short1 = 9999
    short2 = 0

    listholder = ((x_max, y_max), (pos_x, pos_y))

    for p in get_neighbors(listholder):
        if (maze[p[0]][p[1]] == 0):
            num_zeros += 1

            if len_table[p[0]][p[1]] < short1 and len_table[p[0]][p[1]] != -1:
                short1 = len_table[p[0]][p[1]]
            if len_table[p[0]][p[1]] > short2 and len_table[p[0]][p[1]] != -1:
                short2 = len_table[p[0]][p[1]]

    if num_zeros < 2:
        return -1

    short2 = converter - short2         
    return short1 + short2 + 1


def bfs_maze(maze, result_matrix, start, end):
    q = deque()                                 # queue for bfs
    x_max = len(maze)                           # bounds of the maze
    y_max = len(maze[0])
    path_len = 0                                # current path length

    # status matrix: 0 is unvisited, 1 is visted
    stat_mtrx = [[0] * y_max for _ in xrange(x_max)]

    q.append(start)
    
    # while queue is not empty
    while q:
        # get the next point from queue (insert at end, pop off beginning)
        curr_pos = q.pop()

        # if at (0, 0), then current format of maze is finished
        if curr_pos == end:
            break

        # for each neighbor that is not a wall
        # change the neighbors' path length as current + 1 if appropriate
        # if next point is unvisited, add to queue
        listholder = ((x_max, y_max), (curr_pos[0], curr_pos[1]))
        for x, y in get_neighbors(listholder):
            if (maze[x][y] == 0):
                path_len = result_matrix[curr_pos[0]][curr_pos[1]] + 1

                if path_len < result_matrix[x][y] or result_matrix[x][y] == -1:
                    result_matrix[x][y] = path_len

                if stat_mtrx[x][y] != 1:
                    q.append((x, y))

        # mark current point as visited         
        stat_mtrx[curr_pos[0]][curr_pos[1]] = 1

    return result_matrix[end[0]][end[1]]


def answer(maze):
    x_max = len(maze)                           # bounds of the maze
    y_max = len(maze[0])

    # path length matrix for bfs starting at top left
    start_matrix = [[-1] * y_max for _ in xrange(x_max)]
    start_matrix[0][0] = 1

    shortest = bfs_maze(maze, start_matrix, (0, 0), (x_max - 1, y_max - 1))

    if (shortest == -1):
        shortest = 9999

        # path length matrix for bfs starting at bottom right
        end_matrix = [[-1] * y_max for _ in xrange(x_max)]
        end_matrix[x_max - 1][y_max - 1] = 1

        bfs_maze(maze, end_matrix, (x_max - 1, y_max - 1), (0, 0))

        # get all removable walls in maze
        for i in xrange(x_max):
            for j in xrange(y_max):
                if maze[i][j] == 1: 
                    rem_wall = remove_wall_m(maze, start_matrix, end_matrix, x_max, y_max, i, j)
                    if (rem_wall < shortest and rem_wall != -1):
                        shortest = rem_wall

    else:
        converter = shortest + 1

        # get all removable walls in maze
        for i in xrange(x_max):
            for j in xrange(y_max):
                if maze[i][j] == 1: 
                    rem_wall = remove_wall_c(maze, start_matrix, converter, x_max, y_max, i, j)
                    if (rem_wall < shortest and rem_wall != -1):
                        shortest = rem_wall

    return shortest

print answer(maze)







