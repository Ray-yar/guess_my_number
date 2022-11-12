import random

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("")
print("Welcome to (Guess My Number) gameplay. \nThis is an amazing game, you just need to guess the correct number we assigned, by answering incorrect number your score will be down.")
print("Your score will start from 20 and it will come down if your answer is wrong")
print("")
print("Good Luck!!!")
print("")

# Getting User Data
def get_user_answer():
    """
    In This Function we need to get data from user.
    """
    while True:
        user_value = input("Guess my number: ")
        if validate_user_answer(user_value):
            return user_value

# Validate User Data
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

# Generate Random Number
def generate_random_number():
    """
    Generate A random number between 1 - 20
    """
    rand_num = random.randint(1, 20)
    return rand_num

def check_game_result(rand_num, user_data):

    if int(user_data) > int(rand_num):
        print("Too large, Please try again.")
        print("")
        return 2
    elif int(user_data) < int(rand_num):
        print("Too small, Please try again.")
        print("")
        return 2
    elif int(user_data) == int(rand_num):
        print("Congratulations, You have successfully guessed the correct number!")
        return 1

# Run the Game
def main():
    score  = 20
    rand_num = generate_random_number()
    user_data = get_user_answer()
    while True:
        if check_game_result(rand_num,user_data) == 2:
            user_data = get_user_answer()
            score -= 1
            print("")
            print(f"Score: {score}")
        else:
            print("")
            print(f"Your Score is: {score}")
            break
main()