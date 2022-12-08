from PyQt5 import QtWidgets
import sys
import math

import py_rpp2


class RPP_2(QtWidgets.QMainWindow, py_rpp2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action.triggered.connect(lambda: self.Ravning.setCurrentIndex(0))
        self.actionnh.triggered.connect(lambda: self.Ravning.setCurrentIndex(1))
        self.action_2.triggered.connect(lambda: self.Ravning.setCurrentIndex(2))
        self.action_3.triggered.connect(lambda: self.Ravning.setCurrentIndex(3))

        self.pb_run.clicked.connect(self.vesh)
        self.pb_run_2.clicked.connect(self.matcycle)
        self.pb_run_3.clicked.connect(self.vvod)

    def vesh(self):
        try:
            a = 2
            b = 1
            X = math.sqrt(abs(a) + (math.sqrt(abs(a) + abs(b))) + ((a-b) ** 2))
            self.Y = ((math.tan(abs(a) + X + math.radians(30))** 2) * math.exp(-X))/ (X + 2.5 ** 0.4)
            self.le_result.setText(f"{round(self.Y, 4)}")

        except Exception:
            self.statusbar.showMessage('Проверьте введенные значения')

    def matcycle(self):
        try:
            pole = self.le_N.text()
            poles = self.matcycle_ch(int(pole))
            self.le_result_2.setText(poles)

        except Exception:
            if not self.le_N.text():
                self.statusbar.showMessage('Вы не ввели значения')
            else:
                self.statusbar.clearMessage()

    def matcycle_ch(self, poles):
        if poles == 0 or poles == 1:
            poles = 1
            return f"{poles}"
        else:
            if poles > 1:
                pole = 2 * poles + 1
                pole = math.prod(range(pole, 0, -2))
                return f"{pole}"
            else:
                return f"{poles == 1}"

    def vvod(self):
        try:
            x = self.le_x.text()
            x = int(x)
            k = self.le_k.text()
            k = int(k)

            y = 0
            if k == 1:
                y = math.log2(abs(x ** 2 + 1))
            elif k == 2:
                y = math.sqrt(abs(x ** 3 + 2 * x + 5))
            elif k == 3:
                y = math.sqrt(abs(x+1) + abs(x - 1))
            else:
                y = math.exp(-1 / (x ** 2 + 1))

            self.Answer_xk_2.setText(str(y))

        except Exception:
            if not self.le_x.text():
                self.statusbar.showMessage('Проверьте введенные значения')
            else:
                self.statusbar.clearMessage()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RPP_2()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
