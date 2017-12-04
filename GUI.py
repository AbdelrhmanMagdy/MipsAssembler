#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import os,sys

class Dialog(QtGui.QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        self.createGridGroupBox()


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.gridGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("MIPS Assembler")

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()

        self.fileMenu = QtGui.QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)


    def createGridGroupBox(self):
        self.gridGroupBox = QtGui.QGroupBox("MIPS Assembler")
        layout = QtGui.QGridLayout()

        buildBtn = QtGui.QPushButton("Build")
        buildBtn.clicked.connect(self.buildAction)
        runBtn = QtGui.QPushButton("Run")
        runBtn.clicked.connect(self.runAction)
        clearBtn = QtGui.QPushButton("Clear")
        clearBtn.clicked.connect(self.clearAction)  
        layout.addWidget(buildBtn, 0,3)
        layout.addWidget(runBtn, 1, 3)
        layout.addWidget(clearBtn, 2, 3)

        self.inputText = QtGui.QTextEdit()
        self.outputText = QtGui.QTextEdit()
        self.outputText.setReadOnly(True)
        layout.addWidget(self.inputText, 0, 1, 4, 1)
        layout.addWidget(self.outputText, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)
    def buildAction(self):
        self.outputText.clear()        
        with open("input.asm",'w') as file:
            file.write(self.inputText.toPlainText())
        # print(self.inputText.toPlainText())
    def runAction(self):
        with open("output.bin",'r')as file:
            text=file.read()
            self.outputText.append(text)
            os.system("python main.py input.txt")
    def clearAction(self):
        self.outputText.clear()


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
