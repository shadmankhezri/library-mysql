from mysql.connector import connect,Error
#------------------------------
## Creating a database with the name dblibrary
try:
    with connect(host="localhost" , user="root" , password="123456789") as db:
        my_cursor = db.cursor()
        my_cursor.execute("create database dblibrary")
        print("database created...")

except Error as error:
    print(error)
    print(100*"-")
#------------------------------
## create table for dblibrary with the name T_Book
try:
    with connect(host="localhost" , user="root" , password="123456789" , database="dblibrary") as db:
        my_cursor = db.cursor()
        order_table = '''
                    create table T_Book(
                    bookCode int primary key,
                    Title varchar(50),
                    Author varchar(50),
                    Publisher varchar(50)
                )
        '''
        my_cursor.execute(order_table)
        db.commit()

except Error as error:
    print(error)
    print(100*"-")
#------------------------------
## insert books to database
def insert_book(code , title , author , publisher):
    try:
        with connect(host="localhost" , user="root" , password="123456789" , database="dblibrary") as db:
            my_cursor = db.cursor()
            my_cursor.execute(f"insert into T_book(bookCode , Title , Author , Publisher) values({code},'{title}','{author}','{publisher}')")
            db.commit()
            print("*** The book has been successfully added ***\n",100*"-")

    except Error as error:
        print(error)
#------------------------------
## delete book from database
def delete_book(code):
    try:
        with connect(host="localhost" , user="root" , password="123456789" , database="dblibrary") as db:
            my_cursor = db.cursor()
            my_cursor.execute(f"delete from T_book where bookCode = {code}")
            db.commit()
            print("*** The selected book has been successfully deleted ***\n",100*"-")

    except Error as error:
        print(error)
#------------------------------
## search book from database
def search_book(code):
    try:
        with connect(host="localhost" , user="root" , password="123456789" , database="dblibrary") as db:
            my_cursor = db.cursor()
            my_cursor.execute(f"select * from T_book where bookCode = {code}")
            books = my_cursor.fetchall()
            for book in books:
                print(f"Book information selected with code {code}")
                print(f"The title of the book: {book[1]}\nthe writer: {book[2]}\npublisher: {book[3]}")
                print(100*"-")

    except Error as error:
        print(error)
#------------------------------
## show all book
def show_all_book():
    print("Details of all books\n")
    try:
        with connect(host="localhost" , user="root" , password="123456789" , database="dblibrary") as db:
            my_cursor = db.cursor()
            my_cursor.execute("select * from T_book")
            books = my_cursor.fetchall()
            for book in books:
                print(book)
                print(100*"-")

    except Error as error:
        print(error)
#------------------------------
## The main program
choice = 1
while choice != 0:
    print("*** MENU ***\n1-Insert New Book\n2-Delete Book\n3-Search Book\n4-Show All Books")
    print(100*"-")
    choice = int(input("Enter your choice: "))
    print(100*"-")
    if choice == 0:
        print("EXIT")
    ###------------------------
    elif choice == 1:
        code = int(input("Enter code: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        insert_book(code , title , author , publisher)
    ###------------------------
    elif choice == 2:
        code = int(input("Enter Book Code for Delete:"))
        delete_book(code)
    ###------------------------
    elif choice == 3:
        code = int(input("Enter code:"))
        search_book(code)       
    ###------------------------
    elif choice == 4:
        show_all_book()
