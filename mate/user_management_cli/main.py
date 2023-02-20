import os.path
import csv


DB_FILE_NAME = "users.csv"
HEADERS = ["name", "surname", "age"]


def create_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("User's age: ")

    file_exists = os.path.isfile(DB_FILE_NAME)

    with open(DB_FILE_NAME, "a", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow([name, surname, age])
    print("Done")


def read_user():
    if not os.path.isfile(DB_FILE_NAME):
        print("File doesn't exist")
        return

    user = input("Input the name of user to get full info: ")
    with open(DB_FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == user:
                print("Result: ", row)


def update_user():
    if not os.path.isfile(DB_FILE_NAME):
        print("file doesn't exist")
        return




def delete_user():
    print("Delete")


def user_management_cli():
    while True:
        command = input(">>>")

        if command == "create user":
            create_user()
        elif command == "read user":
            read_user()
        elif command == "update user":
            update_user()
        elif command == "delete user":
            delete_user()
        elif command == "exit":
            print("Exiting")
            break
        else:
            print("Unsupported command!")


if __name__ == '__main__':
    user_management_cli()
