#MyWidget class essentially outputs a 1000x800 window displaying self.text
#text is aligned center
from PySide6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.text = QtWidgets.QLabel("Ethan Bleier; cst_205; lab 10", 
        alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1000, 800)
    widget.show()

    sys.exit(app.exec())