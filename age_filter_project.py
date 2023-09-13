# Declare global values
database = []
age_filter = 0


def main():
    print("Welcome to the age filter 2.0...")

    get_data()

    while True:
        more = input("Add another person? Y/N: ").upper()
        if more == "Y":
            get_data()
        elif more == "N":
            break

    try:
        age_filter = int(input("Enter age to filter by: "))
    except ValueError:
        print("Please enter age.")

    print(f"The people over the age of {age_filter} are:")
    i = 0
    while i < len(database):
        if int(database[i]["Age"]) > age_filter:
            print(database[i]["Name"])
        i += 1

    print(f"The people under the age of {age_filter} are:")
    y = 0
    while y < len(database):
        if int(database[y]["Age"]) < age_filter:
            print(database[y]["Name"])
        y += 1


def get_data():
    name = input("Name: ")
    if not name.isalpha():
        print("Please enter a name")
        name = input("Name: ")
    name = name.lower()
    name = name.capitalize()

    age = input("Age: ")
    if not age.isdigit():
        print("Please enter an age")
        age = input("Age: ")

    database.append({"Name": name, "Age": age})


main()
