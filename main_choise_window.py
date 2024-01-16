import sys
from  PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from SAPR_choise_window import Ui_MainWindow
from SAPR_preprocessor import Ui_MainWindow as Preprocessor
from SAPR_preprocessor_dialog import Ui_Dialog as Preprocessor_dialog
#from main_preprocessor import Preprocessor, Preprocessor_dialog
from SAPR_error_1 import Ui_Dialog as Error_1_Dialog
from SAPR_error_2 import Ui_Dialog as Error_2_Dialog
from SAPR_error_3 import Ui_Dialog as Error_3_Dialog
from SAPR_error_4 import Ui_Dialog as Error_4_Dialog
from SAPR_error_5 import Ui_Dialog as Error_5_Dialog
#from SAPR_processor import Ui_MainWindow
#from SAPR_postprocessor import Ui_MainWindow

vocabulary_zadelka = {
    False: "нет",
    True: "есть"
}

# class Kernel_model(QtCore.QAbstractTableModel):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#
#     def set_kernel(self, kernel):
#         pass
#
#     def set_param(self, param):
#         pass
#
#     def rowCount(self, *args, **kwargs) -> int:
#         return super().rowCount()
#
#     def data(self, index, role = ...):
class SAPR(QMainWindow):
    opened = False
    kernels = 1
    sosr = 2
    raspr = 1
    list_of_length = []
    list_of_square = []
    list_of_modul = []
    list_of_voltage = []
    list_of_sosr = []
    list_of_raspr = []
    def __init__(self):
        super(SAPR, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.opened = False

        #self.model = Kernel_model()
        #self.ui.table_kernel.setModel(self.model)

        self.ui.preprocessor_btn.clicked.connect(self.open_Preprocessor)
        self.ui.processor_btn.clicked.connect(self.open_error)
        self.ui.postprocessor_btn.clicked.connect(self.open_error)
        self.Preprocessor_window = QtWidgets.QMainWindow()
        self.Preprocessor_idea = Preprocessor()
        self.Preprocessor_idea.setupUi(self.Preprocessor_window)


    def open_Preprocessor(self):
        if self.opened == False:
            self.open_change_preprocessor()
        else:
            #self.dialog = Preprocessor_dialog()
            self.Preprocessor_window.show()
            self.Preprocessor_idea.table_kernel.cellChanged.connect(self.table)
            self.Preprocessor_idea.table_sosr.cellChanged.connect(self.table)
            self.Preprocessor_idea.table_raspr.cellChanged.connect(self.table)
            self.Preprocessor_idea.button_change.clicked.connect(self.open_change_preprocessor)
            self.Preprocessor_idea.button_plus_kernel.clicked.connect(self.add_kernel)
            self.Preprocessor_idea.button_minus_kernel.clicked.connect(self.delete_kernel)
            self.Preprocessor_idea.button_ok_kernel.clicked.connect(self.OK_kernel)
        # if opened == False:
        #     self.dialog.show()
        #     opened = True
        #     print(opened)

    def open_error(self):
        self.error_1_window = QtWidgets.QDialog()
        self.error_1_idea = Error_1_Dialog()
        self.error_1_idea.setupUi(self.error_1_window)
        self.error_1_window.show()
    ########################################################
    def open_change_preprocessor(self):
        self.change_window = QtWidgets.QDialog()
        self.change_idea = Preprocessor_dialog()
        self.change_idea.setupUi(self.change_window)
        self.change_idea.pushButton.clicked.connect(self.change_preprocessor)
        self.change_window.show()

    def change_preprocessor(self):
        try:
            count_kernel = int(self.change_idea.textEdit.toPlainText())
        except ValueError:
            self.error_2_window = QtWidgets.QDialog()
            self.error_2_idea = Error_2_Dialog()
            self.error_2_idea.setupUi(self.error_2_window)
            self.error_2_window.show()
        else:
            if count_kernel <= 0:
                self.error_5_window = QtWidgets.QDialog()
                self.error_5_idea = Error_5_Dialog()
                self.error_5_idea.setupUi(self.error_5_window)
                self.error_5_window.show()
            else:
                number_of_sosr = count_kernel+1
                number_of_raspr = int(count_kernel)
                zadelka_l = vocabulary_zadelka[self.change_idea.checkBox.isChecked()]
                zadelka_r = vocabulary_zadelka[self.change_idea.checkBox_2.isChecked()]
                if (zadelka_l == 'нет' and zadelka_r == 'нет'):
                    self.error_3_window = QtWidgets.QDialog()
                    self.error_3_idea = Error_3_Dialog()
                    self.error_3_idea.setupUi(self.error_3_window)
                    self.error_3_window.show()
                else:
                    self.Preprocessor_idea.label_zadelka_l.setText(f"{zadelka_l}")
                    self.Preprocessor_idea.label_zadelka_r.setText(f"{zadelka_r}")

                    self.kernels = count_kernel
                    self.sosr = number_of_sosr
                    self.raspr = number_of_raspr

                    SAPR.change_kernel(self)
                    if self.opened == False:
                        print (self.opened)
                        self.change_window.close()
                        self.opened = True
                        self.open_Preprocessor()
                    else:
                        print (self.opened)
                        self.change_window.close()
            # self.kernels+=1
            # self.sosr+=1
            # self.raspr+=1

    def change_kernel(self):
        count_kernels = self.Preprocessor_idea.table_kernel.rowCount()
        print(count_kernels, self.kernels)
        if count_kernels < self.kernels:
            for i in range (0, self.kernels-1):
                count_kernels = self.Preprocessor_idea.table_kernel.rowCount()
                count_sosr = self.Preprocessor_idea.table_sosr.rowCount()
                count_raspr = self.Preprocessor_idea.table_raspr.rowCount()
                self.Preprocessor_idea.table_kernel.insertRow(count_kernels)
                new_item_name_kernel = QTableWidgetItem()
                new_item_name_kernel.setText(f'{count_kernels + 1}:')
                self.Preprocessor_idea.table_kernel.setVerticalHeaderItem(count_kernels, new_item_name_kernel)

                self.Preprocessor_idea.table_sosr.insertRow(count_sosr)
                new_item_name_sosr = QTableWidgetItem()
                new_item_name_sosr.setText(f'{count_sosr + 1}:')
                self.Preprocessor_idea.table_sosr.setVerticalHeaderItem(count_sosr, new_item_name_sosr)
                #self.sosr += 1

                self.Preprocessor_idea.table_raspr.insertRow(count_raspr)
                new_item_name_raspr = QTableWidgetItem()
                new_item_name_raspr.setText(f'{count_raspr + 1}:')
                self.Preprocessor_idea.table_raspr.setVerticalHeaderItem(count_raspr, new_item_name_raspr)
                #self.raspr += 1

            SAPR.show_kernel(self)
        if count_kernels > self.kernels:
            for i in range (count_kernels, self.kernels-1, -1):
                if i > -1:
                    self.Preprocessor_idea.table_kernel.removeRow(i)
                    self.Preprocessor_idea.table_kernel.selectionModel().clearCurrentIndex()

                    self.Preprocessor_idea.table_sosr.removeRow(i + 1)
                    self.Preprocessor_idea.table_sosr.selectionModel().clearCurrentIndex()
                    #self.sosr -= 1

                    self.Preprocessor_idea.table_raspr.removeRow(i)
                    self.Preprocessor_idea.table_raspr.selectionModel().clearCurrentIndex()
                    #self.raspr -= 1

                    for item in range(0, self.kernels + 1):
                        item_name_kernel = QTableWidgetItem()
                        item_name_kernel.setText(f'{item}:')
                        self.Preprocessor_idea.table_kernel.setVerticalHeaderItem(item - 1, item_name_kernel)
                        # self.Preprocessor_idea.table_sosr.insertRow(count_sosr)

                    for item in range(0, self.sosr + 1):
                        item_name_sosr = QTableWidgetItem()
                        item_name_sosr.setText(f'{item}:')
                        self.Preprocessor_idea.table_sosr.setVerticalHeaderItem(item - 1, item_name_sosr)

                    for item in range(0, self.raspr + 1):
                        item_name_raspr = QTableWidgetItem()
                        item_name_raspr.setText(f'{item}:')
                        self.Preprocessor_idea.table_raspr.setVerticalHeaderItem(item - 1, item_name_raspr)
            SAPR.show_kernel(self)
    #####################################
    def show_kernel(self):
        self.Preprocessor_idea.label_3.setText(f"{self.kernels}")
        self.Preprocessor_idea.label_sosr.setText(f"{self.sosr}")
        self.Preprocessor_idea.label_raspr.setText(f"{self.raspr}")

    def add_kernel(self):
        count_kernels = self.Preprocessor_idea.table_kernel.rowCount()
        count_sosr = self.Preprocessor_idea.table_sosr.rowCount()
        count_raspr = self.Preprocessor_idea.table_raspr.rowCount()
        self.Preprocessor_idea.table_kernel.insertRow(count_kernels)
        new_item_name_kernel = QTableWidgetItem()
        new_item_name_kernel.setText(f'{count_kernels + 1}:')
        self.Preprocessor_idea.table_kernel.setVerticalHeaderItem(count_kernels, new_item_name_kernel)
        self.kernels+=1

        self.Preprocessor_idea.table_sosr.insertRow(count_sosr)
        new_item_name_sosr = QTableWidgetItem()
        new_item_name_sosr.setText(f'{count_sosr + 1}:')
        self.Preprocessor_idea.table_sosr.setVerticalHeaderItem(count_sosr, new_item_name_sosr)
        self.sosr+=1

        self.Preprocessor_idea.table_raspr.insertRow(count_raspr)
        new_item_name_raspr = QTableWidgetItem()
        new_item_name_raspr.setText(f'{count_raspr + 1}:')
        self.Preprocessor_idea.table_raspr.setVerticalHeaderItem(count_raspr, new_item_name_raspr)
        self.raspr+=1

        SAPR.show_kernel(self)


    def delete_kernel(self):
        # count_kernels = self.Preprocessor_idea.table_kernel.rowCount()
        # count_sosr = self.Preprocessor_idea.table_sosr.rowCount()
        # count_raspr = self.Preprocessor_idea.table_raspr.rowCount()

        kernel_for_del = self.Preprocessor_idea.table_kernel.currentRow()
        print(kernel_for_del)
        if kernel_for_del+1 > -1 and self.kernels != 1:
            self.Preprocessor_idea.table_kernel.removeRow(kernel_for_del)
            self.Preprocessor_idea.table_kernel.selectionModel().clearCurrentIndex()
            self.kernels-=1

            self.Preprocessor_idea.table_sosr.removeRow(kernel_for_del+1)
            self.Preprocessor_idea.table_sosr.selectionModel().clearCurrentIndex()
            self.sosr -= 1

            self.Preprocessor_idea.table_raspr.removeRow(kernel_for_del)
            self.Preprocessor_idea.table_raspr.selectionModel().clearCurrentIndex()
            self.raspr -= 1

            for item in range(1, self.kernels+1):
                item_name_kernel = QTableWidgetItem()
                item_name_kernel.setText(f'{item}:')
                self.Preprocessor_idea.table_kernel.setVerticalHeaderItem(item-1, item_name_kernel)
                #self.Preprocessor_idea.table_sosr.insertRow(count_sosr)

            for item in range(1, self.sosr+1):
                item_name_sosr = QTableWidgetItem()
                item_name_sosr.setText(f'{item}:')
                self.Preprocessor_idea.table_sosr.setVerticalHeaderItem(item - 1, item_name_sosr)

            for item in range(1, self.raspr+1):
                item_name_raspr = QTableWidgetItem()
                item_name_raspr.setText(f'{item}:')
                self.Preprocessor_idea.table_raspr.setVerticalHeaderItem(item - 1, item_name_raspr)

            SAPR.show_kernel(self)

    def table(self):
        pass
    def OK_kernel(self):
        self.list_of_length = []
        self.list_of_square = []
        self.list_of_modul = []
        self.list_of_voltage = []
        for row in range (0, self.kernels):
            length = self.Preprocessor_idea.table_kernel.item(row, 0).text()
            try:
                length = float(length)
            except ValueError:
                self.error_4_window = QtWidgets.QDialog()
                self.error_4_idea = Error_4_Dialog()
                self.error_4_idea.setupUi(self.error_4_window)
                self.error_4_window.show()
                self.Preprocessor_idea.table_kernel.item(row, 0).setText(str(1))
                length = self.Preprocessor_idea.table_kernel.item(row, 0).text()
            self.list_of_length.append(length)
            #print (self.list_of_length)

            square = self.Preprocessor_idea.table_kernel.item(row, 1).text()
            square = float(square)
            self.Preprocessor_idea.table_kernel.item(row, 1).setText(str(1))
            self.list_of_square.append(square)
            #print (self.list_of_square)

            modul = self.Preprocessor_idea.table_kernel.item(row, 2).text()
            modul = float(modul)
            self.Preprocessor_idea.table_kernel.item(row, 2).setText(str(1))
            self.list_of_modul.append(modul)
            #print(self.list_of_modul)

            voltage = self.Preprocessor_idea.table_kernel.item(row, 3).text()
            voltage = float(voltage)
            self.Preprocessor_idea.table_kernel.item(row, 3).setText(str(1))
            self.list_of_voltage.append(voltage)
            #print(self.list_of_voltage)

        self.list_of_sosr = []
        for row in range (0, self.sosr+1):
            sosr = float(self.Preprocessor_idea.table_sosr.item(row, 0).text())
            self.Preprocessor_window.table_sosr.item(row, 0).setText('1')
            self.list_of_sosr.append(sosr)
            print(self.list_of_sosr)

        self.list_of_raspr = []
        for row in range(0, self.raspr):
            raspr = self.Preprocessor_idea.table_raspr.item(row, 0).text()
            raspr = float(raspr)
            self.Preprocessor_idea.table_raspr.item(row, 0).setText(str(1))
            self.list_of_raspr.append(raspr)
            #print(self.list_of_raspr)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SAPR()
    window.show()

    sys.exit(app.exec())