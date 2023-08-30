import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                            QHBOxLayout ,QVBoxLayout,QGroupDox,QRadioButton,
                            QLineEdit,QPushButton )

from instr import*
from second_win import*

class MainWin(QWidget):
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
        self.layout= QVBoxLayout()


    def initUI(self):
        self.hello_txt=QLabel(txt_hello)
        self.btn_next = QPushButton(txt_next)
        self.instructions=QLabel(txt_instructions)
        self.layout=QVBoxLayout

        self.layout.addWidget(self.hello_txt )
        self.layout.addWidget(self.btn_next)
        self.layout.addWidget(self.instructions)
        self.setLayout(self.layout)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.tw=TextWin()
        self.hide()
        
app = Application([])
mw = MainWin()

app.exec_()