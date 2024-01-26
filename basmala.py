
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

# import functions  as fun

# board= [
#     ["-", "-","-"],
#     ["-", "-","-"],
#     ["-", "-","-"]
# ]

# import  os

# choice= input("Do you want to play against another player or the computer? ").lower()
# gridsize=input("Enter a gridsize from small,medium and big: ").lower()

# user= True # when true it refers to x, otherwise o


# turns= 0
# while turns<9 :
#    if user_input !="s":
#     fun.print_board(board) 
#    elif user_input=="s":
#     os.system("cls")
#     print("New start")
#     board5=[
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"] ]
#     fun.print_board(board)
#     active_user = fun.current_user(user)
#     fun.print_board(board)
#     if choice=="computer" and user== False:
#       user_input= str(fun.computer(gridsize))
#       print(f"The computer enters: {user_input}")
#     else:
#       user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ") 
#     if fun.startagain(user_input):continue
#     if fun.quit(user_input): break
#     if not fun.check_input(user_input):
#         print("Please try again.")
#         continue
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
#     if user_input !="s":
#      fun.print_board(board4) 
#     elif user_input=="s":
#       os.system("cls")
#       print("New start")
#       board5=[
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"] ]
#       fun.print_board(board4)
#     active_user= fun.current_user(user)
#     if choice=="computer" and user== False:
#       user_input= str(fun.computer(gridsize))
#       print(f"The computer enters: {user_input}")
#     else:
#       user_input=input("Please enter a position 1 through 25 or press \"q\" to quit: ") 
#     if fun.startagain(user_input):continue
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

# board5=[
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"]
# ]

# turns=0
# user_input="a"
# while turns<25:
#    if user_input !="s":
#     fun.print_board(board5) 
#    elif user_input=="s":
#       os.system("cls")
#       print("New start")
#       board5=[
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"],
#    ["-","-","-","-","-"] ]
#    fun.print_board(board5)
#    active_user= fun.current_user(user)
#    if choice=="computer" and user== False:
#       user_input= str(fun.computer(gridsize))
#       print(f"The computer enters: {user_input}")
#    if fun.startagain(user_input):continue
#    if fun.quit(user_input): break
#    if not fun.check_input5(user_input):
#       print("Please try again.")
#       continue
#    user_input= int(user_input)-1
#    coords= fun.coordinates5(user_input)
#    if fun.istaken(coords,board5):
#       print("Please try again.")
#       continue
#    fun.add_to_board(coords,board5,active_user)
#    if fun.iswin5(active_user,board5):
#       print()
#       fun.print_board(board5)
#       print()
#       print(f"{active_user} won!")
#       break
#    turns+=1
#    if turns==25:
#       print()
#       fun.print_board(board5)
#       print()
#       print("It's a draw!")
#       break
#    user = not user




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

#   choice= input("Do you want to play against another player or the computer? ").lower()
   #   gridsize=input("Enter a gridsize from small,medium and big: ").lower()
   #  if choice=="player":
   #    user_input=input("Please enter a position 1 through 9 or press \"q\" to quit: ") 
   #  elif choice!="computer" or choice!="player":
   #     print("This is an invalid input, please try again.")
   #     choice= input("Do you want to play against another player or the computer? ").lower() 
   #  elif choice=="computer" and user== False:
   #    user_input= str(fun.computer(gridsize))
   #    print(f"The computer enters: {user_input}")   
   #  elif gridsize!='small' or gridsize!="medium" or gridsize!="big":
   #     print("This is an invalid input, please try again.")
      #  gridsize=input("Enter a gridsize from small,medium and big: ").lower() 

  #  if user_input=="save":
   #    f=open("unsavedgame.txt","a")
   #    f.write(str(f"{board}\n"))
   #    f.close()
   #  if user_input=="continue":
   #    f=open("unsavedgame.txt","r") 
   #    open=f.read()
   #    f.close() 
   #    board= print(open)
   #    fun.print_board(board)
   #    continue   

import functions  as fun

board= [
    ["-", "-","-"],
    ["-", "-","-"],
    ["-", "-","-"]
]

import  os
score=0
def highscore(active_user):
   global score
   score+=150
   print(f"{active_user} your score is {score}")

again="a"
choice= input("Do you want to play against another player or the computer? ").lower()
gridsize=input("Enter a gridsize from small,medium and big: ").lower()

user= True # when true it refers to x, otherwise o

# def check_input(user_input):
#      #chech if it's a number
#      if not fun.isnum(user_input): return False
#      user_input = int(user_input)
#      #check if it's 1-9
#      if gridsize=="small":
#       if not fun.bounds(user_input):return False
#       return True
#      elif gridsize=="medium":
#         if not fun.bounds4(user_input): return False
#         return True
#      elif gridsize=="big":
#         if not fun.bounds4(user_input):return False
#         return True
turns= 0
user_input="#"

# *********************************************************
# Program: YOUR_FILENAME.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-09
# Year: 2023/24 Trimester 1
# Names: MEMBER_NAME_1 | MEMBER_NAME_2 | MEMBER_NAME_3
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3
# Phones: MEMBER_PHONE_1 | MEMBER_PHONE_2 | MEMBER_PHONE_3
# *********************************************************




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


user_input="#"
choice= input("Do you want to play against another player or the computer? ").lower()
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
      user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
   if fun.quit(user_input): break
   turns+=1
   if turns==25:
      print()
      fun.print_board(board5)
      print()
      print("It's a draw!")
      user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
   if fun.quit(user_input): break
   user = not user