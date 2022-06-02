import random

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

#Write your code below this line 👇

choice = [rock, paper, scissors]

input_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
rand_num = random.randint(0,2)
computer_choice = rand_num

print(choice[input_choice])
print(choice[computer_choice])

if input_choice == 0:
    if computer_choice == 0:
        print("Draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")
elif input_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Draw")
    elif computer_choice == 2:
        print("You lose")
elif input_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    elif computer_choice == 2:
        print("Draw")
else:
    pass