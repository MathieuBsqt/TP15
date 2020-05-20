from PySide2.QtWidgets import  *
from PySide2.QtGui import *


class SQLClientWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.Objet=ButtonsPanel()
        self.NotificationPannel=QTextEdit()
        self.layout.addWidget(self.Objet)
        self.layout.addWidget(self.NotificationPannel)

        self.resultable=QTableWidget(5,3)
        self.resultable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.resultable)


        self.setLayout(self.layout)

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.Button=QPushButton("Configure")
        self.Button2=QPushButton("Connect")
        self.Button3=QPushButton("Disconnect")
        self.layout.addWidget(self.Button)
        self.layout.addWidget(self.Button2)
        self.layout.addWidget(self.Button3)
        self.setLayout(self.layout)







if __name__ == "__main__":
   app = QApplication([])
   win = SQLClientWindow()
   win.show()
   app.exec_()

