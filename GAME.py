import random
import math

lower = int(input("Enter Lower bound:- "))  #input from user
 

upper = int(input("Enter Upper bound:- "))  #input from user
 

x = random.randint(lower, upper)    #random number generator from library random
print(x)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 

count = 0
 

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
 
    if x == guess:
        print("Congratulations you did it in ",count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
    
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
   
 