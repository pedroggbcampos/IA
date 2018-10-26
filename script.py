#Boards and functions to test the complexity of the algorithms used
from search import *
from projeto import *

board1 = [["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]] 

board2 = [["O","O","O","X"],["O","O","O","O"],["O","_","O","O"],["O","O","O","O"]]

board3 = [["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]]

board4 = [["O","O","O","X","X","X"],["O","_","O","O","O","O"],["O","O","O","O","O","O"],["O","O","O","O","O","O"]]

problems = [solitaire(board1), solitaire(board2), solitaire(board3), solitaire(board4)]
searchers = [depth_first_graph_search, greedy_search, astar_search]
header = None
def compare_searchers(problems, header, searchers):
    def do(searcher, problem):
        p = InstrumentedProblem(problem)
        if(searcher == greedy_search):
            searcher(p,p.h)

        elif(searcher == astar_search):
            searcher(p)
        else:
            searcher(p)
        #searcher(p)
        print('done')
        return p
    table = [[name(s)] + [do(s, p) for p in problems] for s in searchers]
    print_table(table, header)
def compare_graph_searchers():
    compare_searchers(problems, header, searchers)
compare_graph_searchers()