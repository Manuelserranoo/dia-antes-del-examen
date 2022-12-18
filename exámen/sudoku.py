board =[
  ["5","0","0","0","4","0","0","0","9"],["0","2","0","0","1","0","6","8","0"],["0","0","9","8","7","0","1","0","0"],["0","0","6","7","0","0","2","0","6"],["0","9","0","3","5","4","0","6","0"],["3","0","0","0","0","0","0","0","1"],["0","1","4","0","3","0","0","5","7"],["0","0","5","0","8","7","0","0","0"]]
def solve(board):
  """
  Solves a Sudoku board using backtracking.

  Parameters:
  board: a list of lists representing the Sudoku board. Empty cells are represented
         with the value 0.

  Returns:
  True if the board is solvable, False otherwise.
  """

  # Find the next empty cell
  empty_cell = find_empty_cell(board)
  if not empty_cell:
    # No empty cells, the board is solved
    return True

  row, col = empty_cell

  # Try filling the empty cell with a number from 1 to 9
  for num in range(1, 10):
    if is_valid_move(board, row, col, num):
      # The move is valid, make it and recursively try to solve the rest of the board
      board[row][col] = num
      if solve(board):
        return True

      # The move didn't lead to a solution, backtrack
      board[row][col] = 0

  # No solution found
  return False

def find_empty_cell(board):
  """
  Finds the next empty cell on the board.

  Parameters:
  board: a list of lists representing the Sudoku board.

  Returns:
  A tuple (row, col) representing the row and column indices of the next empty cell,
  or None if there are no empty cells.
  """
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j)
  return None

def is_valid_move(board, row, col, num):
  """
  Determines if it is valid to place the given number on the given cell.

  Parameters:
  board: a list of lists representing the Sudoku board.
  row: the row index of the cell.
  col: the column index of the cell.
  num: the number to place on the cell.

  Returns:
  True if the move is valid, False otherwise.
  """
  # Check if the number is already in the row
  if num in board[row]:
    return False

  # Check if the number is already in the column
  for i in range(len(board)):
    if board[i][col] == num:
      return False

  # Check if the number is already in the 3x3 subgrid
  subgrid_row = row // 3
  subgrid_col = col // 3
  for i in range(subgrid_row * 3, subgrid_row * 3 + 3):
    for j in range(subgrid_col * 3, subgrid_col * 3 + 3):
      if board[i][j] == num:
        return False

  # The number is not in the row, column, or subgrid, the move is valid
  return True
print(solve(board))