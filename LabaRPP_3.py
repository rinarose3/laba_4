from PyQt5 import QtWidgets
import sys
import py_laba3

Result = "Result.txt"
Sourse = "Sourse.txt"
NewResult = "NewResult.txt"


class MainApp(QtWidgets.QMainWindow, py_laba3.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_shifr_2.clicked.connect(self.Shifr)
        self.pb_rashifr_2.clicked.connect(self.Rashifr)

    def Shifr(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)

        gamma = gamma_list
        line = self.line_vvod_2.toPlainText()
        with open("Sourse.txt", "w") as file:
            file.write(line)

        res = open("Result.txt", "w", encoding="utf-8")
        with open('Sourse.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))

                else:
                    break

        self.line_shifr_2.setText(r)

    def Rashifr(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)

        gamma = gamma_list
        line = self.line_shifr_2.toPlainText()
        with open("Result.txt", "w") as file:
            file.write(line)

        res = open("NewResult.txt", "w", encoding="utf-8")
        with open('Result.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))
                else:
                    break
        self.line_enter_2.setText(r)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()