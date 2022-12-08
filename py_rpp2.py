# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rpp2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 352)
        MainWindow.setStyleSheet("color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Ravning = QtWidgets.QStackedWidget(self.centralwidget)
        self.Ravning.setGeometry(QtCore.QRect(10, 10, 491, 281))
        self.Ravning.setObjectName("Ravning")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.text_chislo_2 = QtWidgets.QLabel(self.Home)
        self.text_chislo_2.setGeometry(QtCore.QRect(70, 70, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_chislo_2.setFont(font)
        self.text_chislo_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.text_chislo_2.setObjectName("text_chislo_2")
        self.text_chislo_3 = QtWidgets.QLabel(self.Home)
        self.text_chislo_3.setGeometry(QtCore.QRect(60, 140, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_chislo_3.setFont(font)
        self.text_chislo_3.setObjectName("text_chislo_3")
        self.Ravning.addWidget(self.Home)
        self.Formul_vesh = QtWidgets.QWidget()
        self.Formul_vesh.setObjectName("Formul_vesh")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Formul_vesh)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 481, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_vesh = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_vesh.setFont(font)
        self.title_vesh.setStyleSheet("color: rgb(0, 85, 255);")
        self.title_vesh.setAlignment(QtCore.Qt.AlignCenter)
        self.title_vesh.setObjectName("title_vesh")
        self.verticalLayout.addWidget(self.title_vesh)
        self.fL = QtWidgets.QFormLayout()
        self.fL.setObjectName("fL")
        self.title_ab = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_ab.setFont(font)
        self.title_ab.setObjectName("title_ab")
        self.fL.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_ab)
        self.a_b = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.a_b.setFont(font)
        self.a_b.setObjectName("a_b")
        self.fL.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.a_b)
        self.title_formul = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_formul.setFont(font)
        self.title_formul.setObjectName("title_formul")
        self.fL.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.title_formul)
        self.pb_run = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_run.setStyleSheet("")
        self.pb_run.setObjectName("pb_run")
        self.fL.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pb_run)
        self.pictures_ab_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pictures_ab_2.setText("")
        self.pictures_ab_2.setPixmap(QtGui.QPixmap("1.jpg"))
        self.pictures_ab_2.setObjectName("pictures_ab_2")
        self.fL.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pictures_ab_2)
        self.vL = QtWidgets.QVBoxLayout()
        self.vL.setObjectName("vL")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vL.addItem(spacerItem)
        self.title_result = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_result.setFont(font)
        self.title_result.setObjectName("title_result")
        self.vL.addWidget(self.title_result)
        self.le_result = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_result.setObjectName("le_result")
        self.vL.addWidget(self.le_result)
        self.fL.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.vL)
        self.verticalLayout.addLayout(self.fL)
        self.Ravning.addWidget(self.Formul_vesh)
        self.cycle = QtWidgets.QWidget()
        self.cycle.setObjectName("cycle")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.cycle)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 441, 234))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.vl = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vl.setContentsMargins(0, 0, 0, 0)
        self.vl.setObjectName("vl")
        self.title_cycle = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_cycle.setFont(font)
        self.title_cycle.setStyleSheet("color: rgb(0, 85, 255);")
        self.title_cycle.setAlignment(QtCore.Qt.AlignCenter)
        self.title_cycle.setObjectName("title_cycle")
        self.vl.addWidget(self.title_cycle)
        self.title_znach = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_znach.setFont(font)
        self.title_znach.setObjectName("title_znach")
        self.vl.addWidget(self.title_znach)
        self.fl = QtWidgets.QFormLayout()
        self.fl.setObjectName("fl")
        self.title_formula = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_formula.setFont(font)
        self.title_formula.setObjectName("title_formula")
        self.fl.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.title_formula)
        self.formula = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.formula.setFont(font)
        self.formula.setObjectName("formula")
        self.fl.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.formula)
        self.pb_run_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pb_run_2.setStyleSheet("")
        self.pb_run_2.setObjectName("pb_run_2")
        self.fl.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pb_run_2)
        self.title_result_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_result_2.setFont(font)
        self.title_result_2.setObjectName("title_result_2")
        self.fl.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.title_result_2)
        self.le_result_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.le_result_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_result_2.setObjectName("le_result_2")
        self.fl.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_result_2)
        self.le_N = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.le_N.setObjectName("le_N")
        self.fl.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_N)
        self.N = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.N.setFont(font)
        self.N.setObjectName("N")
        self.fl.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.N)
        self.vl.addLayout(self.fl)
        self.Ravning.addWidget(self.cycle)
        self.vvod_formul = QtWidgets.QWidget()
        self.vvod_formul.setObjectName("vvod_formul")
        self.title_vvod_znach = QtWidgets.QLabel(self.vvod_formul)
        self.title_vvod_znach.setGeometry(QtCore.QRect(10, 50, 439, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_vvod_znach.setFont(font)
        self.title_vvod_znach.setObjectName("title_vvod_znach")
        self.title_vvod = QtWidgets.QLabel(self.vvod_formul)
        self.title_vvod.setGeometry(QtCore.QRect(20, 10, 439, 33))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_vvod.setFont(font)
        self.title_vvod.setStyleSheet("color: rgb(0, 85, 255);")
        self.title_vvod.setAlignment(QtCore.Qt.AlignCenter)
        self.title_vvod.setObjectName("title_vvod")
        self.N_2 = QtWidgets.QLabel(self.vvod_formul)
        self.N_2.setGeometry(QtCore.QRect(220, 50, 46, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.N_2.setFont(font)
        self.N_2.setObjectName("N_2")
        self.le_x = QtWidgets.QLineEdit(self.vvod_formul)
        self.le_x.setGeometry(QtCore.QRect(270, 50, 91, 21))
        self.le_x.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_x.setObjectName("le_x")
        self.N_3 = QtWidgets.QLabel(self.vvod_formul)
        self.N_3.setGeometry(QtCore.QRect(220, 80, 46, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.N_3.setFont(font)
        self.N_3.setObjectName("N_3")
        self.le_k = QtWidgets.QLineEdit(self.vvod_formul)
        self.le_k.setGeometry(QtCore.QRect(270, 80, 91, 21))
        self.le_k.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_k.setObjectName("le_k")
        self.title_formul_2 = QtWidgets.QLabel(self.vvod_formul)
        self.title_formul_2.setGeometry(QtCore.QRect(10, 120, 439, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.title_formul_2.setFont(font)
        self.title_formul_2.setObjectName("title_formul_2")
        self.pictures_2 = QtWidgets.QLabel(self.vvod_formul)
        self.pictures_2.setGeometry(QtCore.QRect(10, 150, 301, 131))
        self.pictures_2.setText("")
        self.pictures_2.setPixmap(QtGui.QPixmap("2.jpg"))
        self.pictures_2.setObjectName("pictures_2")
        self.pb_run_3 = QtWidgets.QPushButton(self.vvod_formul)
        self.pb_run_3.setGeometry(QtCore.QRect(320, 150, 151, 28))
        self.pb_run_3.setStyleSheet("")
        self.pb_run_3.setObjectName("pb_run_3")
        self.title_answer = QtWidgets.QLabel(self.vvod_formul)
        self.title_answer.setGeometry(QtCore.QRect(320, 210, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_answer.setFont(font)
        self.title_answer.setObjectName("title_answer")
        self.Answer_xk_2 = QtWidgets.QLineEdit(self.vvod_formul)
        self.Answer_xk_2.setGeometry(QtCore.QRect(320, 240, 151, 31))
        self.Answer_xk_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Answer_xk_2.setObjectName("Answer_xk_2")
        self.Ravning.addWidget(self.vvod_formul)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setStyleSheet("color: rgb(0, 0, 127);")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionnh = QtWidgets.QAction(MainWindow)
        self.actionnh.setObjectName("actionnh")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.actionnh)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.action_3)

        self.retranslateUi(MainWindow)
        self.Ravning.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение уравнений"))
        self.text_chislo_2.setText(_translate("MainWindow", "Программирование формул"))
        self.text_chislo_3.setText(_translate("MainWindow", "Выполнила Сорокина Таисия"))
        self.title_vesh.setText(_translate("MainWindow", "Формула с вещественными значениями"))
        self.title_ab.setText(_translate("MainWindow", "Даны значения:"))
        self.a_b.setText(_translate("MainWindow", "a = 2    b = 1"))
        self.title_formul.setText(_translate("MainWindow", "Формулы для вычисления:"))
        self.pb_run.setText(_translate("MainWindow", "Вычислить"))
        self.title_result.setText(_translate("MainWindow", "Ответ:"))
        self.title_cycle.setText(_translate("MainWindow", "Арифметический цикл"))
        self.title_znach.setText(_translate("MainWindow", "Введите значения:"))
        self.title_formula.setText(_translate("MainWindow", "Формула:"))
        self.formula.setText(_translate("MainWindow", "(2*N+1)!!"))
        self.pb_run_2.setText(_translate("MainWindow", "Вычислить"))
        self.title_result_2.setText(_translate("MainWindow", "Ответ:"))
        self.N.setText(_translate("MainWindow", "N = "))
        self.title_vvod_znach.setText(_translate("MainWindow", "Введите значения:"))
        self.title_vvod.setText(_translate("MainWindow", "Формула с введенными знач."))
        self.N_2.setText(_translate("MainWindow", "x = "))
        self.N_3.setText(_translate("MainWindow", "k = "))
        self.title_formul_2.setText(_translate("MainWindow", "Формула для вычисления:"))
        self.pb_run_3.setText(_translate("MainWindow", "Вычислить"))
        self.title_answer.setText(_translate("MainWindow", "Ответ:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "Домой"))
        self.actionnh.setText(_translate("MainWindow", "Формула с вещ. знач."))
        self.action_2.setText(_translate("MainWindow", "Цикл"))
        self.action_3.setText(_translate("MainWindow", "Формула с ввод. знач."))