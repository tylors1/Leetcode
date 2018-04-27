# terminal tic tac toe game
import sys

board = [[None, None, None],
		[None, None, None],
		[None, None, None]]
count = 0

def get_play():
	row = raw_input("Enter row: ")
	col = raw_input("Enter col: ")
	if row.isdigit() and col.isdigit():
		row, col = int(row), int(col)
		if row < 3 and col < 3 and board[row][col] == None:
			return row, col
	print "Try entering again..."
	return get_play()

def play(char, row, col):
	board[row][col] = char

def print_board():
	for row in board:
		print row

def check_win():
	for row in board:
		if row[0] != None and all(item == row[0] for item in row):
			return row[0]

	# column check by transposing board
	for col in zip(*board):
		if col[0] != None and all(item == col[0] for item in col):
			return col[0]

	# diagonal check
	if board[1][1] != None:
		if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
			return board[1][1]


# main
print "x goes first!"
while count < 9:
	print_board()
	print
	if count % 2 == 0:
		print "x turn"
		row, col = get_play()
		play('x', row, col)
	else:
		print "o turn"
		row, col = get_play()
		play('o', row, col)
	count += 1
	win = check_win()
	print win
	if win != None:
		print win, "wins!"
		print
		print_board()
		sys.exit()