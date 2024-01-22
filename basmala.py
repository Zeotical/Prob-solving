 #tictactoe tutorial code

# """ #This is called a docstring.It is  used to document Python modules, classes, functions, and methods. 
#     #Enclosed in triple quotes, either single or double, and are placed immediately after the definition of the module, class, function, or method.
#     #can span multiple lines and be used to describe the purpose of the code, its inputs, outputs, and any relevant information
# tic tac toe board
# [
#     [-,-, -],
#     [-,-, -],
#     [-,-, -]
# ]

# user-input -> something 1-9
# if they enter anything else: tell them to go again
# check if the user_input is already taken
# add it to the board
# chech if usr won: checking rows, columns and diagonals
# toggle between users upon succesful moves
# """
# board= [
#     ["-", "-","-"],
#     ["-", "-","-"],
#     ["-", "-","-"]
# ]


import random

x= input("do you want to play against another player or the computer? ")
gridsize=input("enter gridsize from small medium big: ")

def computer(gridsize) -> int:
   if gridsize== "small":
      user_input= random.randint(1,9)
      return user_input
   elif gridsize== "medium":
      user_input= random.randint(1,16)
      return user_input
   elif gridsize=="big":
      user_input= random.randint(1,25)
      return user_input

user= True # when true it refers to x, otherwise o

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
 if user_input == "q":
     print("Thanks for playing!")
     return True
 else: return False
 
# def check_input(user_input):
#      #chech if it's a number
#      if not isnum(user_input): return False
#      user_input = int(user_input)
#      #check if it's 1-9
#      if not bounds(user_input):return False
#      return True
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True 

# def bounds (user_input):
#     if user_input>9 or user_input <1:
#         print("This number is out of bounds")
#         return False
#     else: return True

def istaken(coords,board):
 row = coords[0]
 col = coords[1]
 if board[row][col]!= "-":
    print("This position is already taken.")
    return True
 else: return False 
     
# def coordinates(user_input):
#      row = int(user_input/3)
#      col= user_input
#      if col>2: col= int(col%3)
#      return (row,col)    

def add_to_board(coords,board):
    row = coords[0]
    col= coords[1]
    board[row][col]= active_user

def current_user(user):
    if user: return"x"
    else: return "o"

# def iswin(user, board):
#     if check_row(user, board): return True
#     if check_col(user, board): return True  
#     if check_diag(user,board): return True 

# def check_row(user, board):
#     for row in board:
#         complete_row = True
#         for slot in row:
#             if slot != user:
#                    complete_row = False
#                    break
#         if complete_row: return True
#     return False

# def check_col(user,board):
#     for col in range(3):
#         complete_col= True
#         for row in range(3):
#             if board[row][col] != user:
#                 complete_col= False
#                 break
#         if complete_col: return True
#     return False     

# def check_diag(user, board):
#     #top left to bottom right
#     if board[0][0]== user and board[1][1]==user and board [2][2]==user: return True
#     elif board[0][2]== user and board[1][1] ==user and board [2][0]==user: return True
#     else: return False

# turns= 0
# while turns<9 :
#     active_user = current_user(user)
#     print_board(board)
#     user_input=input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
#     if quit(user_input): break
#     if not check_input(user_input):
#         print("Please try again.")
#         continue
#     user_input= int(user_input) - 1
#     coords = coordinates(user_input)
#     if istaken(coords, board):
#         print("Please try again.")
#         continue
#     add_to_board(coords,board)
#     if iswin(active_user,board):
#         print()
#         print_board(board)
#         print()
#         print(f"{active_user.upper()} won!")
#         break
#     turns +=1
#     if turns==9 :
#         print()
#         print_board(board)
#         print()
#         print("It's a draw!")
#     user = not user

"""
Basmala 1231102801 code

#4*4 board
#win function
#draw function
#user input and toggle b/w users
#check if space is already taken
#check if user enters smth else make them go again

"""
# board4= [
#     ["-","-","-","-"],
#     ["-","-","-","-"],
#     ["-","-","-","-"],
#     ["-","-","-","-"]
# ]

# def check_input4(user_input):
#     if not isnum(user_input): return False
#     user_input= int(user_input)
#     if not bounds4(user_input):return False
#     return True    
        
# def bounds4(user_input):
#     if user_input<1 or user_input>16:
#         print("This number is out of bounds")
#         return False
#     else: return True

# def coordinates4(user_input):
#     row= int(user_input/4)
#     col= user_input
#     if col>3 : col= int(col%4)
#     return (row,col)

# def check_row4(user,board4):
#    for row in board4:
#       complete_row = True
#       for slot in row:
#          if slot!= user:
#             complete_row= False
#             break
#       if complete_row : return True  
#    return False   
   
# def check_col4(user,board4):
#    for col in range(4):
#       complete_col = True
#       for row in range(4):
#          if board4[row][col] != user:
#             complete_col= False
#             break
#       if complete_col: return True
#    return False     

# def check_diag4(user,board4):
#    if board4[0][0] == user and board4[1][1]== user and\
#       board4[2][2]== user and board4[3][3]== user:
#       return True
#    elif board4[0][3] == user and board4[1][2]== user and\
#         board4[2][1]== user and board4[3][0]==user:
#       return True
#    else: return False

# def iswin4(user,board4):
#  if check_row4(user,board4): return True
#  if check_col4(user,board4): return True
#  if check_diag4(user,board4):return True
   
# turns=0
# while turns<16:
#     active_user= current_user(user)
#     print_board(board4)
#     user_input= input("Please enter a position 1 through 16 or enter \"q\" to quit: ")
#     if quit(user_input): break
#     if not check_input4(user_input):
#         print("Please try again.")
#         continue
#     user_input= int(user_input)-1
#     coords= coordinates4(user_input)
#     if istaken(coords,board4): 
#         print("Please try again.")
#         continue
#     add_to_board(coords,board4)
#     if iswin4(active_user,board4):
#        print()
#        print_board(board4)
#        print()
#        print(f"{active_user} won!")
#        break
#     turns+=1
#     if turns==16:
#      print()
#      print_board(board4)
#      print()
#      print("It's a draw!")
#      break
#     user=not user
    
"""
Basmala 1231102801 code

#5*5 board
#win function
#draw function
#user input and toggle b/w users
#check if space is already taken
#check if user enters smth else make them go again

"""   

board5=[
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"]
]

def  check_input5(user_input):
   if not isnum(user_input): return False
   user_input= int(user_input)
   if not bounds5(user_input): return False
   return True
            
def bounds5(user_input):
   if user_input<1 or user_input>25:
      print("This number is out of bounds.")
      return False
   else: return True

def coordinates5(user_input):
   row = int(user_input/5)
   col= int(user_input)
   if col>4: col= int(user_input%5)
   return (row,col)


def check_row5(user,board5):
   for row in board5:
      complete_row=True
      for slot in row:
         if slot!= user:
            complete_row= False
            break
      if complete_row: return True
   return False

def check_col5(user,board5):
   for col in range(5):
      complete_col= True
      for row in range(5):
         if board5[row][col] != user:
            complete_col= False
            break
      if complete_col: return True
   return False

def check_diag5(user,board5):
     if board5[0][0]== user and board5[1][1]== user\
     and board5[2][2]==user and board5[3][3]==user\
     and board5[4][4]==user: return True  
     elif board5[0][4]== user and board5[1][3]== user\
     and board5[2][2]==user and board5[3][1]==user\
     and board5[4][0]==user: return True            

def iswin5(user,board5):
   if check_row5(user,board5): return True
   if check_col5(user,board5): return True     
   if check_diag5(user,board5): return True
turns=0
while turns<25:
   print_board(board5)
   active_user= current_user(user)
   if x=="computer" and user== False:
      user_input= str(computer(gridsize))
      print(user_input)
   else:
      user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ") 
   if quit(user_input): break
   if not check_input5(user_input):
      print("Please try again.")
      continue
   user_input= int(user_input)-1
   coords= coordinates5(user_input)
   if istaken(coords,board5):
      print("Please try again.")
      continue
   add_to_board(coords,board5)
   if iswin5(active_user,board5):
      print()
      print_board(board5)
      print()
      print(f"{active_user} won!")
      break
   turns+=1
   if turns==25:
      print()
      print_board(board5)
      print()
      print("It's a draw!")
      break
   user = not user