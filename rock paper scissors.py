import random
user_wins=0
cpu_wins=0
draw=0
options = ["r", "p", "s"]
options[0]
while True:
        user_input = input("Rock/Paper/Scissors? (R/P/S) or Q to quit: ").lower()
        if user_input == "q":
            print("You won", user_wins, "times.")
            print("You drew", draw, "times.")
            print("Computer won", cpu_wins, "times.")
            print("Goodbye")   
            quit()
        if user_input not in options:
            print('Please type in something valid!')
            continue
        random_number= random.randint(0,2) 
        # rock paper scissors will be assigned to a number 
        #rock = 0 paper = 1 scissors =3
        computer_pick= options[random_number]
        print("Computer chose", computer_pick ,)
         
        if user_input == computer_pick:
            print("Draw!")
            draw+=1
            continue
        
        if user_input == "r" and computer_pick == "s":
            print("You won!")
            user_wins+=1
            continue
        
        elif user_input == "p" and computer_pick == "r":
            print("You won!")
            user_wins+=1
            continue
        elif user_input == "s" and computer_pick == "p":
            print("You won!")
            user_wins+=1
            continue
        else:
            print("You Lose!")
            cpu_wins+=1
        


               
        