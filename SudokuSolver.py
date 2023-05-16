
def findEmpty(board):
    #Find the first empty slot on the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
            
    return None


def checkPosition(board, value, position):
    #position holds (row, col)
    
    #Check Row
    for i in range(len(board[0])):
        if board[position[0]][i] == value and i != position[1]:
            return False
        
    #Check column
    for i in range(len(board)):
        if board[i][position[1]] == value and i != position[0]:
            return False
        
    #Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False
            
    return True


def solve(board):
    spot = findEmpty(board)

    if not spot:
        return True
    
    for i in range(1, 10):
        if checkPosition(board, i, spot):
            board[spot[0]][spot[1]] = i

            if solve(board):
                return True
            
            board[spot[0]][spot[1]] = 0
        
    return False


def printBoard(board):
    # print(" ")
    for i in range(len(board)):
        if i % 3 == 0:
            print("- - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    
    print("- - - - - - - - - - - \n")



# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# if solve(board):
#     printBoard(board)

# else:
#     print("No solution exists")