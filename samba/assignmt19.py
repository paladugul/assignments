#! user/dell/python

#19. Play a number guessing game (User enters a guess, you print YES or Higher or Lower)

import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
for i in range(5):
      if guess < n:
            print "guess is low"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
      elif guess > n:
            print "guess is high"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
      else:
            print "you guessed it!"
            break
else:
      print "Sorry! Better luck next time"


output:

Enter an integer from 1 to 99: 5
guess is low
Enter an integer from 1 to 99: 20
guess is low
Enter an integer from 1 to 99: 52
guess is high
Enter an integer from 1 to 99: 99
guess is high
Enter an integer from 1 to 99: 100
guess is high
Enter an integer from 1 to 99: 152
Sorry! Better luck next time
