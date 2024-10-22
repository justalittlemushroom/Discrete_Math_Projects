# turns decimal to binary
def toBinary(num):
    return bin(num)[2:]   
    
# gets the total number of rows on the present gameboard
def getNumRows():
    return len(game_board)

# displays the current gameboard
def getGameBoard():
    for row in range (1, getNumRows()):
        print(" " * (num_bits - len(toBinary((game_board[row])))) + toBinary(game_board[row]) + "\t" + str(game_board[row]) + "\t" + (' □' * game_board[row]))

# removes the given number of squares in the given row        
def removeSquares(row, num):
    game_board[row] = game_board[row] - num
    if game_board[row] <= 0:
        game_board.pop(row)

# updates the gameboard according to the player's inputted move
def getPlayerMove():
    rowToRemoveFrom = int(input("Enter Row to Remove Square From: "))
    squaresRemoved = int(input("Enter Number of Squares to Remove: "))
    if rowToRemoveFrom < getNumRows() and rowToRemoveFrom > 0 and squaresRemoved <= game_board[rowToRemoveFrom] and squaresRemoved > 0:
        removeSquares(rowToRemoveFrom, squaresRemoved)
    else:
        print("Invalid Input. Try Again.")
        getPlayerMove()

# calculates the best move for the computer to make
def calculateBestMove():
    balance = game_board[0]
    for i in range (0, getNumRows()):
        balance ^= game_board[i]
    if balance == 0:
        return [1, 1]
    else:
        print(balance)
        for row in range (1, getNumRows()):
            if game_board[row] > (balance ^ game_board[row]):
                print(balance ^ game_board[row])
                return [row, game_board[row] - (balance ^ game_board[row])]
    print("Board is Magic But Move Not Found")
    return [1, 1]

# updates the gameboard according to the computer's calculated move
def getComputerMove():
    computerMove = calculateBestMove()
    removeSquares(computerMove[0], computerMove[1])

# sets up the initial gameboard, taking in the number of rows and the number of squares in each row
game_board = []
game_board.append(0)
num_bits = 0

num_rows = int(input("Enter Number of Rows: "))
for i in range (1, num_rows + 1):
    num_squares = int(input("Enter Number of Squares for Row " + str(i) + ": "))
    game_board.append(num_squares)
    if len(toBinary(num_squares)) > num_bits:
       num_bits = len(toBinary(num_squares))

# prints directions to play the game
print("Directions: ")
print("Player 1 and Player 2 take turns removing squares")
print("A player may remove any number of squares but they must be from the same row")
print("A player must remove at least 1 square per turn")
print("The player who removes the last square wins")

# main function that alternates the game between player move and computer move until one wins
while len(game_board) > 1:
    getGameBoard()
    print("Your Move")  
    getPlayerMove()
    if getNumRows() == 1:
        print("Congratulations! You have won!")
        exit
    else: 
        print(game_board)
        getGameBoard()
        print("Computer Move")  
        getComputerMove()
        if getNumRows() == 1:
            print("Better luck next time!")
            exit





    