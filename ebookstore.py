import sqlite3


def create_database():
    """Function that creates a database that for a bookshop."""
    # Creates or opens a database file called ebookstore.
    db = sqlite3.connect('ebookstore.db')

    # Get a cursor
    cursor = db.cursor()

    # Create a table.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 
            books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                quantity INTEGER
            )
        ''')

    # Commit the changes
    db.commit()

    # Close our connection.
    db.close()


def add_data(id, title=None, author=None, quantity=None):
    """Function that adds any a new book to the bookshop database."""
    # Open bookshop database.
    db = sqlite3.connect('ebookstore.db')

    # Get a cursor
    cursor = db.cursor()

    # Insert the data if not inside it.
    data = [
        id,
        title,
        author,
        quantity
    ]

    cursor.execute("""
        INSERT OR IGNORE INTO 
            books(
                id, 
                title, 
                author, 
                quantity
            ) 
        VALUES(?,?,?,?)
    """, data)

    # Commit changes.
    db.commit()

    # Close connection
    db.close()


def grab_all_data():
    """Function that grab all data stored inside books table from ebookstore.db"""
    # Connect to the database.
    db = sqlite3.connect('ebookstore.db')

    # Create a cursor
    cursor = db.cursor()

    # Grab all data and store them into a variable; Return this variable.
    cursor.execute('''
        SELECT
            *
        FROM
            books
    ''')

    records = cursor.fetchall()

    # Close connection
    db.close()

    return records


def delete_book_data(id):
    """Function that deletes a specific book data according to its unique ID number."""
    # Connect to the database
    db = sqlite3.connect('ebookstore.db')

    # Create a cursor.
    cursor = db.cursor()

    # Delete the book's data.
    cursor.execute("""
        DELETE FROM
            books
        WHERE
            id = ?
    """, (id,))

    # Commit the changes
    db.commit()

    # Close database connection.
    db.close()


def check_database():
    # Open database
    db = sqlite3.connect('ebookstore.db')

    # get cursor
    cursor = db.cursor()

    # fetch all data and save into a variable
    cursor.execute("""
        SELECT
            *
        FROM 
            books 
    """)
    records = cursor.fetchall()

    # Print out database info
    print(records)