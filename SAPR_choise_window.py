# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SAPR_choise_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(497, 444)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spred:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(2, 23, 44, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(120, 183, 139, 255));\n"
"font-family: Noto Serif;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 45)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(80, -1, 80, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.preprocessor_btn = QPushButton(self.frame_2)
        self.preprocessor_btn.setObjectName(u"preprocessor_btn")
        self.preprocessor_btn.setMaximumSize(QSize(1000, 16777215))
        self.preprocessor_btn.setStyleSheet(u"QPushButton {\n"
"font-size: 12pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(7, 58, 82, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(7, 58, 82, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.preprocessor_btn)

        self.processor_btn = QPushButton(self.frame_2)
        self.processor_btn.setObjectName(u"processor_btn")
        self.processor_btn.setStyleSheet(u"QPushButton {\n"
"font-size: 12pt;\n"
"color: white;\n"
"background-color: rgba(139, 0, 0, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(139, 0, 0, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(139, 0, 0, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.processor_btn)

        self.postprocessor_btn = QPushButton(self.frame_2)
        self.postprocessor_btn.setObjectName(u"postprocessor_btn")
        self.postprocessor_btn.setStyleSheet(u"QPushButton {\n"
"font-size: 12pt;\n"
"color: white;\n"
"background-color: rgba(139, 0, 0, 255); \n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(139, 0, 0, 170);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(139, 0, 0, 200);\n"
"border-color: white;\n"
"border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.postprocessor_btn)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 70)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044d\u0442\u0430\u043f", None))
        self.preprocessor_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.processor_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.postprocessor_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
    # retranslateUi

