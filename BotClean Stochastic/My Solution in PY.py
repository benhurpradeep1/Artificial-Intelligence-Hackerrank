def two_loops(board):
    for n in range(5):
        for m in range(5):
            if board[n][m] == 'd':
                return n,m
            
            
def nextMove(posr, posc, board):
    i,j = two_loops(board)
    
    if i < posr:
        print("UP")
    elif i > posr:
        print("DOWN")
    elif j < posc:
        print("LEFT")
    elif j > posc:
        print("RIGHT")
    else:
        print('CLEAN')
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
