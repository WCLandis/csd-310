import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#WhatABook main menu. Assistance with ValueError and sys.exit utilizing Richard Krasso's original file.

def show_menu():
    print("\n  Main Menu")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        user_input = int(input('What Would You Like To Do?: '))
        return user_input

    except ValueError:
        print("\n  You Have Entered an Invalid Number, Program Ended \n")
        sys.exit(0)

#Show available books from WhatABook database. Assistance with book formatting utilizing Richard Krasso's original file.

def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details from book")


    books = _cursor.fetchall()

    print("\n Displaying Book")
    
  
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

#Retrieve WhatABook locations. Assistance with location formatting utilizing Richard Krasso's original file.

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n Showing Store Locations")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#WhatABook user validation. Assistance with ValueError and sys.exit utilizing Richard Krasso's original file.

def validate_user():
    
    try:
        user_id = int(input('\n Please Enter Your Customer ID: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid Customer ID, Program Ended\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid Number, Program Ended\n")
        sys.exit(0)

#User account menu. Assistance with ValueError and sys.exit utilizing Richard Krasso's original file.

def show_account_menu():

    try:
        print("\n  Customer Menu")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        
        user_account_options = int(input('What Would You Like to Do?: '))
        return user_account_options

    except ValueError:
        print("\n  Invalid Number, Program Ended\n")
        sys.exit(0)

#Show user wishlist. Assistance with SQL query utilizing Richard Krasso's original file.

def show_wishlist(_cursor, _user_id):
  
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n  Your Wishlist")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

#Show books to add to user wishlist. Assistance with sql_query utilizing Richard Krasso's original file.

def show_books_to_add(_cursor, _user_id):
 

    sql_query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(sql_query)

    _cursor.execute(sql_query)

    books_to_add = _cursor.fetchall()

    print("\n  Available Books")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

#Add book to user's wishlist.

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:


    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 

    print("\n  Welcome to WhatABook")

    user_selection = show_menu() 

 #WhatABook user selections and account options. Assistance with user_selection and account_option nested 'if' statements utilizing Richard Krasso's original file.

    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:


                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                
                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("\n  Please Enter the Book ID You Would Like to Add: "))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("\n        Book ID: {} was added to your wishlist!".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("\n   Invalid Selection, Try Again")

                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("\n  Invalid Selection, Try Again")
            
        user_selection = show_menu()

    print("\n\n  Program Ended")

#WhatABook error handling. Written by: Richard Krasso

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The Username or Password is Invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("This Database Does Not Exist")

    else:
        print(err)

finally:

    db.close()
