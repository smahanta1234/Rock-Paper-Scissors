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

selection=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
comp_selection=random.randint(0,2)

if(selection==0):
    print("Your Choice: Rock")
    print(rock)
elif(selection==1):
    print("Your Choice: Paper")
    print(paper)
else:
    print("Your Choice: Scissors")
    print(scissors)

print("Computer choice:\n")

if(comp_selection==0):
    print(rock)
elif(comp_selection==1):
    print(paper)
else:
    print(scissors)

if (comp_selection==selection):
    print("You Draw!")
elif (selection==0 and comp_selection==1):
    print("You lose!")
elif (selection==1 and comp_selection==2):
    print("You Lose!")
elif (selection==2 and comp_selection==0):
    print("You Lose!")
else:
    print("You win!")