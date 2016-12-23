from pprint import pprint

def generate_next_board_state(board):
    return board

board = []
iteration = 0
size = 20
for i in range(size):
    board.append([0 for i in range(size)])

while (iteration < 3):
    pprint(board)
    board = generate_next_board_state(board)
    iteration += 1
