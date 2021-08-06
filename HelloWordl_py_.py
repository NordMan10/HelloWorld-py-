import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from myDesign import *

data = []
data.append(("1", "600", "630", "660", "240", "yes"))
data.append(("2", "680", "720", "780", "-", "no"))

tableHeaders = ("Id ВС", "Тплан.", "Твозм.", "Тразр.", "Время обработки", "Необходимость обработки")

class MyWindow(QtWidgets.QMainWindow):

    

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.clearTable)

        self.ui.label.setFont(QtGui.QFont('SansSerif', 16))
        self.ui.label.setText("Hello")

        self.initTable()
        self.fillTable()

    def buttonClickHandler(self):
        self.ui.label.setText("Clicked!")
        self.ui.label.adjustSize()


    def initTable(self):

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.setTableHeaders()

    def fillTable(self):
        row = 0
        for dataItem in data:
            col = 0
 
            for item in dataItem:
                cellinfo = QTableWidgetItem(item)
 
                # Только для чтения
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )
 
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
 
            row += 1

    def clearTable(self):
        self.ui.tableWidget.clear()

    def setTableHeaders(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(tableHeaders)



app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())