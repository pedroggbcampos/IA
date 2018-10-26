import copy
from search import *
import time



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
     return get_heuristic(node.state.board)



#print(sol_state([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])>sol_state([["_","O","_","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))

#print(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).result(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]),[(3, 0), (3, 2)]).board)

#print(sol_state([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])>sol_state([["_","O","_","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))

#print(solitaire([["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]]))


board1 = [["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]

board2 = [["O","O","O","X"],["O","O","O","O"],["O","_","O","O"],["O","O","O","O"]]

board3 = [["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]]

board4 = [["O","O","O","X","X","X"],["O","_","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]

boards_list = []
boards_list.append(board1)
boards_list.append(board2)
boards_list.append(board3)
boards_list.append(board4)
print(len(boards_list))

searchers = [depth_first_graph_search, greedy_search, astar_search]
for searchy in searchers:
	print(str(searchy))
	for board in boards_list:
	    start_time = time.time()
	    print(searchy(solitaire(board)))
	    print("--- %s seconds ---" % (time.time() - start_time))
	print("\n\n")


#print(greedy_search(solitaire(board2)))

#print(greedy_search(solitaire(board3)))

#print(greedy_search(solitaire(board4)))
