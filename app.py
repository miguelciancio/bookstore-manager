from PyQt5 import QtWidgets, uic
import sys
from ebookstore import create_database, grab_last_id, add_data, grab_all_data, delete_book_data


# Create thew third window.
class DeleteBookWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method

        # Variables that will receive the number of col or row of the table
        # from 'delete book' window.
        self.col, self.row = 0, 0

        self.main_window = None
        uic.loadUi('app_gui_3.ui', self)

        # Set-up size of each column.cd
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 600)
        self.tableWidget.setColumnWidth(3, 100)

        # Event Listener: capture when user clicks return button.
        self.returnMainWindow_pushButton.clicked.connect(self.returnMainWindow)

        # Execute function that loads all info of books table from the bookshop database (ebookstore.db).
        self.load_data()

        # Event Listener: capture moment that user selects a specific row of the table from 'delete book' window.
        self.tableWidget.cellClicked.connect(self.cellClick)

        # Event Listener: capture moment that user clicks on 'delete' button from 'delete book' window.
        self.deleteBook_pushButton.clicked.connect(self.deleteBook)


    def load_data(self):
        """Function that load all the data stored inside the database table's books and display them all on screen."""
        self.datas = grab_all_data()

        # Set the total number of rows according to the length of the table books
        # from the ebookstore.db database
        self.tableWidget.setRowCount(len(self.datas))

        # Get each individual data of each row from the table books and
        # display them into our screen (our table) in a user-friendly way.
        table_row = 0
        for row in self.datas:
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


    def deleteBook(self):
        """Functions that actually exclude item from database."""
        self.cell = []  # List that will store all cells values from the selected row.

        # Here, we iterate through all the rows inside the table and
        # grab only the selected row by the user.
        for col in range(len(self.datas[0])):
            self.cell.append(self.tableWidget.item(self.row, col).text())

        id_number = int(self.cell[0])  # get the ID primary key.

        delete_book_data(id_number)  # Pass ID primary key to a function that delete the data using it as parameter.

        self.load_data()  # Update screen with a new list as soon as user deletes one item from there.

    def cellClick(self, row, col):
        """Function that sets the row and column that the user selected."""
        self.row = row
        self.col = col


# Create the second window.
class AddNewBookWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        uic.loadUi('app_gui_2.ui', self)  # Load the .ui file

        self.main_window = None

        # Variables that will be used to either add a book or clear all inputs fields at once.
        self.last_id_book = grab_last_id()
        self.title = self.bookTitle_lineEdit
        self.author = self.bookAuthor_lineEdit
        self.quantity = self.bookQuantity_lineEdit

        # Event Listener: capture when user clicks return button.
        self.returnMainWindow_pushButton.clicked.connect(self.returnMainWindow)

        # Event Listener: capture when user clicks 'add' button.
        self.addNewBook_pushButton.clicked.connect(self.addNewBook)

        # Event Listener: capture when user clicks 'clear' button.
        # Clear all inputs field.
        self.clearInput_pushButton.clicked.connect(self.clearInput)

    def returnMainWindow(self):
        """Function that return to the main window when user clicks 'return' button."""
        self.main_window = Ui()
        self.main_window.show()
        self.close()

    def addNewBook(self):
        # Add new data to books table.
        self.id = self.last_id_book[0] + 1
        self.add_title = self.title.text().strip().title()
        self.add_author = self.author.text().strip().title()
        self.add_quantity = self.quantity.text().strip().title()

        # Add new data to database
        if not self.add_title or self.add_author or self.add_quantity:
            pass
        else:
            add_data(self.id, self.add_title, self.add_author, self.add_quantity)

        # CLear all inputs fields after successfully add the data into bookshop database.
        self.clearInput()

    def clearInput(self):
        """Simple function that clears all input fields at once."""
        self.title.setText("")
        self.author.setText("")
        self.quantity.setText("")


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


# ===== Main Application Execution =====
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()  # Start the application
