
import sqlite3

def display_all_member():
    db = sqlite3.connect("Members.db")
    cursor = db.cursor()
    sql = "SELECT * from members;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close()


#main loop
while True:
    #options- ask user what they want to do
    option = input()
    #if option 1----
    if option == "1":
        display_all_member()
    #elif option 2----- etc
    if option =="2":
       Display_Birthday
   
   
    #elif option 9- exit the loop
    if option == "9":
        print("Goodbye")
        break