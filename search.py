from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 106)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 30, 261, 25))
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 17))
        self.label.setObjectName("label")
        self.input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_btn.setGeometry(QtCore.QRect(270, 30, 89, 25))
        self.input_btn.setObjectName("input_btn")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 70, 351, 21))
        self.result.setText("")
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "поиск"))
        self.label.setText(_translate("MainWindow", "поиск по reg_num, dev_id:"))
        self.input_btn.setText(_translate("MainWindow", "найти"))
    
    def add_functions(self):
        self.input_btn.clicked.connect(lambda: self.write_number(self.input.text()))

    def write_number(self, number):
        print(' - input: ', number)
        with open('neighbors.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                all_result_line = line.split()
                tachka = all_result_line[0:3]
                if number in str(tachka):
                    print(' - result: ', tachka)
                    self.result.setText(tachka[0] + ' ' + tachka[1] + ' ' + tachka[2])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
