""" ??? """
import sys
import os
import time
import threading
import multiprocessing
import requests
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

PREVLIST = []
NEXTLIST = []

BASEURL = "http://www.freeomovie.com/page/"
DATAPATH = str(os.getcwd() + "/Data/")
VIDEOPATH = str(os.getcwd() + "/Video/")

class Window():
    widget = 0
    btn_save = 0
    btn_remove = 0
    btn_skip = 0
    img_label = 0
    btn_next = 0
    btn_prev = 0
    itera = 0
    note = ""
    url = ""
    pxmp = ""
    curr = []

    def __init__(self):
        self.initalize()
        time.sleep(5)
        self.widget = QWidget()
        self.widget.setObjectName("Widget")
        self.widget.setGeometry(QRect(0, 0, 756, 510))

        self.curr = PREVLIST.pop(self.itera)
        PREVLIST.insert(self.itera, self.curr)
        self.note = str(self.curr[0])
        self.pxmp = QPixmap(self.curr[1])
        self.url = self.curr[2]

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setText("Save")
        self.btn_save.setGeometry(QRect(640, 440, 104, 26))
        self.btn_save.clicked.connect(lambda: self.save())
        self.btn_remove = QPushButton(self.widget)
        self.btn_remove.setText("Remove")
        self.btn_remove.setGeometry(QRect(640, 480, 104, 26))
        self.btn_remove.clicked.connect(lambda: self.remove())
        self.btn_skip = QPushButton(self.widget)
        self.btn_skip.setText("Skip Remaining")
        self.btn_skip.setGeometry(QRect(10, 470, 104, 26))
        self.btn_skip.clicked.connect(lambda: self.skip())
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
        if self.itera < len(PREVLIST) and not self.curr in PREVLIST:
            PREVLIST.insert(self.itera, self.curr)
            self.itera = self.itera + 1
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)
            print("Next!")
        elif self.itera < len(PREVLIST) and self.curr in PREVLIST:
            self.itera = self.itera + 1
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)
            print("Next!")
        elif self.itera == (len(PREVLIST) - 1):
            self.startnxtroutine()
            pass
        else:
            PREVLIST.insert(self.itera, self.curr)
            self.itera = 0
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)

    def movelistprev(self):
        if self.itera > 0 and not self.curr in PREVLIST:
            PREVLIST.insert(self.itera, self.curr)
            self.itera = self.itera - 1
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)
            print("Prev!")
        elif self.itera > 0 and self.curr in PREVLIST:
            self.itera = self.itera - 1
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)
            print("Prev!")
        else:
            PREVLIST.insert(self.itera, self.curr)
            self.itera = len(PREVLIST) - 1
            self.curr = PREVLIST.pop(self.itera)
            self.note = str(self.curr[0])
            self.pxmp = QPixmap(self.curr[1])
            self.url = self.curr[2]
            self.img_label.setPixmap(self.pxmp)

    def save(self):
        print("Start adding")
        self.btn_save.setEnabled(True)
        if self.itera <= len(PREVLIST):
            if not self.curr in NEXTLIST:
                NEXTLIST.append([self.curr[0], self.curr[1], self.curr[2]])
                #PREVLIST.insert(self.itera, self.curr)
                #self.itera = self.itera + 1
                #self.curr = PREVLIST.pop(self.itera)
                #self.note = str(self.curr[0])
                #self.pxmp = QPixmap(self.curr[1])
                #self.url = self.curr[2]
                #self.img_label.setPixmap(self.pxmp)
                print("finished adding")
            else:
                print("Already in list")
                self.btn_save.setEnabled(False)

        if self.itera == (len(PREVLIST)):
            print("Starting next")
            self.startnxtroutine()


    def remove(self):
        self.btn_remove.setEnabled(True)
        if self.url in NEXTLIST:
            NEXTLIST.remove(self.url)
            print("removed")
        else:
            self.btn_remove.setEnabled(False)

    def skip(self):
        print("End of List reached!")
        self.printlist()
        self.startnxtroutine()

    def printlist(self):
        print("###################################")
        for elem in NEXTLIST:
            print(elem)
        print("###################################")

    def initalize(self):
        """ """
        os.chdir(os.getcwd())
        if not os.path.exists(DATAPATH):
            os.mkdir(DATAPATH)

        if not os.path.exists(VIDEOPATH):
            os.mkdir(VIDEOPATH)

        for number in range(1, 2):
            worker = threading.Thread(target=self.parser, args=(str(number), ), daemon=True)
            worker.start()

    def parser(self, val):
        """ """
        url = BASEURL + str(val)
        outname = "./page_" + str(val) + ".html"
        self.my_download(url, outname)
        with open(outname, "r", encoding="UTF-8") as out:
            for line in  out:
                if "<div class=\"boxentry\">" in line:
                    url = str(next(out))
                    name = url.split("\" title=\"")[1].split("\"")[0]
                    name = name.replace(u"\u2013", "-").replace("&#8217;", "'").replace("&#8211;", "-").replace(u"\xfc", "-")
                    name = name.replace(u"\u00fc", "ue").replace(u"\u00f6", "oe").replace(u"\u00e4", "ae").replace(u"\u00df", "ss")
                    name = name.replace(u"\u00dc", "Ue").replace(u"\u00d6", "Oe").replace(u"\u00c4", "Ae")
                    name = name.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace("ß", "ss")
                    print(name)
                    url = url.split("<a href=\"")[1].split("\" title=\"")[0]
                    print(url)
                    imgurl = str(next(out))
                    imgurl = imgurl.split("<img src=\"")[1].split("\"")[0]
                    if "jpg" in imgurl:
                        img_format = ".jpg"
                    elif "png" in imgurl:
                        img_format = ".png"
                    elif "jpeg" in imgurl:
                        img_format = ".jpeg"
                    else:
                        img_format = ".jpg"
                    print(imgurl)
                    imgpath = str(DATAPATH + name + img_format)
                    self.my_download(imgurl, imgpath)
                    PREVLIST.append([str(name), str(imgpath), str(url)])
        for elem in PREVLIST:
            print(elem)
        return

    def my_download(self, url, outname):
        """ """
        with open(outname, "wb") as file:#open in binary write mode
            response = requests.get(url)#get request
            file.write(response.content)#write to file

    def startnxtroutine(self):
        for movie in NEXTLIST:
            grabber = multiprocessing.Process(target=self.parsemovie, args=(movie, ), daemon=True)
            grabber.start()

    def parsemovie(self, movie):
        partlist = []
        outname = DATAPATH + str(movie[0]) + ".html"
        print("Parsing " + str(movie[0]))
        self.my_download(str(movie[2]), outname)
        with open(outname, "r", encoding="UTF-8") as out:
            for line in out:
                if "<li><a id=\'Openloadco\'" in line:
                    url = str(next(out))
                    url = url.split("&myURL[]=")[1].split("\"")[0]
                    print(str(movie[0]) + str(url))
                    if "&myURL[]=" in url:
                        for x in range(0, (len(url.split("&myURL[]=")) - 1)):
                            partlist.append(url.split("&myURL[]=")[x])
                    else:
                        partlist.append(url)
                    for part in partlist:
                        index = partlist.index(part) + 1
                        getter = threading.Thread(target=self.parsepart, args=(movie[0], part, index), daemon=True)
                        getter.start()
                        while getter.is_alive():
                            time.sleep(1)
                        return

                if "<li><a id=\'streamcloud\'" in line:
                    url = str(next(out))
                    url = url.split("&myURL[]=")[1].split("&tab=1\"")[0]
                    print(str(movie[0]) + str(url))
                    if "&myURL[]=" in url:
                        for x in range(0, (len(url.split("&myURL[]=")) - 1)):
                            partlist.append(url.split("&myURL[]=")[x])
                    else:
                        partlist.append(url)
                    for part in partlist:
                        index = partlist.index(part) + 1
                        getter = threading.Thread(target=self.parsepart, args=(movie[0], part, index), daemon=True)
                        getter.start()
                        while getter.is_alive():
                            time.sleep(1)
                        return

    def parsepart(self, name, url, index):
        partname = DATAPATH + str(name) + " CD " + str(index) + ".html"
        self.my_download(url, partname)
        if "openload" in url:
            print("openload")
            #use Requests to invoke button
            with open(partname, "r", encoding="UTF-8") as part:
                for line in part:
                    if "<video id=\"" in line:
                        vidurl = line.split("src=\"")[1].split("\">")[0]
                        vidurl = "https://openload.co" + vidurl
                        vidname = VIDEOPATH + str(name) + " CD " + str(index) + ".mp4"
                        self.my_download(vidurl, vidname)
        if "streamcloud" in url:
            #use Requests to invoke button
            print("StreamCloud please Fix")

def __main__():

    """
    PREVLIST.append("tregdofdfer /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.deeekd.vggd".split(" "))
    PREVLIST.append("ffsff /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.zjgfhgyg.vggd".split(" "))
    PREVLIST.append("gnfgdhg /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.yhxgfjg.vggd".split(" "))
    PREVLIST.append("sgsdfdfh /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.ftjhghh.vggd".split(" "))
    PREVLIST.append("dsgdhgff /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.jtghdhhd.vggd".split(" "))
    PREVLIST.append("kudhghg /home/koro/Pictures/tumblr_o6za5kduSo1qcxl1io1_1280.png HTTP://www.hthgdfd.vggd".split(" "))
    """
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

__main__()