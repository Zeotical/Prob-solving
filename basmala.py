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

import functions  as fun

# board= [
#     ["-", "-","-"],
#     ["-", "-","-"],
#     ["-", "-","-"]
# ]

import  os

x= input("Do you want to play against another player or the computer? ").lower()
gridsize=input("Enter a gridsize from small,medium and big: ").lower()

user= True # when true it refers to x, otherwise o

def startagain(user_input):
   if user_input=="s":
    os.system('cls') #tried using clear but apparantly windows only supports this? absoulte loss.
    return True
   else: return False  

# turns= 0
# while turns<9 :
#     active_user = current_user(user)
#     fun.print_board(board)
      # if x=="computer" and user== False:
      # user_input= str(fun.computer(gridsize))
      # print(f"The computer enters: {user_input}")
      # else:
      # user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ") 
#     if fun.quit(user_input): break
   #  if not fun.check_input(user_input):
   #      print("Please try again.")
   #      continue
#     user_input= int(user_input) - 1
#     coords = fun.coordinates(user_input)
#     if fun.istaken(coords, board):
#         print("Please try again.")
#         continue
#     fun.add_to_board(coords,board,active_user)
#     if fun.iswin(active_user,board):
#         print()
#         fun.print_board(board)
#         print()
#         print(f"{active_user.upper()} won!")
#         break
#     turns +=1
#     if turns==9 :
#         print()
#         fun.print_board(board)
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

# turns=0
# while turns<16:
#     active_user= current_user(user)
# #     fun.print_board(board4)
#       if x=="computer" and user== False:
#       user_input= str(fun.computer(gridsize))
#       print(f"The computer enters: {user_input}")
#       else:
#       user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ") 
#     if fun.quit(user_input): break
#     if not fun.check_input4(user_input):
#         print("Please try again.")
#         continue
#     user_input= int(user_input)-1
#     coords= fun.coordinates4(user_input)
#     if fun.istaken(coords,board4): 
#         print("Please try again.")
#         continue
#     fun.add_to_board(coords,board4,active_user)
#     if fun.iswin4(active_user,board4):
#        print()
#        fun.print_board(board4)
#        print()
#        print(f"{active_user} won!")
#        break
#     turns+=1
#     if turns==16:
#      print()
#      fun.print_board(board4)
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

turns=0
user_input="a"
while turns<25:
      
   if user_input !="s":
    fun.print_board(board5) 
   elif user_input=="s":
      os.system("cls")
      print("New start")
      board5=[
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"] ]
      fun.print_board(board5)

   active_user= fun.current_user(user)
   if x=="computer" and user== False:
      user_input= str(fun.computer(gridsize))
      print(f"The computer enters: {user_input}")
   else:
      user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ").lower()   
   if startagain(user_input):continue
   if fun.quit(user_input): break
   if not fun.check_input5(user_input):
      print("Please try again.")
      continue
   user_input= int(user_input)-1
   coords= fun.coordinates5(user_input)
   if fun.istaken(coords,board5):
      print("Please try again.")
      continue
   fun.add_to_board(coords,board5,active_user)
   if fun.iswin5(active_user,board5):
      print()
      fun.print_board(board5)
      print()
      print(f"{active_user} won!")
      break
   turns+=1
   if turns==25:
      print()
      fun.print_board(board5)
      print()
      print("It's a draw!")
      break
   user = not user