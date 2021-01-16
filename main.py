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
        self.n = False

    def initUI(self):
        uic.loadUi("okruzhnost.ui", self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        x = random.randint(1, 300)
        y = random.randint(1, 300)
        a = random.randint(1, 300)
        qp.setPen(QColor(255, 255, 0))
        qp.drawEllipse(x, y, a, a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
