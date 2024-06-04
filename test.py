#imports
import sqlite3

#contants and variables
DATABASE = "Members.db"

#functions
def print_all_age():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Name,Last_name,Age from members WHERE Age > 30;" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

def print_all_male():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Gender = 'Male';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

def print_all_blogging():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Name,Last_name,Interests from members WHERE Interests = 'Blogging';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

def print_all_age_between():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Age BETWEEN 25 AND 35;" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

def print_all_birthday():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM members WHERE Birthday > '1990/01/01';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close

def print_all_birthday_between():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT *FROM members WHERE Birthday BETWEEN '1965/01/01' AND '1999/01/01';" 
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close


#main code
while True:
    user_input= input(
"""
What would you like to do.
1. Print all age
2. Print all male
3. Print all blogging
4. Print all age between
5. Print all birthday
6. Print all birthday between
""")
    if user_input == "1":
        print_all_age()
    elif user_input == "2":
        print_all_male()
    elif user_input == "3":
        print_all_blogging
    elif user_input == "4":
        print_all_age_between()
    elif user_input == "5":
        print_all_birthday()
    elif user_input == "6":
        print_all_birthday_between()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")



