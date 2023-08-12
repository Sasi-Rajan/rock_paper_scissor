import random
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input=int(input("Enter 'o' for rock '1' for paper and '2' for scissor "))
comp_rand=random.randint(0,2)
if user_input == 0 and comp_rand == 2:
    print(f"You choose {rock}\n---------------\nComputer choose{scissor}")
    print("You won")
elif user_input == 0 and comp_rand == 1:
    print(f"You choose {rock}\n---------------\nComputer choose{paper}")
    print("You lost")
elif user_input == 0 and comp_rand == 0:
    print(f"You choose {rock}\n---------------\nComputer choose{rock}")
    print("Match draw")
elif user_input == 1 and comp_rand == 0:
    print(f"You choose {paper}\n---------------\nComputer choose{rock}")
    print("You won")
elif user_input == 1 and comp_rand == 1:
    print(f"You choose {paper}\n---------------\nComputer choose{paper}")
    print("Match draw")
elif user_input == 1  and comp_rand == 2:
    print(f"You choose {paper}\n---------------\nComputer choose{scissor}")
    print("You lost")
elif user_input == 2 and comp_rand == 0:
    print(f"You choose {scissor}\n---------------\nComputer choose{rock}")
    print("You lost")
elif user_input == 2 and comp_rand == 1:
    print(f"You choose {scissor}\n---------------\nComputer choose{paper}")
    print("You won")
else:
    print(f"You choose {scissor}\n---------------\nComputer choose{scissor}")
    print("Match draw")