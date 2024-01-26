
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

import os, functions  as fun

choice= input("Do you want to play against another player or the computer? ").lower()

if choice=="computer":
   username1 = input("Player 1 Enter your username:" )
   print ("Hello "+username1)
elif choice=="player":
   username1 = input("Player 1 Enter your username:" )
   print ("Hello "+username1)
   username2 = input("Player 2 Enter your username:" )
   print ("Hello "+username2)

board= [
    ["-", "-","-"],
    ["-", "-","-"],
    ["-", "-","-"]
]


<<<<<<< HEAD
user_input="a"
=======
user_input="#"
choice= input("Do you want to play against another player or the computer? ").lower()
>>>>>>> 5699296d20516be070d8bd2a62d75dcb702e55b7
gridsize=input("Enter a gridsize from small,medium and big: ").lower()

user= True # when true it refers to x, otherwise o


turns= 0
while True :
    if user_input=="s":
        turns=0
        board= [         #added board since it used to take the previous games' input
    ["-", "-","-"],
    ["-", "-","-"],
    ["-", "-","-"]]
        fun.startagain(user_input,gridsize)
    if choice=="computer" and user== False:
      user_input= str(fun.computer(gridsize))
      print(f"The computer enters: {user_input}")
    else:
      fun.print_board(board)
      user_input=input("Please enter a position 1 through 9 or press \"q\" to quit: ") 
    if fun.quit(user_input): break
    if not fun.check_input(user_input,gridsize):
        print("Please try again.")
        continue
    user_input= int(user_input) - 1
    active_user = fun.current_user(user)
    coords = fun.coordinates(user_input)
    if fun.istaken(coords, board):
        print("Please try again.")
        continue
    fun.add_to_board(coords,board,active_user)
    if fun.iswin(active_user,board):
        print()
        fun.print_board(board)
        print()
        print(f"{active_user.upper()} won!")
        user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
    if fun.quit(user_input): break
    turns +=1
    if turns==9 :
        print()
        fun.print_board(board)
        print()
        print("It's a draw!")
        user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
    if fun.quit(user_input): break
    user = not user

"""
Basmala 1231102801 code

#4*4 board
#win function
#draw function
#user input and toggle b/w users
#check if space is already taken
#check if user enters smth else make them go again

"""
board4= [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]
]

turns=0
while turns<16:
    active_user= fun.current_user(user)
    if user_input=="s":
        turns=0
        board4= [
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"],
    ["-","-","-","-"]]
        fun.startagain(user_input,gridsize)
    if choice=="computer" and user== False:
      user_input= str(fun.computer(gridsize))
      print(f"The computer enters: {user_input}")
    else:
      fun.print_board(board4)
      user_input=input("Please enter a position 1 through 16 or press \"q\" to quit: ") 
    if fun.quit(user_input): break
    if not fun.check_input(user_input,gridsize):
      print("Please try again.")
      continue
    user_input= int(user_input)-1
    coords= fun.coordinates4(user_input)
    if fun.istaken(coords,board4): 
        print("Please try again.")
        continue
    fun.add_to_board(coords,board4,active_user)
    if fun.iswin4(active_user,board4):
       print()
       fun.print_board(board4)
       print()
       print(f"{active_user} won!")
       user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
    if fun.quit(user_input): break 
    turns+=1
    if turns==16:
     print()
     fun.print_board(board4)
     print()
     print("It's a draw!")
     user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
    if fun.quit(user_input): break 
    user=not user
    
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
while turns<25:
   active_user= fun.current_user(user) 
   if user_input=="s":
        turns=0
        board5=[             #added board since it used to take the previous games' input
   ["-","-","-","-","-"], 
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"] ]         
        fun.startagain(user_input,gridsize)
   if choice=="computer" and user== False:
      user_input= str(fun.computer(gridsize))
      print(f"The computer enters: {user_input}")
   else:
      user_input=input("Please enter a position 1 through 9 or press \"q\" to quit: ")   
   if fun.startagain(user_input):continue
   if fun.quit(user_input): break
   if not fun.check_input(user_input,gridsize):
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