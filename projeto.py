# TAI content
def c_peg ():
 return "O"
def c_empty ():
 return "_"
def c_blocked ():
 return "X"
def is_empty (e):
 return e == c_empty()
def is_peg (e):
 return e == c_peg()
def is_blocked (e):
 return e == c_blocked() 

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
 return (l, c)
def pos_l (pos):
 return pos[0]
def pos_c (pos):
 return pos[1] 

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
 return [i, f]
def move_initial (move):
 return move[0]
def move_final (move):
 return move[1]


def pos_cont(board, pos):
	return board[pos_l(pos)][pos_c(pos)]

def board_lines(board):
	return len(board)

def board_columns(board):
	return len(board[1])

def board_moves (board):
	moves = []
	nr_lines = board_lines(board)
	nr_col = board_columns(board)
	for l in range(0, nr_lines):
		for c in range (0, nr_col):
			if c < nr_col - 2:

				if is_empty(pos_cont(board, make_pos(l, c))) and is_peg(pos_cont(board, make_pos(l, c + 1))) and is_peg(pos_cont(board, make_pos(l, c + 2))):
					moves.append(make_move(make_pos(l, c + 2), make_pos(l, c)))

				elif is_peg(pos_cont(board, make_pos(l, c))) and is_peg(pos_cont(board, make_pos(l, c + 1))) and is_empty(pos_cont(board, make_pos(l, c + 2))):
					moves.append(make_move(make_pos(l, c), make_pos(l, c + 2)))

			if l < nr_lines - 2:

				if is_empty(pos_cont(board, make_pos(l, c))) and is_peg(pos_cont(board, make_pos(l + 1, c))) and is_peg(pos_cont(board, make_pos(l + 2, c))):
					moves.append(make_move(make_pos(l + 2, c), make_pos(l, c)))

				elif is_peg(pos_cont(board, make_pos(l, c))) and is_peg(pos_cont(board, make_pos(l + 1, c))) and is_empty(pos_cont(board, make_pos(l + 2, c))):
					moves.append(make_move(make_pos(l, c), make_pos(l + 2, c)))
	return moves

b1 = [["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","_","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"]]

print(board_moves(b1))
