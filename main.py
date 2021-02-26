# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 400)
        MainWindow.setStyleSheet("background-color: rgb(37, 37, 37);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 371, 90))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")
        self.btn_division_without_remainder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_division_without_remainder.setGeometry(QtCore.QRect(10, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_division_without_remainder.setFont(font)
        self.btn_division_without_remainder.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_division_without_remainder.setObjectName("btn_division_without_remainder")
        self.btn_CE = QtWidgets.QPushButton(self.centralwidget)
        self.btn_CE.setGeometry(QtCore.QRect(100, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_CE.setFont(font)
        self.btn_CE.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_CE.setObjectName("btn_CE")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(190, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_seven = QtWidgets.QPushButton(self.centralwidget)
        self.btn_seven.setGeometry(QtCore.QRect(10, 160, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_seven.setFont(font)
        self.btn_seven.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_seven.setObjectName("btn_seven")
        self.btn_eight = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eight.setGeometry(QtCore.QRect(100, 160, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_eight.setFont(font)
        self.btn_eight.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_eight.setObjectName("btn_eight")
        self.btn_nine = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nine.setGeometry(QtCore.QRect(190, 160, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_nine.setFont(font)
        self.btn_nine.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_nine.setObjectName("btn_nine")
        self.btn_four = QtWidgets.QPushButton(self.centralwidget)
        self.btn_four.setGeometry(QtCore.QRect(10, 220, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_four.setFont(font)
        self.btn_four.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_four.setObjectName("btn_four")
        self.btn_five = QtWidgets.QPushButton(self.centralwidget)
        self.btn_five.setGeometry(QtCore.QRect(100, 220, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_five.setFont(font)
        self.btn_five.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_five.setObjectName("btn_five")
        self.btn_six = QtWidgets.QPushButton(self.centralwidget)
        self.btn_six.setGeometry(QtCore.QRect(190, 220, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_six.setFont(font)
        self.btn_six.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_six.setObjectName("btn_six")
        self.btn_one = QtWidgets.QPushButton(self.centralwidget)
        self.btn_one.setGeometry(QtCore.QRect(10, 280, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_one.setFont(font)
        self.btn_one.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_one.setObjectName("btn_one")
        self.btn_two = QtWidgets.QPushButton(self.centralwidget)
        self.btn_two.setGeometry(QtCore.QRect(100, 280, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_two.setFont(font)
        self.btn_two.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_two.setObjectName("btn_two")
        self.btn_three = QtWidgets.QPushButton(self.centralwidget)
        self.btn_three.setGeometry(QtCore.QRect(190, 280, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_three.setFont(font)
        self.btn_three.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_three.setObjectName("btn_three")
        self.btn_exponentiation = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exponentiation.setGeometry(QtCore.QRect(10, 340, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_exponentiation.setFont(font)
        self.btn_exponentiation.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_exponentiation.setObjectName("btn_exponentiation")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(100, 340, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(190, 340, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(7, 7, 6);\n"
"color: rgb(255, 255, 255);")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(280, 340, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(62, 22, 86);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_addition = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addition.setGeometry(QtCore.QRect(280, 280, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_addition.setFont(font)
        self.btn_addition.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_addition.setObjectName("btn_addition")
        self.btn_subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtraction.setGeometry(QtCore.QRect(280, 220, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_subtraction.setFont(font)
        self.btn_subtraction.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_subtraction.setObjectName("btn_subtraction")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(280, 160, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(280, 100, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(19)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.btn_divide.setObjectName("btn_divide")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.is_equal = False

        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_one.clicked.connect(lambda: self.write_number(self.btn_one.text()))
        self.btn_two.clicked.connect(lambda: self.write_number(self.btn_two.text()))
        self.btn_three.clicked.connect(lambda: self.write_number(self.btn_three.text()))
        self.btn_four.clicked.connect(lambda: self.write_number(self.btn_four.text()))
        self.btn_five.clicked.connect(lambda: self.write_number(self.btn_five.text()))
        self.btn_six.clicked.connect(lambda: self.write_number(self.btn_six.text()))
        self.btn_seven.clicked.connect(lambda: self.write_number(self.btn_seven.text()))
        self.btn_eight.clicked.connect(lambda: self.write_number(self.btn_eight.text()))
        self.btn_nine.clicked.connect(lambda: self.write_number(self.btn_nine.text()))
        self.btn_addition.clicked.connect(lambda: self.write_number(self.btn_addition.text()))
        self.btn_subtraction.clicked.connect(lambda: self.write_number(self.btn_subtraction.text()))
        self.btn_multiply.clicked.connect(lambda: self.write_number(self.btn_multiply.text()))
        self.btn_divide.clicked.connect(lambda: self.write_number(self.btn_divide.text()))
        self.btn_division_without_remainder.clicked.connect(lambda: self.write_number(self.btn_division_without_remainder.text()))
        self.btn_dot.clicked.connect(lambda: self.write_number(self.btn_dot.text()))
        self.btn_exponentiation.clicked.connect(lambda: self.write_number(self.btn_exponentiation.text()))

        self.btn_equal.clicked.connect(self.results)
        self.btn_CE.clicked.connect(self.clean)
        self.btn_delete.clicked.connect(self.delete)


    def write_number(self, number):
        if self.label_result.text() == '0' or self.is_equal == True:
            self.is_equal = False
            self.label_result.setText(number)
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        result = eval(self.label_result.text())
        self.label_result.setText(str(result))
        self.is_equal = True

    def clean(self):
        self.label_result.setText('0')

    def delete(self):
        temporary_result = self.label_result.text()
        self.label_result.setText(temporary_result[:-1])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_division_without_remainder.setText(_translate("MainWindow", "//"))
        self.btn_CE.setText(_translate("MainWindow", "CE"))
        self.btn_delete.setText(_translate("MainWindow", "delete"))
        self.btn_seven.setText(_translate("MainWindow", "7"))
        self.btn_eight.setText(_translate("MainWindow", "8"))
        self.btn_nine.setText(_translate("MainWindow", "9"))
        self.btn_four.setText(_translate("MainWindow", "4"))
        self.btn_five.setText(_translate("MainWindow", "5"))
        self.btn_six.setText(_translate("MainWindow", "6"))
        self.btn_one.setText(_translate("MainWindow", "1"))
        self.btn_two.setText(_translate("MainWindow", "2"))
        self.btn_three.setText(_translate("MainWindow", "3"))
        self.btn_exponentiation.setText(_translate("MainWindow", "**"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_addition.setText(_translate("MainWindow", "+"))
        self.btn_subtraction.setText(_translate("MainWindow", "-"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_divide.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
