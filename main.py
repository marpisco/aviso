import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPalette

class AvisoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        
        screen_geometry = QApplication.desktop().screenGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.setGeometry(0, screen_height - int(screen_height * 0.15), screen_width, int(screen_height * 0.15))
        self.label = QLabel("Aviso: Este quisque irá ser descontinuado.\nPor favor passe a utilizar o GIAE ou a App Móvel do GIAE.\nCaso tenha perguntas, dirija-se à secretaria.", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: white; font-size: 24px; text-align: center; width: 100%;")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.color_flag = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changeColor)
        self.timer.start(1000)
        
        self.show()

    def changeColor(self):
        if self.color_flag:
            self.setBackgroundColor(QColor('red'))
        else:
            self.setBackgroundColor(QColor('orange'))
        self.color_flag = not self.color_flag

    def setBackgroundColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AvisoWindow()
    sys.exit(app.exec_())