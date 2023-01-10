import random
#import libraries

#change this to be whatever between number you desire
number = random.randint( 0, 10000)
#create your variables
tries = 0
found = False

while not found:
    guess = int(input("Guess: "))
    tries += 1
    if guess == number:
        found = True 
        print (f"You found the {number} after {tries} tries! Great Job")
    elif guess > number:
        print(f"The number you are looking for is less than {guess}! Sorry!")
    else:
        print (f"The number you are looking for is greater than {guess}! Sorry! ")
