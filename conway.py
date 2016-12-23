from pprint import pprint

def generate_next_board_state(board):
    return board

board = []
iteration = 0
size = 8
for i in range(size):
    board.append([0 for i in range(size)])

#Seed the first life-form
board[5][5] = 1

while (iteration < 3):
    pprint(board)
    print('\n')
    board = generate_next_board_state(board)
    iteration += 1
