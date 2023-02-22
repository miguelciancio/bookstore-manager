from PyQt5 import QtWidgets, uic
import sys


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
        self.add_new_book_window = None
        uic.loadUi('app_gui.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

        # Event Listener: captures when user clicks add button.
        self.addNewBook_pushButton.clicked.connect(self.AddNewBookWindow)

    def AddNewBookWindow(self):
        """Function that opens the second window (add new book) when user clicks 'add' button."""
        self.add_new_book_window = AddNewBookWindow()
        self.add_new_book_window.show()
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()  # Start the application
