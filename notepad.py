from PyQt5.QtGui import *
import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('notepad.ui', self)
        global textEdit
        self.control = self.textEdit.toPlainText()
        self.flag = False
        self.flagChange = False
        textEdit = self.textEdit
        self.actionOpen.triggered.connect(self.onOpenTriggered)
        self.actionSave.triggered.connect(self.onSaveTriggered)
        self.actionSave_As.triggered.connect(self.onSaveAsTriggered)
        self.actionExit.triggered.connect(self.onSaveDialogTriggered)

    def onOpenTriggered(self, sender):
        self.textEdit.clear()
        fileDialog = QFileDialog(self, 'Dosya seçiniz','' ,'TextFiles(*.txt)')
        if fileDialog.exec() == QDialog.Accepted:
            global file_name
            file_name = fileDialog.selectedFiles()[0]
            try:
                with open(file_name, encoding='utf-8-sig') as file:
                    s = file.read()
                    self.textEdit.setText(s)
                    self.control = self.textEdit.toPlainText()
            except Exception as err:
                QMessageBox.information(self, 'Error', err)
            self.flag = True




    def onSaveTriggered(self, sender):

        if self.flag is True:
            complateName = os.path.join(file_name)
            with open(complateName, 'r+') as file:
                s = self.textEdit.toPlainText()
                file.write(s)
        else:
            path = QFileDialog.getSaveFileName(self, 'Bir dosya seciniz', '.', 'Text Files(*.txt)')
            if path[0] != '':
                complateName = os.path.join(path[0])
                with open(complateName, 'w+') as file:
                    s = self.textEdit.toPlainText()
                    file.write(s)

        self.flag = False

    def onSaveAsTriggered(self, sender):
        path = QFileDialog.getSaveFileName(self, 'Bir dosya seciniz', '.', 'Text Files(*.txt)')
        if path[0] != '':
            complateName = os.path.join(path[0])
            with open(complateName, 'w+') as file:
                s = self.textEdit.toPlainText()
                file.write(s)

    def onSaveDialogTriggered(self):
        if self.control != self.textEdit.toPlainText():
            try:
                myDialog = SaveDialog()
                myDialog.exec()
            except Exception as err:
                print(err)
        else:
            self.close()



class SaveDialog(QDialog):
    def __init__(self):
        super(SaveDialog, self).__init__()
        loadUi('fileSave.ui', self)
        self.pushButtonSave.clicked.connect(self.onButtonSaveClickedHandler)
        self.pushButtonNoSave.clicked.connect(self.onButtonNoSaveClickedHandler)
        self.pushButtonCancel.clicked.connect(self.onButtonCancelClickedHandler)

    def onButtonSaveClickedHandler(self):
        path = QFileDialog.getSaveFileName(self, 'Bir dosya seciniz', '.', 'Text Files(*.txt)')
        if path[0] != '':
            complateName = os.path.join(path[0])
            with open(complateName, 'w+') as file:
                s = textEdit.toPlainText()
                file.write(s)
        sys.exit()

    def onButtonNoSaveClickedHandler(self):
        sys.exit()

    def onButtonCancelClickedHandler(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()


main()
