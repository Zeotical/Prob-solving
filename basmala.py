#tictactoe tutorial code

""" #This is called a docstring.It is  used to document Python modules, classes, functions, and methods. 
    #Enclosed in triple quotes, either single or double, and are placed immediately after the definition of the module, class, function, or method.
    #can span multiple lines and be used to describe the purpose of the code, its inputs, outputs, and any relevant information
tic tac toe board
[
    [-,-, -],
    [-,-, -],
    [-,-, -]
]

user-input -> something 1-9
if they enter anything else: tell them to go again
check if the user_input is already taken
add it to the board
chech if usr won: checking rows, columns and diagonals
toggle between users upon succesful moves
"""
board= [
    ["-", "-","-"],
    ["-", "-","-"],
    ["-", "-","-"]
]



def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
 if user_input == "q":
     print("Thanks for playing")
     return True
 else: return False
 
def check_input(user_input):
     #chech if it's a number
     if not isnum(user_input): return False
     user_input = int(user_input)
     #check if it's 1-9
     if not bounds(user_input):return False
     return True
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True 

def bounds (user_input):
    if user_input>9 or user_input <1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords,board):
 row = coords[0]
 col = coords[1]
 if board[row][col]!= "-":
    print("This position is already taken.")
    return True
 else: return False 
     
def coordinates(user_input):
     row = int(user_input/3)
     col= user_input
     if col>2: col= int(col%3)
     return (row,col)    

def add_to_board(coords,board):
    row = coords[0]
    col= coords[1]
    board[row][col]="x"

while True:
    print_board(board)
    user_input=input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again.")
        continue
    user_input= int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
    add_to_board(coords,board)
# input= input("enter: ")
# def ha(input):
#     if input=="yes":
#        return True
#     else: return False
# def ha2():
#     ha(input)
# if ha2():
#     print("hello")