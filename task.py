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
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors: "))
li = [rock,paper,scissors]
ch = random.randint(0,2)
print("\n")
if choice == 0 and ch == 0 or choice == 1 and ch == 1 or choice == 2 and ch == 2:
    print("Your Choice: ")
    print(li[choice])
    print("Computer's Choice: ")
    print(li[ch])
    print("Draw!!!")
elif choice == 0 and ch ==1 or choice == 1 and ch == 2 :
    print("Your Choice: ")
    print(li[choice])
    print("Computer's Choice:")
    print(li[ch])
    print("You Lost!!!")
else:
    print("Your Choice: ")
    print(li[choice])
    print("Computer's Choice: ")
    print(li[ch])
    print("You Won!!!")
