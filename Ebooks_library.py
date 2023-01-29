import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox

db = sqlite3.connect('ebookstore_db')
cursor = db.cursor() # Get a cursor object
# Create a table called books
cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
db.commit()

id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = 'Harry Potter and the Philosopher\'s Stone' 
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = 'The Lord of the Ring'
Author4 = 'J.R.R. Tolkien'
Qty4 = 37

id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

id6 = 3006
Title6 = 'I Promessi Sposi'
Author6 = 'Alessandro Manzoni'
Qty6 = 55
# Insert first book
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id1, Title1, Author1, Qty1))

 # Insert second book    
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id2, Title2, Author2, Qty2))

#Insert third book 
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                 VALUES(?,?,?,?)''', (id3, Title3, Author3, Qty3))

# Insert fourth book
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id4, Title4, Author4, Qty4))

# Insert fifth book
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id5, Title5, Author5, Qty5))

# Insert sixth book
cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                VALUES(?,?,?,?)''', (id6, Title6, Author6, Qty6))

db.commit()
db.close()

# Creating and setting up the main window of the app 
window = Tk()
window.geometry('1100x550')
window.title("Books Inventory")
# Creating and configuring labels and entries of the app
# Header
header_label = Label(window, text='BOOK INVENTORY', font=('Arial', 20, 'bold'), pady=15)
header_label.config(justify='center')
header_label.grid(row=0, column=4, sticky=E)

# Id
id_text = StringVar()
id_label = Label(window, text='Id', font=('Arial', 13, 'bold'), pady=10, padx=5)
id_label.grid(row=2, column=0, sticky=E)
id_entry = Entry(window, textvariable=id_text)
id_entry.grid(row=2, column=1, sticky=W)

# Title
title_text = StringVar()
title_label = Label(window, text='Title', font=('Arial', 13, 'bold'), pady=10, padx=5)
title_label.grid(row=3, column=0, sticky=E)
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=3, column=1, sticky=W)

# Author
author_text = StringVar()
author_label = Label(window, text='Author', font=('Arial', 13, 'bold'), pady=10, padx=5)
author_label.grid(row=4, column=0, sticky=E)
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row= 4, column=1, sticky=W)

# Quantity
qty_text = StringVar()
qty_label = Label(window, text='Quantity', font=('Arial', 13, 'bold'), pady=10, padx=5)
qty_label.grid(row=5, column=0, sticky=E)
qty_entry = Entry(window, textvariable=qty_text)
qty_entry.grid(row=5, column=1, sticky=W)

# Function to insert a book in the database 
def submit():
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM books")
        books = cursor.fetchall()
        id = ''
        for values in books:
            id += str(values[0])
            print(id)
            # Create an error message if not all the fields are included or the id is invalid
            if id_text.get() == '' or title_text.get() == '' or author_text.get() == '' or qty_text.get() == '' or id_text.get() in id:
                messagebox.showerror('Required Fields', 'Please include all fields')
                return
        # Update the database    
        cursor.execute("INSERT INTO books(id, Title, Author, Qty) VALUES (?,?,?,?)",(id_text.get(),title_text.get(),author_text.get(),qty_text.get())) 
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        print('Connection to database closed')
 

# Create and configure the submit button
submit_button = Button(window, text="Enter Book", command=submit)
submit_button.config(font=('Arial', 10))
submit_button.grid(row=2, column=2, columnspan=1, pady=10, padx=10)

# Function to display the database
def query():
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor()
        cursor.execute("SELECT *, oid FROM books")
        books = cursor.fetchall()
        print(books)
        print_records = ''
        for values in books:
            # Display the data
            print_records += 'ID: ' + str(values[0]) + ", Title: " + str(values[1]) + ', Author: ' + str(values[2]) + ", Quantity: " + str(values[3]) +"\n"
        # Create and configurate the query label
        query_label = Label(window, text=print_records)
        query_label.config(justify='left', font=('Courier New', 15))
        query_label.grid(row=15, column=1, columnspan=25, padx=10, pady=15)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e

    finally:
        connection.close()
        print('Connection to database closed')

# Create and configurate the query button
query_btn = Button(window,  text="Show Books", command=query)
query_btn.config(font=('Arial', 10))
query_btn.grid(row=4, column=2, columnspan=2, pady=10, padx=10)

# Function to search for a book
def search():
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor()
        # Display the selected book
        cursor.execute('''SELECT * FROM books WHERE id = ? OR title = ? OR author=? OR qty=?''', (id_text.get(), title_text.get(), author_text.get(), qty_text.get()))
        book = cursor.fetchall()
        print_book = str(book) + '\n'
        # Create and configure the search label
        search_label = Label(window, text=print_book)
        search_label.config(font=('Courier New', 15))
        search_label.grid(row=6, column=0, columnspan=6)
        connection.commit()
    except:
        messagebox.showerror('ciao')
    finally:
        connection.close()
   
# Create and configure the search button
search_button = Button(window, text = 'Search Book', command = search)
search_button.config(font=('Arial', 10))
search_button.grid(row=3, column = 2, columnspan= 2, pady=10, padx=10)

# Function to update the database
def update():
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor()
        record_id = select_box.get()
        # Upadte the book details
        cursor.execute(
            'UPDATE books SET Title=?, Author=?, Qty=? WHERE oid=?',
            (title_text_editor.get(),author_text_editor.get(),qty_text_editor.get(),record_id))
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        editor.destroy()
        print('Connection to database closed')
   
# Create and configurate the 'ID Book' label and entry
select_box=Entry(window, width=20)
select_box.grid(row=2, column=5, pady=2, sticky=W)
select_box_label = Label(window, text='ID Book', font=('Arial', 13, 'bold'), justify='left')
select_box_label.grid(row=2, column=4, pady=2, padx=5, sticky=E)

# Function to edit a book
def edit():
    global editor
    # Create and configure a secondary window
    editor = Tk()
    editor.geometry("450x125")
    editor.title("Update Inventory")
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor() # Get a cursor object
        record_id = select_box.get()
        # Display in the secondary window the book to edit
        cursor.execute("SELECT * FROM books WHERE oid=?",[record_id])
        records = cursor.fetchall()
        # Set the global variables 
        global title_text_editor
        global author_text_editor
        global qty_text_editor
        # Creating and configuring the entries and labels for the secondary app window 
        # Title
        title_text_editor = Entry(editor, width=20)
        title_text_editor.config(font=('Arial', 10))
        title_text_editor.grid(row=0, column=1, sticky=W)
        title_text_label_editor = Label(editor, text='Title ', font=('Arial', 12))
        title_text_label_editor.grid(row=0, column=0, sticky=E)
        # Author
        author_text_editor = Entry(editor, width=20)
        author_text_editor.config(font=('Arial', 10))
        author_text_editor.grid(row=1, column=1, sticky=W)
        author_text_label_editor = Label(editor,  text='Author ', font=('Arial', 12))
        author_text_label_editor.grid(row=1, column=0, sticky=E)
        # Quantity
        qty_text_editor = Entry(editor, width=20)
        qty_text_editor.config(font=('Arial', 10))
        qty_text_editor.grid(row=2, column=1, sticky=W)
        qty_text_label_editor = Label(editor, text ='Qty ', font=('Arial', 12))
        qty_text_label_editor.grid(row=2,column=0, sticky=E)
        # Insert the new values in the database 
        for values in records:
            title_text_editor.insert(0, values[1])
            author_text_editor.insert(0, values[2])
            qty_text_editor.insert(0, values[3])
        # Create and configure the Save Book button
        save_button = Button(editor, text="Save Book", command=update)
        save_button.config(font=('Arial', 10))
        save_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        print('Connection to database closed')
    # Run the secondary window app
    editor.mainloop()

# Create and configure the Update Book button
edit_button = Button(window, text="Update Book", command=edit)
edit_button.config(font=('Arial', 10))
edit_button.grid(row=3, column=5, columnspan=2, pady=10, padx=10)

# Function to delete a book
def delete():
    try:
        connection = sqlite3.connect("ebookstore_db")
        cursor = connection.cursor()
        # Delete the data from the database
        cursor.execute("DELETE FROM books WHERE oid=?",[select_box.get()])
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        print('Connection to database closed')
    
# Create and configure the Delete Book button
delete_button = Button(window, text='Delete Book', command=delete)
delete_button.config(font=('Arial', 10))
delete_button.grid(row=4, column=5, columnspan=2, pady=10, padx=10)

# Function to clear the input
def clear_input():
    id_entry.delete(0, END)
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    qty_entry.delete(0, END)
# Create and configure the Clear input button
clear_input_button = Button(window, text='Clear Input', command= clear_input)
clear_input_button.config(font=('Arial', 10))
clear_input_button.grid(row=5, column=2, columnspan=2, pady=10, padx=10)
        
# Run the main window app
window.mainloop()
