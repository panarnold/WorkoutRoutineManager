#! python
# Steps TODO:
# 1. Create dictionaries of users. Program will collect data about them (weight, age, sex, lifting records etc.)
# 2. Quick survey to every user - times a week of training, weakspots, prorities muscles
# 3. Proposition of workout prints on a termianl (random?). If you accept it, just click yes.
# 4. Script will save it onto .xlsx file
# 5. Option for writing a .pdf file directly from .xlsx file
# 6. Script working on a website.

from os import mkdir
import json


users = {}
user_list = open('user_list.txt', 'a')


def check_if_exist(user_name):
    if user_name in user_list.readlines():
        print("Ooops, that user is already exist. One more time")
        main()


def loop_through_list():
    for user in user_list:
        print(user)

def create_new_user():
    user_name = input('Name of your client:\n')
    check_if_exist(user_name)
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
        "user age": user_age,
        "user sex": user_sex,
        "user total": total,
        "squat": user_squat,
        "bench": user_benchpress,
        "deadlift": user_deadlift
        }
    mkdir(f'{user_name.lower()}')

    with open(f'{user_name.lower()}/{user_name.lower()}_data.txt', 'a') as file:
        file.write(json.dumps(users[user_name]))


    
    

    

def create_training_for_user():
    pass

def main():
    print('Hello there.\n\tType 1 to create new user\n' +
    '\n\tType 2 to choose from existing users')
    option = input()
    try:
        option = int(option)
    except:
        print('Please read carefully. One more time')
        main()

    if option == 1:
        create_new_user()
    elif option == 2:
        loop_through_list()
    else:
        print('Please read carefully. One more time')
        main()


main()



