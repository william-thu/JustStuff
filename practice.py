import random
choice_for_name = True
choice_for_repeat_name = True
choice_for_repeat_generate = True

names = []

user_choice_for_name = input("Give me a name to add into the list: ")
names.append(user_choice_for_name)

while choice_for_repeat_name == True:
    user_choice_for_repeat = input("Do you want to give me another name? (y/n): ")
    if user_choice_for_repeat == "y":
        user_choice_for_name = input("Give me another name: ")
        names.append(user_choice_for_name)
    elif user_choice_for_repeat == "n":
        print("Printing list of names: ", names)
        random_name = random.choice(names)
        print("Now picking a random name from the list...\nThe random name is: ", random_name)
        choice_for_repeat_name = False
        while choice_for_repeat_generate == True:
            user_choice_for_repeat = input("Generate again? (y/n): ")
            if user_choice_for_repeat == "y":
                random_name = random.choice(names)
                print("Generated name: ", random_name)
            elif user_choice_for_repeat == "n":
                choice_for_repeat_generate = False
            else:
                print("Invalid input.")
    else:
        print("Invalid input.")
