#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
#import statistics
#import time
import sys

ROW = "ABCDEFGHI"
COL = "123456789"

VAL = (1, 2, 3, 4, 5, 6, 7, 8, 9)

BOX_1 = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')
BOX_2 = ('A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6')
BOX_3 = ('A7', 'A8', 'A9', 'B7', 'B8', 'B9', 'C7', 'C8', 'C9')
BOX_4 = ('D1', 'D2', 'D3', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3')
BOX_5 = ('D4', 'D5', 'D6', 'E4', 'E5', 'E6', 'F4', 'F5', 'F6')
BOX_6 = ('D7', 'D8', 'D9', 'E7', 'E8', 'E9', 'F7', 'F8', 'F9')
BOX_7 = ('G1', 'G2', 'G3', 'H1', 'H2', 'H3', 'I1', 'I2', 'I3')
BOX_8 = ('G4', 'G5', 'G6', 'H4', 'H5', 'H6', 'I4', 'I5', 'I6')
BOX_9 = ('G7', 'G8', 'G9', 'H7', 'H8', 'H9', 'I7', 'I8', 'I9')

BOXES = {}
for i in range(9) :
    BOXES[BOX_1[i]] = BOX_1
    BOXES[BOX_2[i]] = BOX_2
    BOXES[BOX_3[i]] = BOX_3
    BOXES[BOX_4[i]] = BOX_4
    BOXES[BOX_5[i]] = BOX_5
    BOXES[BOX_6[i]] = BOX_6
    BOXES[BOX_7[i]] = BOX_7
    BOXES[BOX_8[i]] = BOX_8
    BOXES[BOX_9[i]] = BOX_9  


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    if board_to_string(board).count('0') == 0 :
        return board

    var = MRV()
    for value in VAL :
        if consistent(var, value, board) :
            board[var] = value
            result = backtracking(board)
            if result != False :
                return result
            board[var] = 0

    return False


def MRV() :
    mrv = 0
    var = None

    for v in board :
        if board[v] == 0 :
            row = v[0]
            col = v[1]
            box = BOXES[v]
            count = set()

            for c in range(1,10) :
                if board[row + str(c)] != 0 :
                    count.add(board[row + str(c)])

            for r in range(ord('A'), ord('J')) :
                if board[chr(r) + col] != 0 :
                    count.add(board[chr(r) + col])

            for sqr in box : 
                if board[sqr] != 0 :
                    count.add(board[sqr])

            if len(count) > mrv :
                mrv = len(count)
                var = v

    return var


def consistent(var, value, board) :
    row = var[0]
    col = var[1]
    box = BOXES[var]

    for c in range(1,10) :
        if board[row + str(c)] == value :
            return False

    for r in range(ord('A'), ord('J')) :
        if board[chr(r) + col] == value :
            return False

    for sqr in box : 
        if board[sqr] == value :
            return False

    return True

if __name__ == '__main__':
    #  Read boards from source.
    sudoku_list = sys.argv[1];
    #src_filename = 'sudokus_start.txt'
    #try:
        #srcfile = open(src_filename, "r")
        #sudoku_list = srcfile.read()
    #except:
        #print("Error reading the sudoku file %s" % src_filename)
        #exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    #runtimes = []

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        #print_board(board)
        #start_time = time.time()

        # Solve with backtracking
        solved_board = backtracking(board)

        #total_time = time.time() - start_time
        #runtimes.append(total_time)

        # Print solved board. TODO: Comment this out when timing runs.
        #print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")
    #print("number: " + str(len(runtimes)))
    #print("min: " + str(min(runtimes)))
    #print("max: " + str(max(runtimes)))
    #print("mean: " + str(statistics.mean(runtimes)))
    #print("std_dev: " + str(statistics.stdev(runtimes)))