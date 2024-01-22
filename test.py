
import random 
gridsize= input()
def computer(gridsize):
   if gridsize== "small":
      user_input= random.randint(1,9)
      return user_input
   elif gridsize== "medium":
      user_input= random.randint(1,16)
      return user_input
   elif gridsize=="big":
     print( random.randint(1,25))
    
a=(computer(gridsize))
