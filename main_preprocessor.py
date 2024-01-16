import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
#from SAPR_choise_window import Ui_MainWindow
from SAPR_preprocessor import Ui_MainWindow
from SAPR_preprocessor_dialog import Ui_Dialog
#from SAPR_processor import Ui_MainWindow
#from SAPR_postprocessor import Ui_MainWindow

class Preprocessor(QMainWindow):
    def __init__(self):
        super(Preprocessor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def open_preprocessor_dialog(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.pushButton.clicked.connect(self.add_new_transaction)

class Preprocessor_dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Preprocessor_dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Preprocessor()
#     dialog = Preprocessor_dialog()
#     opened = False
#     window.show()
#     if opened == False:
#         dialog.show()
#         opened = True
#     sys.exit(app.exec())