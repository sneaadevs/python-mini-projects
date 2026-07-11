rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choice=input("What do you choose?Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
if player_choice=="0":
    print(rock)
elif player_choice=="1":
    print(paper)
elif player_choice=="2":
    print(scissors)
else:
    print("Invalid input")
import random
symbols = [rock, paper, scissors]
computer_choice=random.randint(0,2)
print("Computer chose:")
print(symbols[computer_choice])
if player_choice==str(computer_choice):
    print("It's a draw")
elif (player_choice=="0" and computer_choice==2) or (player_choice=="1" and computer_choice==0) or (player_choice=="2" and computer_choice==1):
    print("You win")
else:
    print("You lose")
