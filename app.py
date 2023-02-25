from PyQt5 import QtWidgets, uic
import sys
from ebookstore import create_database, add_data, grab_all_data


# Create thew third window.
class DeleteBookWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.main_window = None
        uic.loadUi('app_gui_3.ui', self)

        # Set-up size of columns
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 600)
        self.tableWidget.setColumnWidth(3, 100)

        # Event Listener: capture when user clicks return button.
        self.returnMainWindow_pushButton.clicked.connect(self.returnMainWindow)

        # Execute function that loads all info of books table from the bookshop database (ebookstore.db).
        self.load_data()


    def load_data(self):
        datas = grab_all_data()

        # Set the total number of rows according to the length of the table books
        # from the ebookstore.db database
        self.tableWidget.setRowCount(len(datas))

        # Get each individual data of each row from the table books and
        # display them into our screen (our table) in a user-friendly way.
        table_row = 0
        for row in datas:
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            table_row += 1

    def returnMainWindow(self):
        """Function that return to the main window when user clicks 'return' button."""
        self.main_window = Ui()
        self.main_window.show()
        self.close()


# Create the second window.
class AddNewBookWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.main_window = None
        uic.loadUi('app_gui_2.ui', self)  # Load the .ui file

        # Event Listener: capture when user clicks return button.
        self.returnMainWindow_pushButton.clicked.connect(self.returnMainWindow)

    def returnMainWindow(self):
        """Function that return to the main window when user clicks 'return' button."""
        self.main_window = Ui()
        self.main_window.show()
        self.close()


#  Create a base class that will load the .ui file in the constructor
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        self.delete_book_window = None
        self.add_new_book_window = None
        uic.loadUi('app_gui.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

        # Event Listener: captures when user clicks 'add' button.
        self.addNewBook_pushButton.clicked.connect(self.AddNewBookWindow)

        # Event Listener: captures when user clicks 'delete' button.
        self.deleteBook_pushButton.clicked.connect(self.DeleteBookWindow)

    def AddNewBookWindow(self):
        """Function that opens the second window (add new book) when user clicks 'add' button."""
        self.add_new_book_window = AddNewBookWindow()
        self.add_new_book_window.show()
        self.close()

    def DeleteBookWindow(self):
        """Function that opens the third window (delete book) when user clicks 'delete' button."""
        self.delete_book_window = DeleteBookWindow()
        self.delete_book_window.show()
        self.close()


# Create a database and add initial values into it.
create_database()

# Add initial values to our database.
add_data(3001, 'A Tale of Two Cities', 'Charles Dickens', 30)
add_data(3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40)
add_data(3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25)
add_data(3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37)
add_data(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)

# ===== Main Application Execution =====
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()  # Start the application
