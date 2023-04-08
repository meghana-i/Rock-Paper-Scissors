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
elements = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if your_choice >= 3 or your_choice < 0: 
  print("You typed an invalid number, you lose!") 
else: 
  print(elements[your_choice])
  
  computer_choice = random.randint(0,2)
  print(f"Computer chose:\n{elements[computer_choice]}")
  
  if computer_choice == 0 and your_choice == 1:
    print("You lose.")
  elif computer_choice == 2 and your_choice == 1:
    print("You lose.")
  elif computer_choice == 1 and your_choice == 0:
    print("You lose.")
  elif computer_choice == your_choice:
    print("It's a draw")
  else:
      print("You Win!")