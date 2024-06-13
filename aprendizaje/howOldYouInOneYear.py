# This script interacts with the user by asking for their name and age, 
#then responds with a greeting and a comment about their age next year.

# Print a prompt asking for the user's name
print('What is your name?')

# Read the user's input (their name) and store it in the variable 'myName'
myName = input()

# Print a greeting message that includes the user's name
print('Hi ' + myName)

# Print a prompt asking for the user's age
print('How old are you?')

# Read the user's input (their age) and store it in the variable 'age'
age = input()

# Calculate the user's age next year by converting the age to an integer, adding 1, 
#and converting it back to a string
# Print a message that comments on the user's age next year
print('Wow, you will be ' + str(int(age) + 1) + ' in one year!')
