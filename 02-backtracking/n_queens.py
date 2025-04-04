def solve_n_queens(n):
  solutions = []
  board = []

  def is_safe(row, col):
    for r, c in enumerate(board):
      if c == col or abs(r - row) == abs(c - col):
        return False

    return True

  def backtrack(row):
    if row == n:
      solutions.append(board[:])
      return
    
    for col in range(n):
      if is_safe(row, col):
        board.append(col)
        backtrack(row + 1)
        board.pop()

  backtrack(0)
  return solutions

print(solve_n_queens(4))
