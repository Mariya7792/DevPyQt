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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.DeadlineLabel = QLabel(self.centralwidget)
        self.DeadlineLabel.setObjectName(u"DeadlineLabel")
        self.DeadlineLabel.setTextFormat(Qt.TextFormat.MarkdownText)
        self.DeadlineLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.DeadlineLabel.setIndent(0)

        self.horizontalLayout_4.addWidget(self.DeadlineLabel)

        self.DeadlineData = QDateEdit(self.centralwidget)
        self.DeadlineData.setObjectName(u"DeadlineData")

        self.horizontalLayout_4.addWidget(self.DeadlineData)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.NotesText = QTextEdit(self.centralwidget)
        self.NotesText.setObjectName(u"NotesText")

        self.verticalLayout_4.addWidget(self.NotesText)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DeleteButton = QPushButton(self.centralwidget)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.horizontalLayout.addWidget(self.DeleteButton)

        self.ChangeButton = QPushButton(self.centralwidget)
        self.ChangeButton.setObjectName(u"ChangeButton")

        self.horizontalLayout.addWidget(self.ChangeButton)

        self.AddButton = QPushButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")

        self.horizontalLayout.addWidget(self.AddButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.NotesStorage = QTextEdit(self.centralwidget)
        self.NotesStorage.setObjectName(u"NotesStorage")

        self.horizontalLayout_2.addWidget(self.NotesStorage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d:", None))
        self.DeleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.ChangeButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

