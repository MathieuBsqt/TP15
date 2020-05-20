from PySide2.QtWidgets import  *
from eX1 import *


class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.text=text
        self.layout = QHBoxLayout()
        self.label=QLabel(self.text)
        self.layout.addWidget(self.label)
        self.text=QTextEdit()
        self.layout.addWidget(self.text)
        self.setMaximumHeight(50)
        self.setLayout(self.layout)

class ConfigurationDiagol(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout=QVBoxLayout()

        self.text1=LabeledTextField("IP Adress")
        self.layout.addWidget(self.text1)

        self.text2=LabeledTextField("User")
        self.layout.addWidget(self.text2)

        self.text3=LabeledTextField("Password")
        self.layout.addWidget(self.text3)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDiagol()
   win2 = SQLClientWindow()
   win.show()
   win2.show()
   app.exec_()

