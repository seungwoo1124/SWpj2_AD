# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordBook4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from word import Word

import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.word = Word()
        self.s = self.word.readWords("suneung.txt")
        self.sitem = list(self.s.items())
        self.sidx = 0

        self.t = self.word.readWords("toeic.txt")
        self.titem = list(self.t.items())
        self.tidx = 0

        self.g = self.word.readWords("gongmuwon.txt")
        self.gitem = list(self.g.items())
        self.gidx = 0

        self.wrongword = {}


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 914)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(191,150,208);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 10))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(40, 1, 40, 1)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 10))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_5.setSizeIncrement(QtCore.QSize(10, 30))
        self.pushButton_5.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 10))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_4.setSizeIncrement(QtCore.QSize(10, 30))
        self.pushButton_4.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 20, 10, 20)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 716, 450))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 691, 431))
        self.textEdit_2.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_2.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.toolButton_2.setCheckable(False)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.toolButton_2)
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_2.addWidget(self.toolButton_3)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.toolButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(249, 16777215))
        self.pushButton.setStyleSheet("background-color: rgb(220, 173, 240);\n"
"\n"
"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(249, 16777215))
        self.pushButton_2.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(249, 16777215))
        self.pushButton_3.setStyleSheet("background-color: rgb(220, 173, 240);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 270))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 268))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 761, 251))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "All-pass wordbook & test"))
        self.pushButton_5.setText(_translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "수능"))
        self.pushButton_4.setText(_translate("MainWindow", "Dictionary"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.toolButton_2.setText(_translate("MainWindow", "1"))
        self.toolButton_3.setText(_translate("MainWindow", "2"))
        self.toolButton.setText(_translate("MainWindow", "3"))
        self.pushButton.setText(_translate("MainWindow", "수능"))
        self.pushButton_2.setText(_translate("MainWindow", "토익"))
        self.pushButton_3.setText(_translate("MainWindow", "공무원"))

        self.textEdit.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)

        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked)
        self.pushButton_3.clicked.connect(self.buttonClicked)
        self.pushButton_4.clicked.connect(self.buttonClicked)
        self.pushButton_5.clicked.connect(self.buttonClicked)
        self.toolButton.clicked.connect(self.testButton)
        self.toolButton_2.clicked.connect(self.testButton)
        self.toolButton_3.clicked.connect(self.testButton)


    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == "수능":
            self.label_2.setText("수능")
        elif key == "토익":
            self.label_2.setText("토익")
        elif key == "공무원":
            self.label_2.setText("공무원")
        elif key == "Dictionary":
            if self.label_2.text() == "수능":
                self.s = self.word.readWords("suneung.txt")
                self.textEdit_2.setText("")
                for key, value in self.s.items():
                    self.textEdit_2.setText(self.textEdit_2.toPlainText() + key + "\t" + value + "\n")
                self.toolButton.setText("3")
                self.toolButton_2.setText("2")
                self.toolButton_3.setText("1")


            elif self.label_2.text() == "토익":
                self.t = self.word.readWords("toeic.txt")
                self.textEdit_2.setText("")
                for key, value in self.t.items():
                    self.textEdit_2.setText(self.textEdit_2.toPlainText() + key + "\t" + value + "\n")
                self.toolButton.setText("3")
                self.toolButton_2.setText("2")
                self.toolButton_3.setText("1")
            else:
                self.g = self.word.readWords("gongmuwon.txt")
                self.textEdit_2.setText("")
                for key, value in self.g.items():
                    self.textEdit_2.setText(self.textEdit_2.toPlainText() + key + "\t" + value + "\n")
                self.toolButton.setText("3")
                self.toolButton_2.setText("2")
                self.toolButton_3.setText("1")

        elif key == "Test":
            if self.label_2.text() == "수능":
                self.s = self.word.readWords("suneung.txt")
                self.sitem = list(self.s.items())
                print(self.sitem)
                self.sidx = 0
                self.wrongword = {}

                self.textEdit_2.setText(self.sitem[self.sidx][0])

                a = random.randrange(1, 4)
                b = random.randrange(1, len(self.sitem))
                c = random.randrange(1, len(self.sitem))

                if a == 1:
                    self.toolButton_2.setText(self.sitem[self.sidx][1])
                    self.toolButton.setText(self.sitem[b][1])
                    self.toolButton_3.setText(self.sitem[c][1])

                elif a == 2:
                    self.toolButton_3.setText(self.sitem[self.sidx][1])
                    self.toolButton.setText(self.sitem[b][1])
                    self.toolButton_2.setText(self.sitem[c][1])
                else:
                    self.toolButton.setText(self.sitem[self.sidx][1])
                    self.toolButton_2.setText(self.sitem[b][1])
                    self.toolButton_3.setText(self.sitem[c][1])


            elif self.label_2.text() == "공무원":
                self.g = self.word.readWords("gongmuwon.txt")
                self.gitem = list(self.g.items())
                print(self.gitem)
                self.gidx = 0
                self.wrongword = {}

                self.textEdit_2.setText(self.gitem[self.gidx][0])

                a = random.randrange(1, 4)
                b = random.randrange(1, len(self.gitem))
                c = random.randrange(1, len(self.gitem))

                if a == 1:
                    self.toolButton_2.setText(self.gitem[self.gidx][1])
                    self.toolButton.setText(self.gitem[b][1])
                    self.toolButton_3.setText(self.gitem[c][1])

                elif a == 2:
                    self.toolButton_3.setText(self.gitem[self.gidx][1])
                    self.toolButton.setText(self.gitem[b][1])
                    self.toolButton_2.setText(self.gitem[c][1])
                else:
                    self.toolButton.setText(self.gitem[self.gidx][1])
                    self.toolButton_2.setText(self.gitem[b][1])
                    self.toolButton_3.setText(self.gitem[c][1])
            else:
                self.t = self.word.readWords("toeic.txt")
                self.titem = list(self.t.items())
                print(self.titem)
                self.tidx = 0
                self.wrongword = {}

                self.textEdit_2.setText(self.titem[self.tidx][0])

                a = random.randrange(1, 4)
                b = random.randrange(1, len(self.titem))
                c = random.randrange(1, len(self.titem))

                if a == 1:
                    self.toolButton_2.setText(self.titem[self.sidx][1])
                    self.toolButton.setText(self.titem[b][1])
                    self.toolButton_3.setText(self.titem[c][1])

                elif a == 2:
                    self.toolButton_3.setText(self.titem[self.sidx][1])
                    self.toolButton.setText(self.titem[b][1])
                    self.toolButton_2.setText(self.titem[c][1])
                else:
                    self.toolButton.setText(self.titem[self.sidx][1])
                    self.toolButton_2.setText(self.titem[b][1])
                    self.toolButton_3.setText(self.titem[c][1])

    def testButton(self):
        button = self.sender()
        key = button.text()
        if self.toolButton.text() == '3' or self.toolButton_2.text() == '1' or self.toolButton_3.text() == '2':
            return
        if self.label_2.text() == "수능":
            if self.s[self.textEdit_2.toPlainText()] != key:
                self.wrongword[self.textEdit_2.toPlainText()] = key

            if self.sidx == len(self.sitem) - 1:
                self.textEdit_2.setText("테스트가 끝났습니다.")
                self.word.writeWords('wrong.txt', self.wrongword)
                f = self.word.readWords('wrong.txt')
                for key, value in f.items():
                    self.textEdit.append(key + "\t\t" + value)
                return

            self.sidx += 1

            print(self.sidx)

            self.textEdit_2.setText(self.sitem[self.sidx][0])

            a = random.randrange(1, 4)
            b = random.randrange(1, len(self.sitem))
            c = random.randrange(1, len(self.sitem))

            if a == 1:
                self.toolButton_2.setText(self.sitem[self.sidx][1])
                self.toolButton.setText(self.sitem[b][1])
                self.toolButton_3.setText(self.sitem[c][1])

            elif a == 2:
                self.toolButton_3.setText(self.sitem[self.sidx][1])
                self.toolButton.setText(self.sitem[b][1])
                self.toolButton_2.setText(self.sitem[c][1])
            else:
                self.toolButton.setText(self.sitem[self.sidx][1])
                self.toolButton_2.setText(self.sitem[b][1])
                self.toolButton_3.setText(self.sitem[c][1])


        elif self.label_2.text() == "토익":

            if self.t[self.textEdit_2.toPlainText()] != key:
                self.wrongword[self.textEdit_2.toPlainText()] = key

            if self.tidx == len(self.titem) - 1:
                self.textEdit_2.setText("테스트가 끝났습니다.")
                self.word.writeWords('wrong.txt', self.wrongword)
                f = self.word.readWords('wrong.txt')
                for key, value in f.items():
                    self.textEdit.append(key + "\t\t" + value)
                return

            self.tidx += 1

            print(self.tidx)

            self.textEdit_2.setText(self.titem[self.tidx][0])

            a = random.randrange(1, 4)
            b = random.randrange(1, len(self.titem))
            c = random.randrange(1, len(self.titem))

            if a == 1:
                self.toolButton_2.setText(self.titem[self.tidx][1])
                self.toolButton.setText(self.titem[b][1])
                self.toolButton_3.setText(self.titem[c][1])

            elif a == 2:
                self.toolButton_3.setText(self.titem[self.tidx][1])
                self.toolButton.setText(self.titem[b][1])
                self.toolButton_2.setText(self.titem[c][1])
            else:
                self.toolButton.setText(self.titem[self.tidx][1])
                self.toolButton_2.setText(self.titem[b][1])
                self.toolButton_3.setText(self.titem[c][1])


        else:
            if self.g[self.textEdit_2.toPlainText()] != key:
                self.wrongword[self.textEdit_2.toPlainText()] = key

            if self.gidx == len(self.gitem) - 1:
                self.textEdit_2.setText("테스트가 끝났습니다.")
                self.word.writeWords('wrong.txt', self.wrongword)
                f = self.word.readWords('wrong.txt')
                for key, value in f.items():
                    self.textEdit.append(key + "\t\t" + value)
                return

            self.gidx += 1

            print(self.gidx)

            self.textEdit_2.setText(self.gitem[self.gidx][0])

            a = random.randrange(1, 4)
            b = random.randrange(1, len(self.gitem))
            c = random.randrange(1, len(self.gitem))

            if a == 1:
                self.toolButton_2.setText(self.gitem[self.gidx][1])
                self.toolButton.setText(self.gitem[b][1])
                self.toolButton_3.setText(self.gitem[c][1])

            elif a == 2:
                self.toolButton_3.setText(self.gitem[self.gidx][1])
                self.toolButton.setText(self.gitem[b][1])
                self.toolButton_2.setText(self.gitem[c][1])
            else:
                self.toolButton.setText(self.gitem[self.gidx][1])
                self.toolButton_2.setText(self.gitem[b][1])
                self.toolButton_3.setText(self.gitem[c][1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

