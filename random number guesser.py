import random
top_of_range =input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print('Please type a number larger than 0 next time!')
        quit()
        
else:
    print('Please type in a number next time!')
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses+=1
    user_input= input("Please guess a number: ")
    if user_input.isdigit():
        user_input= int(user_input)
    else:
        print('Please type a positive number next time! ')
        continue    
    
    if user_input == random_number:
        print("Congratulations, you got it right!")
        break
    
    elif user_input > random_number:
            print('Lower')
    else:
            print('Higher')
        
print("You got it in", guesses , "guesses.")