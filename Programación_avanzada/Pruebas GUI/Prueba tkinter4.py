import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QPen, QColor, QPainterPath
from PyQt6.QtCore import Qt, QRectF
from math import cos, sin, radians


# Maria Camila Chaparro Pinilla, USTA, PROGRAMACIÓN AVANZADA, 2024
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Figuras")
        self.setFixedSize(400, 400)

        self.mostrar_figura = Figura()

        self.menu = QComboBox()
        self.menu.addItems(["Círculo", "Cuadrado", "Triángulo", "Octógono"])

        self.menu.currentTextChanged.connect(self.cambio_figura)

        formato = QVBoxLayout()
        formato.addWidget(self.menu)
        formato.addWidget(self.mostrar_figura)

        container = QWidget()
        container.setLayout(formato)

        self.setCentralWidget(container)

    def cambio_figura(self, seleccion):
        self.mostrar_figura.fijarFigura(seleccion)


class Figura(QWidget):

    def __init__(self):
        super(Figura, self).__init__()
        self.figura = None
        self.color = QColor("yellow")

    def fijarFigura(self, figura):
        self.figura = figura
        self.update()

    def paintEvent(self, event):
        pintar = QPainter(self)
        pintar.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        pintar.setBrush(self.color)

        area = QRectF(100, 100, 200, 200)

        if self.figura is None:
            pintar.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, "FIGURAS")
        elif self.figura == "Círculo":
            pintar.drawEllipse(area)
        elif self.figura == "Cuadrado":
            pintar.drawRect(area)
        elif self.figura == "Triángulo":
            trazo = QPainterPath()
            trazo.moveTo(200, 100)
            trazo.lineTo(300, 300)
            trazo.lineTo(100, 300)
            trazo.lineTo(200, 100)
            pintar.drawPath(trazo)
        elif self.figura == "Octógono":
            trazo = QPainterPath()
            angulo = 45
            centrox, centroy = 200, 200
            radius = 100
            for i in range(8):
                x = centrox + radius * cos(radians(angulo * i))
                y = centroy + radius * sin(radians(angulo * i))
                if i == 0:
                    trazo.moveTo(x, y)
                else:
                    trazo.lineTo(x, y)
            trazo.closeSubpath()
            pintar.drawPath(trazo)


app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()

app.exec()
