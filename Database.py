#imports
import sqlite3

#contants and variables
DATABASE = "Members.db"



#functions
def print_all_members():
    '''print all members nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT ID,Name,Last_name,Age FROM members;" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"ID          Name        Last_name   Age")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12}{members[2]:<12}{members[3]:<12}")
    db.close()

def print_all_gender():
    '''print all gender nicely'''
    db = sqlite3.connect(DATABASE)
    #Ask user gender type
    Gender = input("View gender: ")
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Gender == ?;"
    cursor.execute(sql,(Gender,))
    results = cursor.fetchall()
    print(f"Id          Name        Last_name   Age         Gender      Birthday    Interests   ")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12}{members[2]:<12}{members[3]:<12}{members[4]:<12}{members[5]:<12}{members[6]:<12}")
    db.close()

def print_all_interests():
    '''print all interests nicely'''
    db = sqlite3.connect(DATABASE)
    #Ask user interests 
    Interests = input("What is your interests: ")
    cursor = db.cursor()
    sql = "SELECT Name,Last_name,Interests from members WHERE Interests == ?;" 
    cursor.execute(sql,(Interests,))
    results = cursor.fetchall()
    print(f"Name        Last_name   Interests")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12}{members[2]:<12}")
    db.close()

def print_all_age_between():
    '''print all age between nicely'''
    db = sqlite3.connect(DATABASE)
    #ask user upper age
    #ask user lower_age
    lower_age = int(input("What is the lowest age?: "))
    upper_age = int(input("What is the highest age?: "))
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Age BETWEEN ? AND ?;" 
    cursor.execute(sql,(lower_age,upper_age))
    results = cursor.fetchall()
    print(f"Id          Name        Last_name   Age         Gender      Birthday    Interests")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12}{members[2]:<12}{members[3]:<12}{members[4]:<12}{members[5]:<12}{members[6]:<12}")
    db.close()

def print_all_birthday():
    '''print all birthday nicely'''
    db = sqlite3.connect(DATABASE)
    #view birthday's less than 
    Birthday = input("View birthday's greater than: ")
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Birthday > ?;" 
    cursor.execute(sql,(Birthday,))
    results = cursor.fetchall()
    print(f"Id          Name        Last_name   Age         Gender      Birthday    Interest")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12}{members[2]:<12}{members[3]:<12}{members[4]:<12}{members[5]:<12}{members[6]:<12}")
    db.close()

def print_all_birthday_between():
    '''print all birthday between nicely'''
    db = sqlite3.connect(DATABASE)
    #View birthday's between
    Lower_birthday = input("Type in the lower birthday: ")
    Upper_birthday = input("Type in the upper birthday: ") 
    cursor = db.cursor()
    sql = "SELECT Name,Last_name,Age,Birthday FROM members WHERE Birthday BETWEEN ? AND ?;"
    cursor.execute(sql,(Lower_birthday,Upper_birthday))
    results = cursor.fetchall()
    print(f"Name        Last_name    Age               Birthday")
    for members in results:
        print(f"{members[0]:<12}{members[1]:<12} Age: {members[2]:<12} Birthday: {members[3]:<12}")
    db.close()


#main code

print("welcome to the dating database,in this database you can view all information about each person")
while True:
    user_input = input(
"""
What would you like to do.
1. Print all members
2. Print all gender
3. Print all interests
4. Print all age between
5. Print all birthday
6. Print all birthday between
""")
    if user_input == "1":
        print_all_members()
    elif user_input == "2":
        print_all_gender()
    elif user_input == "3":
        print_all_interests()
    elif user_input == "4":
        print_all_age_between()
    elif user_input == "5":
        print_all_birthday()
    elif user_input == "6":
        print_all_birthday_between()
    elif user_input == "7":
        break
    #add another elif and break
    else:
        print("That was not an option\n")



