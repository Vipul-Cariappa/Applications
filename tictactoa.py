glist = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]

class game:
   def __init__(self, q):
      self.q = q

   def board(self, glist):
      print("")
      print("")
      print("")
      print(f" {glist[0]} | {glist[1]} | {glist[2]} ")
      print(" ---------------- ")
      print(f" {glist[3]} | {glist[4]} | {glist[5]} ")
      print(" ---------------- ")
      print(f" {glist[6]} | {glist[7]} | {glist[8]} ")
      print("")
      print("")
      print("")


   def move(self, glist):
      self.board(glist)

      # Players move
      position = int(input(f"Enter the place number where you want to mark {self.q}: "))
      position -= 1

      ''' Check method to not rewrite a position '''
      while True:
         if glist[position] == "   ":
            glist[position] = self.q
            break
         else:
            print("\n!!!You cant rewrite a existing move!!!")
            position = int(input(f"Enter the place number where you want to mark {self.q}: "))
            position -= 1

      result = self.check_win(glist)
      return result



   def check_win(self, glist):
      
      # horizontal check
      if glist[0] == glist[1] == glist[2] == self.q:
         # row 1
         return (f"\n{self.q} wins the match")
      elif glist[3] == glist[4] == glist[5] == self.q:
         # row 2
         return (f"\n{self.q} wins the match")
      elif glist[6] == glist[7] == glist[8] == self.q:
         # row 3
         return (f"\n{self.q} wins the match")
      
      # vertical check
      elif glist[0] == glist[3] == glist[6] == self.q:
         # column 1
         return (f"\n{self.q} wins the match")
      elif glist[1] == glist[4] == glist[7] == self.q:
         # column 2
         return (f"\n{self.q} wins the match")
      elif glist[2] == glist[5] == glist[8] == self.q:
         # column 3
         return (f"\n{self.q} wins the match")

      # diagonl check
      elif glist[0] == glist[4] == glist[8] == self.q:
         return (f"\n{self.q} wins the match")
      elif glist[2] == glist[4] == glist[6] == self.q:
         return (f"\n{self.q} wins the match")

      # else statement
      else:
         return None        # change if wanted


player1 = game(" x ")
player2 = game(" o ")

game_return = None

while True:
   game_return = player1.move(glist)
   if game_return != None:
      print(game_return)
      break
   
   game_return = player2.move(glist)
   if game_return != None:
      print(game_return)
      break