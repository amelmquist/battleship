import random


#Values to help you out
BOARD_SIZE_X = 8
BOARD_SIZE_Y = 8
previous_guesses = [] #formatted as (x,y,hit)


#CODE SNIPPETS THAT MAY BE HELPFUL
#"For loop"
for i in range(10):
    pass # to nothing


#"If statement"
x = 1
y = 1
if(x == 1 and y==2): #this says: "if x equals 1 and y equals 2, do the following..."
    pass #pass just says "we are not going to do anything here"

#"Print statement"
x = 10
print("This is a print statement. The value of X is:", x) #words go in quotes, variables go by themselves


#===============================================================================
# THE CODE TO PERFORM A SINGLE TURN GOES HERE. ASK IF YOU HAVE ANY QUESTIONS
#===============================================================================
def take_turn():
    # This would create a random guess
    x_guess = random_location()
    y_guess = random_location()

    #This checks if we have already guessed this locations before
    while(already_guessed(x_guess,y_guess)):
            x_guess = random_location()
            y_guess = random_location()

    # This is where we commit to a final decision for a guess location
    return (x_guess,y_guess)





#HELPER FUNCTION THAT CHECKS IF YOU HAVE ALREADY GUESSED SOMETING - YOU DO NOT HAVE TO USE THIS IF YOU DON"T WANT
def already_guessed(x,y):
    for guess in previous_guesses:
            if(guess[0] == x and guess[1] == y):
                return True
    return False

#HELPER FUNCTION TO MAKE A RANDOM SELECTION
def random_location():
    return random.randint(0,7)
