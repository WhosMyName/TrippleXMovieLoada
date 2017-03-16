
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time

PREVLIST = []
NEXTLIST = []
#APP = QApplication(sys.argv)

class Window():
    widget = 0
    btn_save = 0
    btn_remove = 0
    btn_exit = 0
    img_label = 0
    btn_next = 0
    btn_prev = 0
    itera = 0
    note = ""
    url = ""
    pxmp = ""

    def __init__(self):
        self.widget = QWidget()
        self.widget.setObjectName("Widget")
        self.widget.setGeometry(QRect(0, 0, 756, 510))

        self.note = str(PREVLIST[self.itera][0])
        self.pxmp = QPixmap(PREVLIST[self.itera][1])
        self.url = PREVLIST[self.itera][2]

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setText("Save")
        self.btn_save.setGeometry(QRect(640, 440, 104, 26))
        self.btn_save.clicked.connect(lambda: self.enable())
        self.btn_remove = QPushButton(self.widget)
        self.btn_remove.setText("Remove")
        self.btn_remove.setGeometry(QRect(640, 480, 104, 26))
        self.btn_remove.clicked.connect(lambda: self.disable())
        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setText("Exit")
        self.btn_exit.setGeometry(QRect(10, 470, 104, 26))
        self.btn_exit.clicked.connect(lambda: self.printlist())
        self.btn_next = QPushButton(self.widget)
        self.btn_next.setText("Next")
        self.btn_next.setGeometry(QRect(630, 10, 104, 26))
        self.btn_next.clicked.connect(lambda: self.movelistnext())
        self.btn_prev = QPushButton(self.widget)
        self.btn_prev.setText("Previous")
        self.btn_prev.setGeometry(QRect(10, 10, 104, 26))
        self.btn_prev.clicked.connect(lambda: self.movelistprev())

        self.img_label = QLabel(self.widget)
        self.img_label.setText(self.note)
        self.img_label.setGeometry(QRect(140, 10, 471, 491))
        self.img_label.setPixmap(self.pxmp)

        QMetaObject.connectSlotsByName(self.widget)
        self.widget.show()

    def movelistnext(self):
        if self.itera < (len(PREVLIST) -1):
            self.itera = self.itera + 1
            self.note = str(PREVLIST[self.itera][0])
            print(self.note)
            self.pxmp = QPixmap(PREVLIST[self.itera][1])
            self.url = PREVLIST[self.itera][2]
            self.img_label.setPixmap(self.pxmp)
            print("Next!")
        elif self.itera == len(PREVLIST):
            #startnxtroutine()
            pass
        else:
            print("End of List reached!")

    def movelistprev(self):
        if self.itera > 0:
            self.itera = self.itera - 1
            self.note = str(PREVLIST[self.itera][0])
            print(self.note)
            self.pxmp = QPixmap(PREVLIST[self.itera][1])
            self.url = PREVLIST[self.itera][2]
            self.img_label.setPixmap(self.pxmp)
            print("Prev!")
        else:
            print("End of List reached!")


    def enable(self):
        print("Start adding")
        if self.itera < (len(PREVLIST) -1):
            if not self.url in NEXTLIST:
                #self.itera = self.itera + 1
                NEXTLIST.append(self.url)
                #self.note = str(PREVLIST[self.itera][0])
                #self.pxmp = QPixmap(PREVLIST[self.itera][1])
                #self.url = PREVLIST[self.itera][2]
                #self.img_label.setPixmap(self.pxmp)
                print("finished adding")
                print("pls")
                print("ffs")
            else:
                #disable_button()
                pass
        elif self.itera == len(PREVLIST):
            #startnxtroutine()
            pass

    def disable(self):
        if self.url in NEXTLIST:
            NEXTLIST.remove(self.url)
            print("removed")
        else:
            print("nothing to remove")
            pass

    def printlist(self):
        print("###################################")
        for x in NEXTLIST:
            print(x)
        print("###################################")

def __main__():

    PREVLIST.append("tregdofdfer /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.deeekd.vggd".split(" "))
    PREVLIST.append("ffsff /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.zjgfhgyg.vggd".split(" "))
    PREVLIST.append("gnfgdhg /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.yhxgfjg.vggd".split(" "))
    PREVLIST.append("sgsdfdfh /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.ftjhghh.vggd".split(" "))
    PREVLIST.append("dsgdhgff /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.jtghdhhd.vggd".split(" "))
    PREVLIST.append("kudhghg /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.hthgdfd.vggd".split(" "))

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

__main__()