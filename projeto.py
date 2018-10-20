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


def get_peg_number(Board):
    sum = 0
    for x in Board:
        sum += x.count(c_peg())
    return sum

class sol_state: 

    def __init__(self, b): 
        self.board = b
        self.peg_nr = get_peg_number(b)

        
    def __lt__(self, other_sol_state):
        return self.peg_nr < other_sol_state.peg_nr 


 

class solitaire(Problem): 
    """Models a Solitaire problem as a satisfaction
 problem. 
       A solution cannot have more than 1 peg left 
on the board. """ 
    def __init__(self, board): 
        self.board = board

    def actions(self, state): 
        return board_moves(state.board) 

    def result(self, state, action): 
        self.board = board_perform_move(state.board, action)
         
    def goal_test(self, state):
        return state.peg_nr == 1

    def path_cost(self, c, state1, action, state2):
        pass 
    def h(self, node): 
        
        pass
        """Needed for informed search.""" 


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