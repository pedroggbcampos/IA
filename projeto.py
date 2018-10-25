import copy
from search import *



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

#DeepCopy
def make_board_copy(board):
 return copy.deepcopy(board)



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
"""
b1 = [["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","_","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"]]
"""
#print(board_moves(b1))




def board_perform_move(board, move): #exemplo de move [(0,2), (0,0)]
 """ FAZ UMA DEEP COPY PARA NAO ALTERAR DIRETAMENTE O BOARD """
 aux = make_board_copy(board)
 aux[pos_l(move_initial(move))][pos_c(move_initial(move))] = c_empty()
 aux[pos_l(move_final(move))][pos_c(move_final(move))] = c_peg()
 if pos_l(move_initial(move)) == pos_l(move_final(move)):
  aux[pos_l(move_initial(move))][(pos_c(move_initial(move)) + pos_c(move_final(move)))//2] = c_empty()
 else:
  aux[(pos_l(move_initial(move)) + pos_l(move_final(move)))//2][pos_c(move_initial(move))] = c_empty()
 return aux

"""
b1 = [["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","_","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["O","O","O","O","O","O","O","O","O"],
 ["X","X","O","O","O","O","O","X","X"],
 ["X","X","O","O","O","O","O","X","X"]]

b2 = [["X","O","O","O","X"],["O","O","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["X","O","_","_","X"]]
"""

def get_peg_number(Board):
    sum = 0
    for x in Board:
        sum += x.count(c_peg())
    return sum

def get_heuristic(Board):
	"""
	sum = 0
	counter = 0
	if get_peg_number(Board) == 1:
		return 0
	for x in Board:
	    if counter == 0:
	        sum += x.count(c_peg())
	    elif counter == len(Board) - 1:
	        sum += x.count(c_peg())
	    else:
	        if is_peg(x[0]):
	            sum += 1
	        if is_peg(x[-1]):
	            sum += 1
	        for i in range (1, len(x) - 1):
	        	if is_blocked(pos_cont(Board, make_pos(counter + 1, i))) or is_blocked(pos_cont(Board, make_pos(counter - 1, i))) or is_blocked(pos_cont(Board, make_pos(counter, i + 1))) or is_blocked(pos_cont(Board, make_pos(counter, i - 1))):
	        		sum += 1
	    sum += x.count(c_peg())
	    counter += 1
	    """
	peg_positions = []
	pegs = get_peg_number(Board)
	if pegs == 1:
		return 0
	moves = board_moves(Board)
	for move in moves:
		if move[0] not in peg_positions:
			peg_positions.append(move[0])


	return 2*pegs - len(peg_positions)

	"""
	pegs = get_peg_number(Board)

	if pegs == 1:
		return 0

	movable = []
	allMoves = board_moves(Board)
	for move in allMoves:
		if move_initial(move) not in movable:
			movable.append(move_initial(move))

	
	return pegs + (pegs - len(movable))
	"""
	
	
	
    
##    nr_lines = board_lines(Board)
##    nr_col = board_columns(Board)
##        for c in range (1, nr_col - 1):
##            if not is_peg(pos_cont(Board, make_pos(l + 1, c))) and not is_peg(pos_cont(Board, make_pos(l - 1, c))) and not is_peg(pos_cont(Board, make_pos(l, c + 1))) and not is_peg(pos_cont(Board, make_pos(l, c - 1))):
##                and not is_peg(pos_cont(Board, make_pos(l +1 , c + 1))) and not is_peg(pos_cont(Board, make_pos(l + 1, c - 1))) and not is_peg(pos_cont(Board, make_pos(l - 1, c + 1))) and not is_peg(pos_cont(Board, make_pos(l - 1, c - 1))):
##                sum += 1
##    return sum


class sol_state:

    def __init__(self, b):
        self.board = b
        self.peg_nr = get_peg_number(b)


    def __lt__(self, other_sol_state):
        #return self.peg_nr > other_sol_state.peg_nr
        return self.board < other_sol_state.board




class solitaire(Problem):
    """Models a Solitaire problem as a satisfaction
 problem.
       A solution cannot have more than 1 peg left
on the board. """
    def __init__(self, board):
     self.initial = sol_state(board)

    def actions(self, state):
        return board_moves(state.board)

    def result(self, state, action):
     return sol_state(board_perform_move(state.board, action))

    def goal_test(self, state):
        return state.peg_nr == 1
        #return get_peg_number(state.board) == 1

    def path_cost(self, c, state1, action, state2):
        return c+1

    def h(self, node):
     #return node.state.peg_nr -1
     return get_heuristic(node.state.board)
        #pass
     """Needed for informed search."""


#print(sol_state([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])>sol_state([["_","O","_","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))

#print(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).result(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]),[(3, 0), (3, 2)]).board)

#print(sol_state([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])>sol_state([["_","O","_","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))


#print(greedy_search(solitaire([["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]])))

#print(solitaire([["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]]))


"""
class solitaire(Problem):
    Models a Solitaire problem as a satisfaction
 problem.
       A solution cannot have more than 1 peg left
on the board.
    def __init__(self, board):
        ...
    def __lt__(self, <other sol_state>):
    ...
 """
