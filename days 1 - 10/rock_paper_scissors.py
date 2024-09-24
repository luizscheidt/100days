import random

rock= '''
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

options = [rock, paper, scissors]

player = int(input("Type 0 for rock, 1 for paper and 2 for scissors. Ready? Rock, paper, scissors, GO!"))
computer = random.randint(0,2)

print(f"Player:{options[player]}")
print(f"Computer{options[computer]}")

if player == computer:
    print("Draw!")
elif player == 0 and computer == 1:
    print("You lose!")
elif player == 0 and computer == 2:
    print("You win!")
elif player == 1 and computer == 0:
    print("You win!")
elif player == 1 and computer == 2:
    print("You lose!")
elif player == 2 and computer == 0:
    print("You lose!")
elif player == 2 and computer == 1:
    print("You win!")

