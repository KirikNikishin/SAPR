# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SAPR_preprocessor.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 803)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spred:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(2, 23, 44, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(120, 183, 139, 255));\n"
"font-family: Noto Serif;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: white;")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 611, 491))
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.button_plus_kernel = QPushButton(self.widget)
        self.button_plus_kernel.setObjectName(u"button_plus_kernel")
        self.button_plus_kernel.setMinimumSize(QSize(32, 28))
        self.button_plus_kernel.setMaximumSize(QSize(32, 28))
        self.button_plus_kernel.setStyleSheet(u"QPushButton{\n"
"font-size: 14pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_plus_kernel)

        self.button_minus_kernel = QPushButton(self.widget)
        self.button_minus_kernel.setObjectName(u"button_minus_kernel")
        self.button_minus_kernel.setMinimumSize(QSize(32, 28))
        self.button_minus_kernel.setMaximumSize(QSize(32, 28))
        self.button_minus_kernel.setStyleSheet(u"QPushButton{\n"
"font-size: 14pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_minus_kernel)

        self.button_ok_kernel = QPushButton(self.widget)
        self.button_ok_kernel.setObjectName(u"button_ok_kernel")
        self.button_ok_kernel.setMinimumSize(QSize(32, 28))
        self.button_ok_kernel.setMaximumSize(QSize(32, 28))
        self.button_ok_kernel.setStyleSheet(u"QPushButton{\n"
"font-size: 14pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_ok_kernel)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.table_kernel = QTableWidget(self.widget)
        if (self.table_kernel.columnCount() < 4):
            self.table_kernel.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_kernel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_kernel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_kernel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_kernel.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_kernel.rowCount() < 1):
            self.table_kernel.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_kernel.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_kernel.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_kernel.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_kernel.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_kernel.setItem(0, 3, __qtablewidgetitem8)
        self.table_kernel.setObjectName(u"table_kernel")
        self.table_kernel.setStyleSheet(u"QHeaderView{\n"
"font-size: 14pt; \n"
"background-color: rgba(255,255,255,0);\n"
"color: green;\n"
"border: 0px;\n"
"}\n"
"QTableWidget{\n"
"background-color: rgba(255,255,255,100);\n"
"alternate-background-color: #606060;\n"
"selection-background-color: #282828;\n"
"font-size: 14pt;\n"
"border: 0px;\n"
"}")

        self.gridLayout_7.addWidget(self.table_kernel, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: white;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setMaximumSize(QSize(400, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 50))
        self.label_18.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(202, 16777215))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_7)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 201, 441))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_19)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.table_sosr = QTableWidget(self.layoutWidget)
        if (self.table_sosr.columnCount() < 1):
            self.table_sosr.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_sosr.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        if (self.table_sosr.rowCount() < 2):
            self.table_sosr.setRowCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_sosr.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_sosr.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_sosr.setItem(0, 0, __qtablewidgetitem12)
        self.table_sosr.setObjectName(u"table_sosr")
        self.table_sosr.setStyleSheet(u"QHeaderView{\n"
"font-size: 14pt; \n"
"background-color: rgba(255,255,255,0);\n"
"color: green;\n"
"border: 0px;\n"
"}\n"
"QTableWidget{\n"
"background-color: rgba(255,255,255,0);\n"
"alternate-background-color: #606060;\n"
"selection-background-color: #282828;\n"
"font-size: 14pt;\n"
"border: 0px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.table_sosr)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.line_10 = QFrame(self.frame_6)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"background-color: white;")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_10)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(202, 16777215))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_8)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 261, 441))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 50))
        self.label_20.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_20)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.table_raspr = QTableWidget(self.layoutWidget1)
        if (self.table_raspr.columnCount() < 1):
            self.table_raspr.setColumnCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_raspr.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        if (self.table_raspr.rowCount() < 1):
            self.table_raspr.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_raspr.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_raspr.setItem(0, 0, __qtablewidgetitem15)
        self.table_raspr.setObjectName(u"table_raspr")
        self.table_raspr.setEnabled(True)
        self.table_raspr.setStyleSheet(u"QHeaderView{\n"
"font-size: 14pt; \n"
"background-color: rgba(255,255,255,0);\n"
"color: green;\n"
"border: 0px;\n"
"}\n"
"QTableWidget{\n"
"background-color: rgba(255,255,255, 0);\n"
"alternate-background-color: #606060;\n"
"selection-background-color: #282828;\n"
"font-size: 14pt;\n"
"border: 0px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.table_raspr)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: white;")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1000, 0))
        self.frame_2.setMaximumSize(QSize(4000, 33))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_6)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_sosr = QLabel(self.frame_2)
        self.label_sosr.setObjectName(u"label_sosr")
        self.label_sosr.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_sosr)

        self.line_7 = QFrame(self.frame_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_raspr = QLabel(self.frame_2)
        self.label_raspr.setObjectName(u"label_raspr")
        self.label_raspr.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_raspr)

        self.line_8 = QFrame(self.frame_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.label_zadelka_l = QLabel(self.frame_2)
        self.label_zadelka_l.setObjectName(u"label_zadelka_l")
        self.label_zadelka_l.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_zadelka_l)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_zadelka_r = QLabel(self.frame_2)
        self.label_zadelka_r.setObjectName(u"label_zadelka_r")
        self.label_zadelka_r.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_zadelka_r)

        self.line_9 = QFrame(self.frame_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_change = QPushButton(self.frame_2)
        self.button_change.setObjectName(u"button_change")
        self.button_change.setStyleSheet(u"QPushButton{\n"
"font-size: 10pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.horizontalLayout.addWidget(self.button_change)

        self.button_save = QPushButton(self.frame_2)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setStyleSheet(u"QPushButton {\n"
"font-size: 10pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.horizontalLayout.addWidget(self.button_save)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setMaximumSize(QSize(16777215, 225))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_4, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0440\u0436\u043d\u0438:", None))
        self.button_plus_kernel.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_minus_kernel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_ok_kernel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a", None))
        ___qtablewidgetitem = self.table_kernel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"L", None));
        ___qtablewidgetitem1 = self.table_kernel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"A", None));
        ___qtablewidgetitem2 = self.table_kernel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"E", None));
        ___qtablewidgetitem3 = self.table_kernel.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sp", None));
        ___qtablewidgetitem4 = self.table_kernel.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1:", None));

        __sortingEnabled = self.table_kernel.isSortingEnabled()
        self.table_kernel.setSortingEnabled(False)
        self.table_kernel.setSortingEnabled(__sortingEnabled)

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0440\u0435\u0434\u043e\u0442\u043e\u0447\u0435\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem5 = self.table_sosr.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fx", None));
        ___qtablewidgetitem6 = self.table_sosr.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1:", None));
        ___qtablewidgetitem7 = self.table_sosr.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2:", None));

        __sortingEnabled1 = self.table_sosr.isSortingEnabled()
        self.table_sosr.setSortingEnabled(False)
        self.table_sosr.setSortingEnabled(__sortingEnabled1)

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem8 = self.table_raspr.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"qx", None));
        ___qtablewidgetitem9 = self.table_raspr.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1:", None));

        __sortingEnabled2 = self.table_raspr.isSortingEnabled()
        self.table_raspr.setSortingEnabled(False)
        self.table_raspr.setSortingEnabled(__sortingEnabled2)

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043e:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0435\u0440\u0436\u043d\u0435\u0439:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0441\u0440\u0435\u0434\u043e\u0442\u043e\u0447\u0435\u043d\u043d\u044b\u0445 \u043d\u0430\u0433\u0440\u0443\u0437\u043e\u043a:", None))
        self.label_sosr.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0445 \u043d\u0430\u0433\u0440\u0443\u0437\u043e\u043a:", None))
        self.label_raspr.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u043b\u043a\u0438:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041b:", None))
        self.label_zadelka_l.setText(QCoreApplication.translate("MainWindow", u"\u0435\u0441\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041f:", None))
        self.label_zadelka_r.setText(QCoreApplication.translate("MainWindow", u"\u0435\u0441\u0442\u044c", None))
        self.button_change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

