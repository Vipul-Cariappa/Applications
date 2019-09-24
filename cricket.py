import random


def batting_ps(target):
   bat = 0
   ball = 1
   total = 0

   while True:
      if bat != ball and total < target:
         bat = int(input("\nEnter the number: "))
         ball = random.choice((1, 2, 3, 4, 5, 6))
         print(f"The bowler put {ball}!\n")
         total += bat
         print(f"Runs scored is {total}")
      else:
         break

   if bat == ball:
      print("You are out!! \n\t!!You lost the match!!")
   else:
      print("\n\t!!You won the Match!!")


def batting_cs(target):
   bat = 0
   ball = 1
   total = 0

   while True:
      if bat != ball and total < target:
         ball = int(input("\nEnter the number: "))
         bat = random.choice((1, 2, 3, 4, 5, 6))
         print(f"The batsman put {bat}!\n")
         total += bat
         print(f"Runs scored is {total}")
      else:
         break

   if bat == ball:
      print("\n\t!!You won the Match!!")
   else:
      print("You are out!! \n\t!!You lost the match!!")

   
def bowling_ps(target):
   bat = 0
   ball = 1
   total = 0

   while True:
      if bat != ball and total < target:
         ball = int(input("\nEnter the number: "))
         bat = random.choice((1, 2, 3, 4, 5, 6))
         print(f"The batsman put {bat}!\n")
         total += bat
         print(f"Runs scored is {total}")
      else:
         break

   if bat == ball:
      print("\n\t!!You won the Match!!")
   else:
      print("You are out!! \n\t!!You lost the match!!")


def bowling_cs(target):
   bat = 0
   ball = 1
   total = 0

   while True:
      if bat != ball and total < target:
         bat = int(input("\nEnter the number: "))
         ball = random.choice((1, 2, 3, 4, 5, 6))
         print(f"The bowler put {ball}!\n")
         total += bat
         print(f"Runs scored is {total}")
      else:
         break

   if bat == ball:
      print("You are out!! \n\t!!You lost the match!!")
   else:
      print("\n\t!!You won the Match!!")


def batting_pf():
   bat = 0
   ball = 1
   total = 0

   while bat != ball:
      bat = int(input("\nEnter the number: "))
      ball = random.choice((1, 2, 3, 4, 5, 6))
      print(f"The bowler put {ball}!\n")
      total += bat
      print(f"Runs scored is {total}")

   print(f"You are out!! Target is {total}")
   print("You are bowling now!")
   bowling_ps(total)


def batting_cf():
   bat = 0
   ball = 1
   total = 0

   while bat != ball:
      bat = random.choice((1, 2, 3, 4, 5, 6))
      ball = int(input("\nEnter the number: "))
      print(f"The batsman put {bat}!\n")
      total += bat
      print(f"Runs scored is {total}")

   print(f"Computer is out!! Target is {total}")
   print("You are batting now!")
   bowling_cs(total)


def bowling_pf():
   bat = 0
   ball = 1
   total = 0

   while bat != ball:
      ball = int(input("\nEnter the number: "))
      bat = random.choice((1, 2, 3, 4, 5, 6))
      print(f"The batsman put {bat}!\n")
      total += bat
      print(f"Runs scored is {total}")

   print(f"Computer is out!! Target is {total}")
   print("You are batting now!")
   batting_ps(total)


def bowling_cf():
   bat = 0
   ball = 1
   total = 0

   while bat != ball:
      ball = random.choice((1, 2, 3, 4, 5, 6))
      bat = int(input("\nEnter the number: "))
      print(f"The bowler put {ball}!\n")
      total += bat
      print(f"Runs scored is {total}")

   print(f"You are out!! Target is {total}")
   print("You are bowling now!")
   batting_cs(total)


# Toss
toss = random.choice(("Heads", "Tales"))

while True:
   #try:
      wish = input("Heads(h) or Tales(t): ")

      if wish.lower() == "h" and toss == "Heads":
         print("It is heads you won the toss!!")
         choice = input("Batting(a) or Bowling(b): ")

         if choice.lower() == "a":
            batting_pf()
            break
         elif choice.lower() == "b":
            bowling_pf()
            break
         else:
            print("\n!!!You enter something wrong!!!\n")
         

      elif wish.lower() == "t" and toss == "Tales":
         print("It is tales you won the toss!!")
         choice = input("Batting(a) or Bowling(b): ")
         
         if choice.lower() == "a":
            batting_pf()
            break
         elif choice.lower() == "b":
            bowling_pf()
            break
         else:
            print("\n!!!You enter something wrong!!!\n")

      else:
         choice = random.choice(("bat", "ball"))
         print(f"You lost the toss, computer will {choice} first.")
         
         if choice.lower() == "bat":
            batting_cf()
            break
         else:
            bowling_cf()
            break   
   #except:
      print("\n!!!You enter something wrong!!!\n")
   