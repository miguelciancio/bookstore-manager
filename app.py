from PyQt5 import QtWidgets, uic
import sys
from ebookstore import create_database, add_data, grab_all_data, delete_book_data


# Create thew third window.
class DeleteBookWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method

        # Variables that will receive the number of col or row of the table
        # from 'delete book' window.
        self.col, self.row = 0, 0

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

        # Event Listener: capture moment that user selects a specific row of the table from 'delete book' window.
        self.tableWidget.cellClicked.connect(self.cellClick)

        # Event Listener: capture moment that user clicks on 'delete' button from 'delete book' window.
        self.deleteBook_pushButton.clicked.connect(self.deleteBook)


    def load_data(self):
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


# ===== Main Application Execution =====
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()  # Start the application
