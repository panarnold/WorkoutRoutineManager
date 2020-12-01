#! python
# Steps TODO:
# 1. Create dictionaries of users. Program will collect data about them (weight, age, sex, lifting records etc.)
# 2. Quick survey to every user - times a week of training, weakspots, prorities muscles
# 3. Proposition of workout prints on a termianl (random?). If you accept it, just click yes.
# 4. Script will save it onto .xlsx file
# 5. Option for writing a .pdf file directly from .xlsx file
# 6. Script working on a website.

import os.path
import json
import random


users = {}
current_user = {}
user_list = open('user_list.txt', 'a+')


def load_user_from_dir(user_name):

    with open(f'{user_name}/{user_name}_data.json', 'r') as json_file:
        current_user = json.load(json_file)

        return current_user


    
    # current_user = json.load(f'{user_name}/{user_name}_data.json')


    # print(current_user)
    
    # if user_name in directories_list:
    #     users[user_name]



def check_if_exist(user_name, user_list):
    for user_names in user_list:
        if user_name in user_names:
            return True
    
    


def get_user_list():
    list = []
    with open('user_list.txt', 'r') as file:
        for user in file.read().splitlines():
            list.append(user)
    return list

def print_list(list):
    for user in list:
        print(user)

def create_new_user():
    user_name = input('Name of your client:\n').lower()
    list = get_user_list()
    if check_if_exist(user_name, list):
        print("Sorry, that user is already exist. Acual user list:")
        print_list(list)
        main()
        
    user_list.write(f'{user_name}\n')
    user_list.close()
    user_age = int(input('Age:\n'))
    user_sex = input('Sex: male/female? (type m/f):\n')

    while True:
        if user_sex == 'm' or user_sex == 'f':
            break
        user_sex = input('Ok, one more time: m/f?\n')

    user_benchpress = int(input('Benchpress record:\n'))
    user_squat = int(input('Squat record:\n'))
    user_deadlift = int(input('Deadlift record:\n'))

    total = user_benchpress + user_squat + user_deadlift

    users[user_name] = {
        "user_name": user_name, 
        "user_age": user_age,
        "user_sex": user_sex,
        "user_total": total,
        "squat": user_squat,
        "bench": user_benchpress,
        "deadlift": user_deadlift
        }
    
    
    if not os.path.exists(user_name):
        os.mkdir(user_name)

        with open(f'{user_name}/{user_name}_data.json', 'a') as file:
            file.write(json.dumps(users[user_name]))
    
    return users[user_name]

def choose_user(user_list):
    #TODO read from the files to find correct user 
    choice = input('Choose the user:\n')
    
    if choice in user_list:
        return users[choice]
    else:
        choose_user(user_list)
    
    

    

def create_training_for_user():
    pass

def main():
    option = try_if_option_is_int(input('Hello there.\n\tType 1 to create new user' +
    '\n\tType 2 to choose from existing users\n\tType 3 to exit the program:\n'))
    try_if_option_is_in_range(option, 1, 3)

    list = []
    if option == 1:
        current_user = create_new_user()
        user_menu()
        # print(current_user)
    elif option == 2:
        list = get_user_list()
        for user in list:
            print(user)
        current_user = load_user_from_dir(input('Choose the user:\n'))
        user_menu()
    elif option == 3:
        print("Thank's, cya.")
        exit(0)

def user_menu():
    option = try_if_option_is_int(input("\t1 - make a workout routine\n\t2 - back to main menu:\n"))

    try_if_option_is_in_range(option, 1, 2)

    if option == 1:
        workout_survey(current_user)
    elif option == 2:
        main()

def workout_survey(current_user):
    print("Let's start quick survey.")

    how_many_trainings = try_if_option_is_int(input("How many tranings per week? (3, 4, 5)?"))
    try_if_option_is_in_range(how_many_trainings, 3, 5)

    set_training_type = try_if_option_is_int(input("Set training type(1 - volume, 2 - intensity)"))
    try_if_option_is_in_range(set_training_type, 1, 2)

    set_priority = try_if_option_is_int(input("Set priority(1 - quads, 2 - chest, 3 - hamstrings)"))
    try_if_option_is_in_range(set_priority, 1, 3)

    generate_traning_day(how_many_trainings, set_training_type, set_priority)

def generate_traning_day(how_many_trainings, set_training_type, set_priority):
    pass








def try_if_option_is_int(option):
    if option.isalnum():
        return int(option)
    else:
        option = input("Option has to be an int, my man. One more time:\n")
        try_if_option_is_int(option)

def try_if_option_is_in_range(option, min_range, max_range):
    option = int(option)
    if option < min_range or option > max_range:
        option = input(f"Option has to be something between {min_range} and {max_range}")
        try_if_option_is_in_range(option, min_range, max_range)

        

main()
# load_user_from_dir('wojtek')
# try_if_option_is_int("4")



