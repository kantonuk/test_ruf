from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QHBOxLayout ,QVBoxLayout,QGroupDox,QRadioButton,
                             QLineEdit,QPushButton )

from instr import*
from second_win import*

class FinalWin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()



    def set_appear(self):
        self.setWindowTitle(title_txt)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.workh_test=QLabel(txt_workheart)
        self.index_text=QLabel(txt_index)
        self.line.layout=QVBoxLayout()
        self.line_layout.addWidget(self.index_text,alignment=Qt.AlignCentre)
        self.line_layout.addWidget(self.workh_text,alignment=Qt.AlignCentre)
        self.setLayout(self.line_layout)

    def connects(self):
        pass