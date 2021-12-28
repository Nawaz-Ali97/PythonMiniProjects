print("Welcome to my Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
correct=0
incorrect=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    correct+= 1
else:
    print("Incorrect")
    incorrect+= 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct')
    correct+= 1
else:
    print("Incorrect")
    incorrect+= 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct')
    correct+= 1
else:
    print("Incorrect")
    incorrect+= 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct')
    correct+= 1
else:
    print("Incorrect")
    incorrect+= 1

answer = input("Which popular company designed the first CPU? ")
if answer.lower() == "intel":
    print('Correct')
    correct+= 1
else:
    print("Incorrect")
    incorrect+= 1
print("You got " +str(correct)+ " questions correct and " +str(incorrect)+ " questions wrong.")
print("You got " +str((correct/5)*100)+ "%.")

