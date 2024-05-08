# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signals.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_object(object):
    def setupUi(self, object):
        if not object.objectName():
            object.setObjectName(u"object")
        object.resize(385, 163)
        self.verticalLayout_2 = QVBoxLayout(object)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditInput = QLineEdit(object)
        self.lineEditInput.setObjectName(u"lineEditInput")

        self.horizontalLayout.addWidget(self.lineEditInput)

        self.lineEditMirror = QLineEdit(object)
        self.lineEditMirror.setObjectName(u"lineEditMirror")

        self.horizontalLayout.addWidget(self.lineEditMirror)

        self.lineEdit_3 = QLineEdit(object)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.radioButton = QRadioButton(object)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.pushButtonMirror = QPushButton(object)
        self.pushButtonMirror.setObjectName(u"pushButtonMirror")

        self.verticalLayout.addWidget(self.pushButtonMirror)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(object)

        QMetaObject.connectSlotsByName(object)
    # setupUi

    def retranslateUi(self, object):
        object.setWindowTitle(QCoreApplication.translate("object", u"Form", None))
        self.lineEditInput.setText("")
        self.radioButton.setText(QCoreApplication.translate("object", u"RadioButton", None))
        self.pushButtonMirror.setText(QCoreApplication.translate("object", u"\u041d\u0430\u0436\u043c\u0438 \u043c\u0435\u043d\u044f", None))
    # retranslateUi

