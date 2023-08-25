from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QHBOxLayout ,QVBoxLayout,QGroupDox,QRadioButton,
                             QLineEdit,QPushButton )
from instr import*

class TextWin(QWidget):
    def self_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        pass

    def connects(self):
        pass
