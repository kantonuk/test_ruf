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
        self.text_timer=QLabel(txt_timer)
        self.text_name=QLabel(txt_name)
        





        self.l_line=QVBoxLayout
        self.r_line=QVBoxLayout
        self.h_line=QHBOxLayout


        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_name,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next,alignment=Qt.AlignCentre)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
        


    def connects(self):
        pass
