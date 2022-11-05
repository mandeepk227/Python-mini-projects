import numpy as np
sudoku = []
print('Please represent blanks with 0')
for i in range(9):
  row = list(input(f'Enter numbers for {i+1} row without any space or comma: '))
  row = [int(i) for i in row]
  sudoku.append(row)

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col =find

    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col]=i
            if solve(board):
                return True
            board[row][col]=0

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)
    return None

# Checking if the board is valid or not

def valid(board, num, pos):
    # checking rows
    for i in range(len(board[0])):
        if board[pos[0]] [i] == num and pos[1] !=i:
            return False

    # checking columns
    for i in range(len(board)):
        if board[i] [pos[1]] == num and pos[0] !=i:
            return False
    
    # checking box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x*3 , box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == num and (i,j) !=pos :
                return False
    return True


def print_board(board):
  for i in range(len(board)):
    if i%3 == 0 and i!=0:
      print("- - - - - - - - - - - - - - - -")
    for j in range(len(board[0])):
      if j%3 == 0 and j!=0:
        print('|  ', end='')
      if j == 8 :
        print(board[i][j])
      else:
        print((board[i][j]),' ', end='')
  
print_board(sudoku)
solve(sudoku)
print('====================================')
print_board(sudoku)


