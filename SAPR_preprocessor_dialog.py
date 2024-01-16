# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SAPR_preprocessor_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
#import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(753, 404)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spred:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(2, 23, 44, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(120, 183, 139, 255));\n"
"font-family: Noto Serif;")
        self.gridLayout_16 = QGridLayout(Dialog)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line, 1, 0, 1, 3)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_2, 3, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background-color: none;\n"
"border: 0px;")

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background-color: none;\n"
"border: 0px;")

        self.gridLayout_3.addWidget(self.checkBox, 0, 1, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_3)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frame_5)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_15.addWidget(self.line_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_12)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"font-size: 10pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82); \n"
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

        self.horizontalLayout_13.addWidget(self.pushButton)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)


        self.gridLayout_9.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setMaximumSize(QSize(1250, 16777215))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"font-size: 10pt;\n"
"color: white;\n"
"background-color: rgba(7, 58, 82); \n"
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

        self.horizontalLayout_14.addWidget(self.pushButton_2)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)


        self.verticalLayout.addLayout(self.horizontalLayout_14)


        self.gridLayout_11.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)


        self.gridLayout_14.addLayout(self.horizontalLayout_15, 5, 0, 1, 3)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_3, 4, 0, 1, 3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.textEdit = QTextEdit(self.frame_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(41, 31))
        self.textEdit.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_3, 3, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_2, 0, 0, 1, 2)


        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0437\u0430\u0434\u0435\u043b\u043a\u0438:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0441\u043b\u0435\u0432\u0430", None))
        self.checkBox_2.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0441\u043f\u0440\u0430\u0432\u0430", None))
        self.checkBox.setText("")
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c</p><p>\u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c?", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c</p><p>\u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f?</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b?", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0441\u0442\u0435\u0440\u0436\u043d\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
    # retranslateUi

