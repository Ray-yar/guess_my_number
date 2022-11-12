import random

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Guess My Number is an interesting game to play.")
print("You just need to guess the number we assigned, any time that you fail then your number will be decreased.")
print("Your number will start from 20 and it will decrease if you answer wrong number")
print("")
print("Lets Start!!!")
print("")

user_input = 0;
rand_num = 0;

def get_user_answer():
    """
    In This Function we need to get data from user.
    """
    while True:
        user_value = input("Guess my number:\n")
        if validate_user_answer(user_value):
            print("Your data is valid")
            break

def validate_user_answer(value):
    try:
        int(value)
    
        if int(value) > 20:
            print(f"Ohh no, {value} is out of range! Please enter between 1 - 20\n")
            return False

        elif int(value) < 0:
            print(f"Sorry, {value} is an invalid number, please try again.\n")
            return False
    
    except:
        print("Sorry, you have entered an invalid amount!\n")
        return False

    return True

def generate_random_number():
    """
    Generate A random number between 1 - 20
    """
    rand_num = random.randint(1, 20)
    return rand_num

def main():
    rand_num = generate_random_number()
    get_user_answer()

main()