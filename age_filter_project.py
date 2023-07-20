import time

name_list = []
age_list = []
agefilter = 0
filtcombined = dict()


def output():
    if filtcombined == dict():
        print("There is nobody inside your parameters\n")
        time.sleep(1)
    elif filtcombined != dict():
        print("The people older then %s are: " % str(agefilter))
        for i in filtcombined:
            print(i)


def sassy_end():
    print("Oh I see how it is...")
    time.sleep(1)
    print("Fine then...")
    time.sleep(2)
    print("Bye!")
    time.sleep(5)
    exit()


def filter_applied():
    global agefilter
    agefilter = int(input("Enter the age to filter by:\n"))
    combined = dict(zip(name_list, age_list))
    for (key, value) in combined.items():
        if value >= agefilter:
            filtcombined[key] = value
    output()


def questions():
    global name_list
    global age_list
    new_name = input("Enter a name or End to finish:\n").capitalize()
    time.sleep(1)
    if new_name != "End":
        new_age = input("Enter their Age:\n")
        time.sleep(1)
        name_list.append(new_name)
        age_list.append(int(new_age))
        questions()
    elif new_name == "End":
        filter_applied()


def start():
    user_input = input("Age Filter - Enter Names, "
                            "Age and what age to filter from... "
                            "Type go to start or no to stop:\n")
    if user_input.lower() == "go":
        time.sleep(1)
        print("Lets go!")
        time.sleep(1)
        questions()
    elif user_input.lower() == "no":
        sassy_end()
    elif user_input.lower() != "go":
        print("Please read and try again...\n")
        time.sleep(1)
        start()


start()


def restart():
    global name_list
    global age_list
    global agefilter
    global filtcombined
    time.sleep(1)
    restart_check = input("Do you wish to start again? Yes/No\n").lower()
    if restart_check == "no":
        sassy_end()
    elif restart_check == "yes":
        name_list = []
        age_list = []
        agefilter = 0
        filtcombined = dict()
        start()
    elif restart_check != "no" or "yes":
        time.sleep(1)
        print("Please type yes or no...")
        time.sleep(1)
        restart()


while agefilter != 0:
    restart()
