#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    # print("")
    # print("posr", posr)
    # print("posc", posc)
    # print("board", board)
    
    # h_move = ""
    # for vert in range(len(board)):
    #     for cell_in_h in range(len(board[posr])):
    #         # print(board[posr][cell_in_h])
    #         if(board[posr][cell_in_h] == "d"):
    #             h_move = cell_in_h - posc
    #             if(h_move > 0):
    #                 print("RIGHT" * abs(h_move))
    #                 posc += abs(h_move)
    #                 print("CLEAN")
    #             if(h_move < 0):
    #                 print("LEFT" * abs(h_move))
    #                 posc -= abs(h_move)
    #                 print("CLEAN")
    #             if(h_move == 0):
    #                 print("CLEAN")
    #     posr += 1
    #     print("DOWN")
    
    # ONLY ONE MOVE PER TURN
    next_move = ""
    mini_move = len(board[0])
    for cell_in_h in range(len(board[posr])):
        if(board[posr][cell_in_h] == "d"):
            h_move = cell_in_h - posc
            if(abs(h_move) < mini_move):
                mini_move = abs(h_move)
                if(h_move > 0):
                    next_move = "RIGHT"
                if(h_move < 0):
                    next_move = "LEFT"
                if(h_move == 0):
                    next_move = "CLEAN"
    if(next_move != ""):
        print(next_move)
    else:
        print("DOWN")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
