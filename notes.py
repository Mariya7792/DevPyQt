# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(671, 343)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.TodayLabel = QLabel(self.centralwidget)
        self.TodayLabel.setObjectName(u"TodayLabel")
        self.TodayLabel.setTextFormat(Qt.TextFormat.MarkdownText)
        self.TodayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TodayLabel.setIndent(0)

        self.horizontalLayout_3.addWidget(self.TodayLabel)

        self.CurrentDate = QDateEdit(self.centralwidget)
        self.CurrentDate.setObjectName(u"CurrentDate")

        self.horizontalLayout_3.addWidget(self.CurrentDate)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.DeadlineLabel = QLabel(self.centralwidget)
        self.DeadlineLabel.setObjectName(u"DeadlineLabel")
        self.DeadlineLabel.setTextFormat(Qt.TextFormat.MarkdownText)
        self.DeadlineLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DeadlineLabel.setIndent(0)

        self.horizontalLayout_2.addWidget(self.DeadlineLabel)

        self.DeadlineData = QDateEdit(self.centralwidget)
        self.DeadlineData.setObjectName(u"DeadlineData")

        self.horizontalLayout_2.addWidget(self.DeadlineData)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.NotesText = QTextEdit(self.centralwidget)
        self.NotesText.setObjectName(u"NotesText")

        self.verticalLayout_3.addWidget(self.NotesText)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AddButton = QPushButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")

        self.horizontalLayout.addWidget(self.AddButton)

        self.SaveButton = QPushButton(self.centralwidget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.DeleteButton = QPushButton(self.centralwidget)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.horizontalLayout.addWidget(self.DeleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.NotesStorage = QTextEdit(self.centralwidget)
        self.NotesStorage.setObjectName(u"NotesStorage")

        self.horizontalLayout_4.addWidget(self.NotesStorage)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TodayLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.DeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d:", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

