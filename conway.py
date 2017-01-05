from pprint import pprint
from copy import copy

"""
Conway Rules:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

def generate_next_board_state(board):
    new_board = copy(board)
    for i in xrange(len(board)):
        for j in xrange(len(board)):
            count = count_alive_cells_near_cell(board, i, j)
            if board[i][j] == 1:
                if count < 2: new_board[i][j] = 0; # Rule 1
                if count > 3: new_board[i][j] = 0; # Rule 3
            if board[i][j] == 0:
                if count == 3: new_board[i][j] = 1;
    return new_board

def count_alive_cells_near_cell(board,x,y):
    alive_cells = []
    for i in [x-1,x+1]:
        for j in [y-1,y+1]:
            if(board[i % len(board)][j % len(board[0])] == 1):
                alive_cells.append([i,j])
    return len(alive_cells)

board = []
iteration = 0
size = 8
for i in range(size):
    board.append([0 for i in range(size)])

#Seed the first life-form
board[5][5] = 1
board[4][5] = 1

while (iteration < 3):
    pprint(board)
    print('\n')
    board = generate_next_board_state(board)
    iteration += 1
