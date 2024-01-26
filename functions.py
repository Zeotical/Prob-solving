import random, os

#Functions I didn't have to make more of?

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def current_user(user):
    if user: return"x"
    else: return "o"

def quit(user_input):
 if user_input == "q":
     print("Thanks for playing!")
     return True
 else: return False

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True 

def add_to_board(coords,board,active_user):
    row = coords[0]
    col= coords[1]
    board[row][col]= active_user

def istaken(coords,board):
 row = coords[0]
 col = coords[1]
 if board[row][col]!= "-":
    print("This position is already taken.")
    return True
 else: return False 

def check_input(user_input,gridsize):
     #chech if it's a number
     if not isnum(user_input): return False
     user_input = int(user_input)
     #check if it's 1-9
     if gridsize=="1":
      if not bounds(user_input,gridsize):return False
      else:return True
     elif gridsize=="2":
      if not bounds(user_input,gridsize): return False
      else:return True
     elif gridsize=="3":
      if not bounds(user_input,gridsize):return False
      else:return True


def bounds (user_input,gridsize):
    if gridsize=="1": 
      if user_input>9 or user_input <1:
         print("This number is out of bounds")
         return False
      else: return True
    elif gridsize=="2":
      if user_input<1 or user_input>16:
         print("This number is out of bounds")
         return False
      else: return True
    elif gridsize=="3":
      if user_input<1 or user_input>25:
          print("This number is out of bounds.")
          return False
      else: return True

def computer(gridsize):
   if gridsize== "small":
      user_input= random.randint(1,9)
      return user_input
   elif gridsize== "medium":
      user_input= random.randint(1,16)
      return user_input
   elif gridsize=="big":
      user_input= random.randint(1,25)
      return user_input


def startagain(user_input,gridsize):
   if user_input=="s" and gridsize=="small":
     os.system("cls")
     print("New start")
   elif user_input=="s" and gridsize=="medium":
     os.system("cls")
     print("New start")
   elif user_input=="s" and gridsize=="big":
     os.system("cls")
     print("New start")
#Functions I had to make multiple different versions of

def coordinates(user_input):
     row = int(user_input/3)
     col= user_input
     if col>2: col= int(col%3)
     return (row,col)    

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                   complete_row = False
                   break
        if complete_row: return True
    return False

def check_col(user,board):
    for col in range(3):
        complete_col= True
        for row in range(3):
            if board[row][col] != user:
                complete_col= False
                break
        if complete_col: return True
    return False     

def check_diag(user, board):
    #top left to bottom right
    if board[0][0]== user and board[1][1]==user and board [2][2]==user: return True
    elif board[0][2]== user and board[1][1] ==user and board [2][0]==user: return True
    else: return False

def iswin(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True  
    if check_diag(user,board): return True 

def coordinates4(user_input):
    row= int(user_input/4)
    col= user_input
    if col>3 : col= int(col%4)
    return (row,col)


def iswin4(user,board4):
 if check_row4(user,board4): return True
 if check_col4(user,board4): return True
 if check_diag4(user,board4):return True

def check_row4(user,board4):
   for row in board4:
      complete_row = True
      for slot in row:
         if slot!= user:
            complete_row= False
            break
      if complete_row : return True  
   return False   
   
def check_col4(user,board4):
   for col in range(4):
      complete_col = True
      for row in range(4):
         if board4[row][col] != user:
            complete_col= False
            break
      if complete_col: return True
   return False     

def check_diag4(user,board4):
   if board4[0][0] == user and board4[1][1]== user and\
      board4[2][2]== user and board4[3][3]== user:
      return True
   elif board4[0][3] == user and board4[1][2]== user and\
        board4[2][1]== user and board4[3][0]==user:
      return True
   else: return False   

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