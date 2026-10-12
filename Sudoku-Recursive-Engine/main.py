import random

def create_empty_board():
  return [[0 for _ in range(9)] for _ in range(9)]
def print_board(board):
  print("\n--- Valid Sudoku Board ---\n")
  for row in range(9):
    if row % 3 == 0 and row != 0:
      print("- - - - - - - - - - - - - ")
    for col in range(9):
      if col % 3 == 0 and col != 0:
        print(" | ", end="")
      if col == 8:
        print(board[row][col])
      else:
        print(str(board[row][col]) + " ", end="")
  print("\n--------------------------\n")
def is_valid(board, row, col, num):
  for i in range(9):
    if board[row][i] == num:
      return False
  for i in range(9):
    if board[i][col] == num:
      return False
  box_row_start = (row // 3) * 3
  box_col_start = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if board[box_row_start + i][box_col_start + j] == num:
        return False
  return True  
def fill_board(board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
          if is_valid(board, row, col, num):
            board[row][col] = num  
            if fill_board(board):
              return True
            board[row][col] = 0
        return False  
  return True  
my_board = create_empty_board()
fill_board(my_board)
print_board(my_board)
