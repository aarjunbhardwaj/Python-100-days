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
choice =(input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors\n 0,1,2:"))  
computer_choice = random.randint(0,2)

if not choice.isdigit():
    print("you entered invalid value, Try again and Choose a number between (0-2)")
else:
    choice = int(choice)
    if choice > 2:
        print("you entered invalid number,try again and choose between (0-2)")
    elif choice == 0 or choice == 1 or choice == 2:
        if choice == 0:
            print(f"you choose : Rock {rock}")
        elif choice == 1:
            print(f"you choose : Paper {paper}")
        elif choice == 2:
            print(f"you choose : scissors {scissors}") 

        if computer_choice == 0:
            print(f"The computer Choose: Rock {rock}") 
            if choice == 2:
                print(f"you lose! Rock wins against scissors.")
            elif choice == 0:
                print(f"it's a draw")
            else:
                print("You win")
              
        elif computer_choice == 1:
            print(f"you choose : paper {paper}")
            if choice == 0:
                print("you lose paper wins against rock")
            elif choice == 0:
                print("it's a draw")
            else:
                print("you win")
            
        elif computer_choice == 2:
            print(f"you choose : scissors {scissors}") 
            if choice == 1:
                print("you lose,scissors wins against paper")
            elif choice == 2:
                print("It's a draw !")
            else:
                print("you win")        

                  
