board = [' '] * 9

def draw_board():
  print(f' {board[0]} | {board[1]} | {board[2]} ')
  print('-----------')
  print(f' {board[3]} | {board[4]} | {board[5]} ')
  print('-----------')
  print(f' {board[6]} | {board[7]} | {board[8]} ')

def computer_move():
  best_score = -float('inf')
  best_move = None
  for i in range(9):
    if board[i] == ' ':
      board[i] = 'X'
      score = minimax(board, False)
      board[i] = ' '
      if score > best_score:
        best_score = score
        best_move = i
  board[best_move] = 'X'

def minimax(board, is_maximizing):
  winner = check_winner()
  if winner == 'O':
    return -1
  elif winner == 'X':
    return 1
  elif ' ' not in board:
    return 0

  if is_maximizing:
    best_score = -float('inf')
    for i in range(9):
      if board[i] == ' ':
        board[i] = 'X'
        score = minimax(board, False)
        board[i] = ' '
        best_score = max(score, best_score)
    return best_score
  else:
    best_score = float('inf')
    for i in range(9):
      if board[i] == ' ':
        board[i] = 'O'
        score = minimax(board, True)
        board[i] = ' '
        best_score = min(score, best_score)
    return best_score

def player_move():
  move = input("Wprowadz numer (1-9): ")
  try:
    move = int(move) - 1
    if move in range(9) and board[move] == ' ':
      board[move] = 'O'
    else:
      print("------Bład!------ Prosze wybrac inny numer.")
      player_move()
  except ValueError:
    print("------Bład!------ Prosze wybrac numer od 1-9.")
    player_move()

def check_winner():
  winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
  ]
  for combination in winning_combinations:
    if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != ' ':
      return board[combination[0]]
  return None

def main():
  draw_board()
  while True:
    computer_move()
    draw_board()
    winner = check_winner()
    if winner:
      print("Przegrana")
      break
    elif ' ' not in board:
      print("Remis")
      break
    player_move()
    draw_board()
    winner = check_winner()
    if winner:
      print("Wygrana")
      break

main()