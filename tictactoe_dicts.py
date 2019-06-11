# check winner of board
def checkWinner(board):
    if board[1] == board[2] == board[3] != ' ': # matches top row
        return 1
    elif board[1] == board[5] == board[9] != ' ': # matches diagnally from top left
        return 1
    elif board[1] == board[4] == board[7] != ' ': # matches left column
        return 1
    elif board[4] == board[5] == board[6] != ' ': # matches middle row
        return 1
    elif board[7] == board[5] == board[3] != ' ': # matches diagnoally from bottom left
        return 1
    elif board[7] == board[8] == board[9] != ' ': # matches bottom row
        return 1
    elif board[2] == board[5] == board[8] != ' ': # matches middle column
        return 1
    elif board[3] == board[6] == board[9] != ' ': # matches right column
        return 1
    else:
        return 0

# prints board
def printBoard(board):
    print(board[1] + '|' + board[2] + "|" + board[3] + '    1|2|3')
    print('-+-+-    -+-+-')
    print(board[4] + '|' + board[5] + "|" + board[6] + '    4|5|6')
    print('-+-+-    -+-+-')
    print(board[7] + '|' + board[8] + "|" + board[9] + '    7|8|9')

# generates a dictionary for board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

turn = 'X' # sets initial turn
printBoard(board)
result = checkWinner(board)
turnCount = 0

# runs until someone wins or all slots are filled
while result == 0 and turnCount < 9:
    move = input('Turn for ' + turn + '. Pick a space for the move: ')
    turnCount += 1
    board[int(move)] = turn
    result = checkWinner(board)
    printBoard(board)    
    if result == 1: # if there's a winner
        print(turn + " wins!")
        continue
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
