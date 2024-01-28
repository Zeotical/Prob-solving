# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL11-09
# Year: 2023/24 Trimester 1
# Names: Basmala Mohammed Ali Elimam | Nur Dina Ainulhayat Binti Mohd Affandy | Nurul Haifa Aliah Binti Mohd Yazid
# IDs: 1231102801 | 1231102033 | 1231102000
# Emails: 1231102801@student.mmu.edu.my | 1231102033@student.mmu.edu.my | 1231102000@student.mmu.edu.my
# Phones: +601167770850 | 010-362-9106 | 012-721-1586
# *********************************************************

#NOTE code which doesn't have a hastag with a member's name is from the tutorial or was alternated 
#based on the tutorial



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

import time, functions  as fun

board= [
    ["-", "-","-"],
    ["-", "-","-"],
    ["-", "-","-"]
]


user_input="#"
score1=0
score2=0

choice= input("Do you want to play against another player or the computer? ").lower() #Basmala


if choice=="computer":
   username1 = input("Player 1 Enter your username:" )
   print ("Hello "+username1)
   username2="computer"	
elif choice=="player":
   username1 = input("Player 1 Enter your username:" )
   print ("Hello "+username1)
   username2 = input("Player 2 Enter your username:" )
   print ("Hello "+username2)

while True:
    print("Choose a grid size!")
    print("1. small (3x3)")
    print("2. medium (4x4)")
    print("3. big (5x5)")
    gridsize = input("Enter your choice (1, 2, or 3): ")
    if gridsize in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3")





user= True # when true it refers to x, otherwise o 

board= [         
      ["-", "-","-"],
      ["-", "-","-"],
      ["-", "-","-"]]
turns= 0
if gridsize=="1":
    starttime=time.time()
    while True:
        starttime=time.time()
        if user_input=="s":
             turns=0
             starttime=time.time()
             fun.startagain(user_input,gridsize)
             choice= input("Do you want to play against another player or the computer? ").lower()
             gridsize="1"
             if choice=="computer":
                username1 = input("Player 1 Enter your username:" )
                print ("Hello "+username1)
                username2="computer" 
             elif choice=="player":
                username1 = input("Player 1 Enter your username:" )
                print ("Hello "+username1)
                username2 = input("Player 2 Enter your username:" )
                print ("Hello "+username2)
             board= [         #added board since it used to take the previous games' input
        ["-", "-","-"],
        ["-", "-","-"],
        ["-", "-","-"]]
        fun.print_board(board)    
        if choice=="computer" and user== False:
            user_input= str(fun.computer(gridsize))
            print(f"The computer enters: {user_input}")
        else:
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
        if user and fun.iswin(active_user,board):
           print()
           fun.print_board(board)
           print()
           user=username1 
           elapsed_time = time.time() - starttime
           if elapsed_time <= 30:
            print(f"{username1} won!")
            score1+=150
            print(f"Your score is {score1}")
            fun.scoresleaderboard(score1,score2)
           elif elapsed_time>30:
            print("Sadly, you played over the time limit :(")
            fun.scoresleaderboard(score1,score2)   
           user=True
           user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
           if fun.quit(user_input): break
        elif user==False and fun.iswin(active_user,board):
          print()
          fun.print_board(board)
          print()
          user=username2
          elapsed_time = time.time() - starttime
          if elapsed_time <= 30:
            print(f"{username2} won!")
            score2+=150
            print(f"Your score is {score2}")
            fun.scoresleaderboard(score1,score2,username1,username2)
          elif elapsed_time>30:
            print("Sadly, you played over the time limit :(")
            fun.scoresleaderboard(score1,score2,username1,username2)
          user=False
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
if gridsize=="2":
    starttime=time.time()
    while True:
        if user_input=="s":
             turns=0
             starttime=time.time()
             fun.startagain(user_input,gridsize)
             choice= input("Do you want to play against another player or the computer? ").lower()
             gridsize="2"
             if choice=="computer":
                username1 = input("Player 1 Enter your username:" )
                print ("Hello "+username1)
                username2="computer" 
             elif choice=="player":
                username1 = input("Player 1 Enter your username:" )
                print ("Hello "+username1)
                username2 = input("Player 2 Enter your username:" )
                print ("Hello "+username2)
             board4= [         #added board since it used to take the previous games' input
        ["-","-","-","-"],
        ["-","-","-","-"],
        ["-","-","-","-"],
        ["-","-","-","-"]]
        fun.print_board(board4)         
        if choice=="computer" and user== False:
            user_input= str(fun.computer(gridsize))
            print(f"The computer enters: {user_input}")
        else:
            user_input=input("Please enter a position 1 through 16 or press \"q\" to quit: ") 
        if fun.quit(user_input): break
        if not fun.check_input(user_input,gridsize):
            print("Please try again.")
            continue
        user_input= int(user_input) - 1
        active_user= fun.current_user(user)
        coords = fun.coordinates4(user_input)
        if fun.istaken(coords, board4):
            print("Please try again.")
            continue
        fun.add_to_board(coords,board4,active_user)
        if user and fun.iswin4(active_user,board4):
           print()
           fun.print_board(board4)
           print()
           user=username1 
           elapsed_time = time.time() - starttime
           if elapsed_time <= 60:
            score1+=150
            print(f"Your score is {score1}")
            fun.scoresleaderboard(score1,score2,username1,username2)
            print(f"{username1} won!")
           elif elapsed_time>60:
            print("Sadly, you played over the time limit :(")
            fun.scoresleaderboard(score1,score2,username1,username2)
           user=True 
           user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
           if fun.quit(user_input): break
        elif user==False and fun.iswin4(active_user,board4):
          print()
          fun.print_board(board4)
          print()
          user=username2
          elapsed_time= time.time() - starttime
          if elapsed_time <= 60:
             score2+=150
             print(f"Your score is {score2}")
             fun.scoresleaderboard(score1,score2)
             print(f"{username2} won!")
          elif elapsed_time>60:
           print("Sadly, you played over the time limit :(")
           fun.scoresleaderboard(score1,score2)
          user=False 
          user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
          if fun.quit(user_input): break
        turns +=1
        if turns==16 :
            print()
            fun.print_board(board4)
            print()
            print("It's a draw!")
            user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
            if fun.quit(user_input): break
        user = not user
    
board5=[
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"],
   ["-","-","-","-","-"]
]

if gridsize=="3":
    starttime=time.time()
    while True:
      if user_input=="s":
           turns=0
           starttime=time.time()
           fun.startagain(user_input,gridsize)
           choice= input("Do you want to play against another player or the computer? ").lower()
           gridsize="3"
           if choice=="computer":
              username1 = input("Player 1 Enter your username:" )
              print ("Hello "+username1)
              username2="computer"
           elif choice=="player":
              username1 = input("Player 1 Enter your username:" )
              print ("Hello "+username1)
              username2 = input("Player 2 Enter your username:" )
              print ("Hello "+username2)

           board5=[            
              ["-","-","-","-","-"], 
              ["-","-","-","-","-"],
              ["-","-","-","-","-"],
              ["-","-","-","-","-"],
              ["-","-","-","-","-"] ]   
      fun.print_board(board5)
      if choice=="computer" and user== False:
           user_input= str(fun.computer(gridsize))
           print(f"The computer enters: {user_input}")
      else:
          user_input=input("Please enter a position 1 through 9 or press \"q\" to quit: ").lower()  
      if fun.quit(user_input): break
      if not fun.check_input(user_input,gridsize):
          print("Please try again.")
          continue
      user_input= int(user_input)-1
      active_user = fun.current_user(user)
      coords= fun.coordinates5(user_input)
      if fun.istaken(coords,board5):
          print("Please try again.")
          continue
      fun.add_to_board(coords,board5,active_user)
      if user and fun.iswin5(active_user,board5): 
         print()
         fun.print_board(board5)
         print()
         user=username1 
         elapsed_time = time.time() - starttime
         if elapsed_time <= 90:
            score1+=150
            print(f"Your score is {score1}")
            fun.scoresleaderboard(score1,score2,username1,username2)
            print(f"{username1} won!")
         elif elapsed_time>90:
            print("Sadly, you played over the time limit :(")
            fun.scoresleaderboard(score1,score2,username1,username2) 
         user_input=input("To play again enter \"s\", to quit enter \"q\": ").lower() 
         if fun.quit(user_input): break
      elif user==False and fun.iswin5(active_user,board5):
        print()
        fun.print_board(board5)
        print()
        user=username2
        elapsed_time = time.time() - starttime
        if elapsed_time <= 90:
            score2+=150 #Basmala
            print(f"Your score is {score2}") #Basmala
            fun.scoresleaderboard(score1,score2) #Basmala
            print(f"{username2} won!")
        elif elapsed_time>90:
            print("Sadly, you played over the time limit :(")
            fun.scoresleaderboard(score1,score2) #Basmala
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
