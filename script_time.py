from search import *
from projeto import *

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