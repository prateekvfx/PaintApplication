import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PaintUI import Ui_MainWindow
from PyQt6.QtGui import QImage, QPainter, QPen, QIcon
from PyQt6.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Paint Tool - Prateek Shukla")
        self.setWindowIcon(QIcon("icons/paintBrush.png"))
        # self.statusBar().showMessage("Developed by Prateek Shukla")

        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.GlobalColor.black
        self.lastPoint = QPoint()

        # connecting signals
        self.ui.actionsave.triggered.connect(self.save)
        self.ui.actionclear.triggered.connect(self.clear)
        self.ui.action3px.triggered.connect(self.threePixel)
        self.ui.action5px.triggered.connect(self.fivePixel)
        self.ui.action7px.triggered.connect(self.sevenPixel)
        self.ui.action9px.triggered.connect(self.ninePixel)

        self.ui.actionBlack.triggered.connect(self.blackColor)
        self.ui.actionWhite.triggered.connect(self.whiteColor)
        self.ui.actionRed.triggered.connect(self.redColor)
        self.ui.actionGreen.triggered.connect(self.greenColor)
        self.ui.actionYellow.triggered.connect(self.yellowColor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.position()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.MouseButton.LeftButton):
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine))
            painter.drawLine(self.lastPoint, event.position())
            self.lastPoint = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image",
                                                  "PNG(*.png);; JPEG(*.jpg * .jpeg);; All Files(*.*)")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.GlobalColor.white)
        self.update()

    def threePixel(self):
        self.brushSize = 3

    def fivePixel(self):
        self.brushSize = 5

    def sevenPixel(self):
        self.brushSize = 7

    def ninePixel(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.GlobalColor.black

    def whiteColor(self):
        self.brushColor = Qt.GlobalColor.white

    def redColor(self):
        self.brushColor = Qt.GlobalColor.red

    def greenColor(self):
        self.brushColor = Qt.GlobalColor.green

    def yellowColor(self):
        self.brushColor = Qt.GlobalColor.yellow


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())

