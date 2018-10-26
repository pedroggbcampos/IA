#Antonio Vieira 86387     Pedro Campos 86494   grupo 071


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





def board_perform_move(board, move): 
 """ FAZ UMA DEEP COPY PARA NAO ALTERAR DIRETAMENTE O BOARD """
 aux = make_board_copy(board)
 aux[pos_l(move_initial(move))][pos_c(move_initial(move))] = c_empty()
 aux[pos_l(move_final(move))][pos_c(move_final(move))] = c_peg()
 if pos_l(move_initial(move)) == pos_l(move_final(move)):
  aux[pos_l(move_initial(move))][(pos_c(move_initial(move)) + pos_c(move_final(move)))//2] = c_empty()
 else:
  aux[(pos_l(move_initial(move)) + pos_l(move_final(move)))//2][pos_c(move_initial(move))] = c_empty()
 return aux



def get_peg_number(Board):
    sum = 0
    for x in Board:
        sum += x.count(c_peg())
    return sum

def get_heuristic(Board):
 pegs = get_peg_number(Board)
 if pegs == 1:
  return 0
 moves_para_centro = []
 meio_linha = board_lines(Board)//2
 meio_coluna = board_columns(Board)//2
 moves = board_moves(Board)
 for move in moves:
  if math.fabs(meio_linha - move[1][0]) + math.fabs(meio_coluna - move[1][1]) <= ((meio_linha + meio_coluna)//2) :
   moves_para_centro.append(move[1])

 return pegs + (pegs - len(moves_para_centro))



class sol_state:

    def __init__(self, b):
        self.board = b
        self.peg_nr = get_peg_number(b)


    def __lt__(self, other_sol_state):
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

    def path_cost(self, c, state1, action, state2):
        return c+1

    def h(self, node):
     return get_heuristic(node.state.board)

