import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_derlem import Ui_dlgDerlem
from ui_secenekler import Ui_Dialog


class Secenekler(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Secenekler, self).__init__()
        self.setupUi(self)


    def secenekKaydet(self):
        print("secenek kaydet")
        

class MyDialog(QtWidgets.QDialog, Ui_dlgDerlem):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)
        self.show()

    def secenekler(self):
        s = Secenekler()
        x = s.exec_()
        print("secenekler")

    def kaydet(self):
        print("kaydet")

    def donustur(self):
        print("donustur")

    def dosyasec(self):
        print("dosyasec")
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Dosya sec')
        if fname[0]:
            f = open(fname[0],"r").read()
            self.editGirdi.setPlainText(f)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyDialog()
    sys.exit(app.exec_())
