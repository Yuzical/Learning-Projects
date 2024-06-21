import csv
import os.path

email_list = "email_database.csv"
exist = os.path.isfile(email_list)

if not exist:
    e_DB = open(email_list, "w")  # create CSV in write mode
    e_DB.close()


def c_email():
    e_Name = input("Enter your Name.\n")
    e_User = input("Please enter in a Username for the Email.\n")
    e_Pass = input("Please enter in a Password for the Email.\n")
    print("Your email has successfully been created.")
    print("Your Username is " + e_User +
          "@yuzical.com \nYour Password is " + e_Pass)
    with open(email_list, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([e_Name, e_User, e_Pass])
    print("Data saved to " + email_list)


def d_email():
    with open(email_list, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    print("Current data in the CSV file:")
    for row in rows:
        print(row)
    e_to_delete = input(
        "Enter the name you want to delete from the database.\n")
    updated_rows = [row for row in rows if row[0] != e_to_delete]
    with open(email_list, mode='w', newline='') as file:
        writer = csv.writer(file)
        # write the updated rows to the CSV file
        writer.writerows(updated_rows)
    print(f"The data for {e_to_delete} has been deleted from the database.")
    return


print("Welcome to a Email Creation or Deletion Simulation")
email = input(
    "Would you like to create or delete an Email Address? (Please type Create or Delete)\n")
while email != 'Create' and email != 'Delete':
    print("Your input is invalid. Please Try again.")
    email = input(
        "Would you like to create or delete an Email Address? (Please type Create or Delete)\n")
    if email == 'Create' or email == 'Delete':
        break
if email == 'Create':
    c_email()
    exit()
elif email == 'Delete':
    d_email()
    exit()
