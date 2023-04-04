import sys

from button_pyqt import Ui_Python
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Python = QtWidgets.QMainWindow()
    ui = Ui_Python()
    ui.setupUi(Python)
    Python.show()
    sys.exit(app.exec_())
