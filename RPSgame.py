import random
intro = "||ROCK PAPER SCISSOR GAME (MULTIPLAYER)||"
rules = '''Enter 'r' for ROCK, 'p' for PAPER and 'S1' for SCISSOR'''
menu = '''
1. Single Player
2. Two Player
3. Exit
'''
rpc = ['R', 'P', 'S']
chp = ['1', 'y', 'Y', 'yes', 'Yes', 'YES']

print(intro)

print(rules)


while(True):
   mode = int(input(menu))
   if mode==3:
      exit(0)
   user = input("Player 1: ")
   if user.upper() not in rpc :
      print("Invalid input. Try again.")
      continue
   else:
      user=user.upper()
   if mode==1:
      pc = random.choice(rpc)
      print("Computer :", pc)
   if mode == 2:
      pc = input("Player 2: ")
      if pc.upper() not in rpc:
         print("Invalid input. Try Again.")
         continue
      else:
         pc = pc.upper()
   if(mode==3):
      exit(0)
   if(user == pc):
      print("Draw")
   elif user=='R':
      if pc=='S':
         print("You won.")
      elif pc=='P':
         print("You lost.")
   elif user=='P':
      if pc=='S':
         print("You lost.")
      elif pc=='R':
         print("You won.")
   elif user=='S':
      if pc=='R':
         print("You lost.")
      elif pc=='P':
         print("You won.")
