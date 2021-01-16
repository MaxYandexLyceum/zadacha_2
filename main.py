import sys

from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.f = False

    def initUI(self):
        uic.loadUi("okruzhnost.ui", self)
        self.f = False
        self.pushButton.clicked.connect(self.do)

    def do(self):
        self.f = True

    def paintEvent(self, event):
        if self.f:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()
            self.f = False

    def draw_flag(self, qp):
        x = random.randint(1, 300)
        y = random.randint(1, 300)
        a = random.randint(1, 300)
        print(x, y, a)
        #qp.setBrush(QColor(256, 50, 50))
        qp.drawRect(x, y, a, a)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
