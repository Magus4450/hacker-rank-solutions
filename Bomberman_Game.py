""""
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell , any valid cells  and  are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

1. Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
2. After one second, Bomberman does nothing.
3. After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
4. After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
5. Bomberman then repeats steps 3 and 4 indefinitely.

Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after  seconds.

For example, if the initial grid looks like:
...
.O.
...

it looks the same after the first second. After the second second, Bomberman has placed all his charges:
OOO
OOO
OOO


At the third second, the bomb in the middle blows up, emptying all surrounding cells:
O.O
...
O.O
"""

# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# Function to print the board in readable way
def print_grd(arr):
    for row in arr:
        for num in row:
            print(num, end=" ")
        print("")
    print("")
    print("-"*10)
    print("")


def bomberMan(n, grid):
    r = len(grid)                                   # Rows
    c = len(grid[0])                                # Columns
    bomb_coord = grid[:]                            # Copying bombs into new grid
    for sec in range(1,n+1):        
        if sec % 3 == 1:            
            bomb_coord = grid[:]                    # Copying bombs into new grid
        elif sec % 3 == 2:
            grid = ['O' * c for _ in range(r) ]     # Putting bombs in all space of grid
        elif sec % 3 == 0:
            for i in range(r):
                for j in range(c):
                    
                    if bomb_coord[i][j] == grid[i][j] and grid[i][j] == "O": # If Bomb
                        grid[i] = grid[i][:j] + '.' + grid[i][j+1:] 
                        if(j < c-1):
                            grid[i] = grid[i][:j+1] + '.' + grid[i][j+2:]  
                        if(j>0):
                            grid[i] = grid[i][:j-1] + '.' + grid[i][j:]  
                        if(i > 0):
                            grid[i-1] = grid[i-1][:j] + '.' + grid[i-1][j+1:] 
                        if(i < r-1):
                            grid[i+1] = grid[i+1][:j] + '.' + grid[i+1][j+1:] 
    return grid

if __name__ == "__main__":
    gridd =['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
    n = 3
    
    print_grd(bomberMan(n, gridd))
