"""
Chess is the oldest game, but it is still popular these days. For this task, we will use only one chess piece - the Knight.
The knight moves to the nearest square but not on the same row, column, or diagonal. (This can be thought of as moving
two squares horizontally, then one square vertically, or moving one square horizontally then two squares vertically - i.e.
in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with K for knights and '0' for empty cells. Your task is to remove knights until there are no
knights left that can attack one another.

Input    Output
5           1
0K0K0
K000K
00K00
K000K
0K0K0
"""


def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knight = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_position = [row + rows[i], col + cols[i]]
        if is_valid(current_position, size) and board[current_position[0]][current_position[1]] == "K":
            killed_knight += 1
    return killed_knight


n = int(input())
board = []
total_kills = 0

for _ in range(n):
    board.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]
    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = "0"
    total_kills += 1

print(total_kills)
