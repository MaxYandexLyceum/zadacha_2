import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 2500, 1500)
        self.setWindowTitle('Супрематизм')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

        self.btn = QLabel(self)
        self.btn.setText("Никакая")
        self.btn.move(30, 50)
        global x
        global y
        global d
        global but
        x = 0
        y = 0
        d = 0
        self.f = False
        self.n = False
        but = ""
        self.x = 0
        self.y = 0
        self.xx = 0
        self.yy = 0

    def mousePressEvent(self, event):
        self.coords.setText(f"Координаты:{event.x()}, {event.y()}")
        global but
        if event.button() == Qt.LeftButton:
            self.btn.setText("Левая")
            but = "l"
        elif event.button() == Qt.RightButton:
            self.btn.setText("Правая")
            but = "r"
        global x
        global y
        self.x = event.x()
        self.y = event.y()
        self.f = True
        # currentQPoint = self.mapFromGlobal(QtGui.QCursor.pos())
        #print(currentQPoint.x(), currentQPoint.y())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.btn.setText("Пробел")
            global but
            but = "p"
            currentQPoint = self.mapFromGlobal(QtGui.QCursor.pos())
            self.x = currentQPoint.x()
            self.y = currentQPoint.y()
            self.coords.setText(f"Координаты:{self.x}, {self.y}")
            self.f = True

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        d = random.randint(0, 700)
        qp.setBrush(QColor(a, b, c))
        # Рисуем прямоугольник заданной кистью
        if self.n and but == "r":
            qp.drawRect(self.x - d // 2, self.y - d // 2, d, d)
        if self.n and but == "l":
            qp.drawEllipse(self.x - d // 2, self.y - d // 2, d, d)
        if self.n and but == "p":
            g = random.randint(0, 500)
            currentQPoint = self.mapFromGlobal(QtGui.QCursor.pos())
            self.x = currentQPoint.x()
            self.y = currentQPoint.y()
            qp.drawPolygon(QPoint(self.x - g, self.y + g), QPoint(self.x + g, self.y + g), QPoint(self.x, self.y - g))
        if self.f:
            self.update()
            self.f = False
        self.n = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

