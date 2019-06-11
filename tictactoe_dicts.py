def checkWinner(board):
    if board[1] == board[2] == board[3] != ' ':
        return 1
    elif board[1] == board[5] == board[9] != ' ':
        return 1
    elif board[1] == board[4] == board[7] != ' ':
        return 1
    elif board[4] == board[5] == board[6] != ' ':
        return 1
    elif board[7] == board[5] == board[3] != ' ':
        return 1
    elif board[7] == board[8] == board[9] != ' ':
        return 1
    elif board[2] == board[5] == board[8] != ' ':
        return 1
    elif board[3] == board[6] == board[9] != ' ':
        return 1
    else:
        return 0
    
def printBoard(board):
    print(board[1] + '|' + board[2] + "|" + board[3] + '    1|2|3')
    print('-+-+-    -+-+-')
    print(board[4] + '|' + board[5] + "|" + board[6] + '    4|5|6')
    print('-+-+-    -+-+-')
    print(board[7] + '|' + board[8] + "|" + board[9] + '    7|8|9')

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

while True:
    turn = input("Do you want to be 'X' or 'O'?")
    turn = turn.upper()
    if turn == 'X' or turn == 'O':
        break
        
printBoard(board)
result = checkWinner(board)
turnCount = 0
while result == 0 and turnCount < 9:
    while True:
        move = input('Turn for ' + turn + '. Pick a valid space for the move: ')
        if board[int(move)] == ' ':
            break
    turnCount += 1
    board[int(move)] = turn
    result = checkWinner(board)
    printBoard(board)    
    if result == 1:
        print(turn + " wins!")
        continue
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
