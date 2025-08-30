Here's the code with descriptive comments:

```python
# Import the random module to generate a random number for the coin toss
import random

# Initialize a variable to store the user's guess
guess = ''

# Continue to ask the user for input until they enter either 'heads' or 'tails'
while guess not in ('heads', 'tails'):
    # Prompt the user to guess the coin toss
    print('Guess the coin toss! Enter heads or tails:')
    # Get the user's input
    guess = input()

# Generate a random number to simulate the coin toss (0 is tails, 1 is heads)
toss = random.randint(0, 1)

# Check if the user's guess matches the result of the coin toss
if toss == guess:
    # If the user guessed correctly, print a success message
    print('You got it!')
else:
    # If the user guessed incorrectly, print a failure message and ask for another guess
    print('Nope! Guess again!')
    # Get the user's next guess
    guess = input()
    # Check if the user's second guess matches the result of the coin toss
    if toss == guess:
        # If the user guessed correctly the second time, print a success message
        print('You got it!')
    else:
        # If the user still guessed incorrectly, print a humorous failure message
        print('Nope. You are really bad at this game.')
```