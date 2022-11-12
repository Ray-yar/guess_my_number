# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Guess My Number is an interesting game to play.")
print("You just need to guess the number we assigned, any time that you fail then your number will be decreased.")
print("Your number will start from 20 and it will decrease if you answer wrong number")
print("")
print("Lets Start!!!")
print("")

def get_user_answer():
    """
        In This Function we need to get data from user.
    """
    user_value = input("Enter the correct number:\n")
    return user_value


get_user_answer()