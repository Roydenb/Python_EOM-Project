import random

def get_user_input():
    user_input_list = []
    while len(user_input_list) < 6:
        user_input = int(input("Please enter a number: "))
        if user_input < 0 or user_input > 49:
            print('Please enter a number between 1 and 49')
            continue
        user_input_list.append(user_input)
    return user_input_list

user_input_list = get_user_input()

random_list = random.sample(range(1, 49), 6) # winning lotto numbers
print(random_list)
print(user_input_list)

def check_winning_count():
    count = 0
    for num in user_input_list:
        if num in random_list:
            count = count + 1
    return count

def check_winnings():
    count = check_winning_count()
    if count < 2:
        print("Sorry, try next time.")
    if count == 2:
        print("Well Done you win R20.00")

check_winnings()
