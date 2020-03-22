import sys, time

from PyQt5.QtWidgets import (
     QApplication,
     QGraphicsScene,
     QGraphicsGridLayout,
     QGraphicsTextItem,
     QGraphicsWidget,
     QGraphicsView,
     QMainWindow,
     QGraphicsRectItem)

from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtGui import QColor

class ClockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.scene = QGraphicsScene()
        self.gView = QGraphicsView(self.scene)
        self.gView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCentralWidget(self.gView)
        self.layout = QGraphicsGridLayout()
        graphicsW = QGraphicsWidget()
        graphicsW.setLayout(self.layout)
        self.scene.addItem(graphicsW)
        gli = QGraphicsWidget()
        QGraphicsRectItem(0, 5, 10, 10, gli)
        self.layout.addItem(gli, 0 , 0)
        gli = QGraphicsWidget()
        QGraphicsRectItem(0, 5, 10, 10, gli)
        self.layout.addItem(gli, 11 , 0)
        gli = QGraphicsWidget()
        QGraphicsRectItem(0, 5, 10, 10, gli)
        self.layout.addItem(gli, 0 , 12)
        gli = QGraphicsWidget()
        QGraphicsRectItem(0, 5, 10, 10, gli)
        self.layout.addItem(gli, 11, 12)
        for row, letterarr in enumerate([['E','S','K','I','S','T','A','F','Ü','N','F'],
                                         ['Z','E','H','N','Z','W','A','N','Z','I','G'],
                                         ['D','R','E','I','V','I','E','R','T','E','L'],
                                         ['V','O','R','F','U','N','K','N','A','C','H'],
                                         ['H','A','L','B','A','E','L','F','Ü','N','F'],
                                         ['E','I','N','S','X','A','M','Z','W','E','I'],
                                         ['D','R','E','I','P','M','J','V','I','E','R'],
                                         ['S','E','C','H','S','N','L','A','C','H','T'],
                                         ['S','I','E','B','E','N','Z','W','Ö','L','F'],
                                         ['Z','E','H','N','E','U','N','K','U','H','R']]):
            for pos, letter in enumerate(letterarr):
                gli = QGraphicsWidget()
                QGraphicsTextItem(letter, gli)
                self.layout.addItem(gli, row + 1, pos + 1)
        

        
    def showWords(self, timeToShow):
        wordConversion = {'es': [[0, 0], [0, 1]], 'ist': [[0, 3], [0, 4], [0, 5]], 'fuenfmin': [[0, 7], [0, 8], [0, 9], [0, 10]],
                          'zehnmin': [[1, 0], [1, 1],[1, 2], [1, 3]], 'zwanzig': [[1, 4], [1, 5],[1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],
                          'dreibruch': [[2, 0], [2, 1],[2, 2], [2, 3]], 'viertel': [[2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],
                          'vor': [[3, 0], [3, 1],[3, 2]], 'nach': [[3, 7], [3, 8], [3, 9], [3, 10]],
                          'halb': [[4, 0], [4, 1],[4, 2], [4, 3]], 'elf':[[4, 5], [4, 6],[4, 7]], 'fuenf': [[4, 7], [4, 8], [4, 9], [4, 10]],
                          'ein': [[5, 0], [5, 1],[5, 2]], 'eins': [[5, 0], [5, 1],[5, 2], [5, 3]], 'am': [[5, 5], [5, 6]], 'zwei': [[5, 7], [5, 8], [5, 9], [5, 10]],
                          'drei': [[6, 0], [6, 1],[6, 2], [6, 3]], 'pm': [[6, 4], [6, 5]], 'vier': [[6, 7], [6, 8], [6, 9], [6, 10]],
                          'sechs': [[7, 0], [7, 1],[7, 2], [7, 3], [7, 4]], 'acht': [[7, 7], [7, 8], [7, 9], [7, 10]],
                          'sieben': [[8, 0], [8, 1],[8, 2], [8, 3], [8, 4], [8, 5]], 'zwoelf': [[8, 6], [8, 7], [8, 8], [8, 9], [8, 10]],
                          'zehn': [[9, 0], [9, 1],[9, 2], [9, 3]], 'neun': [[9, 3], [9, 4], [9, 5], [9, 6]], 'uhr': [[9, 8], [9, 9], [9, 10]]}
        for row in range(1, 11):
            for col in range(1, 12):
                self.layout.itemAt(row, col).childItems()[0].setDefaultTextColor(QColor('#E0E0DD'))
        for wordToShow in timeToShow.split():
            if wordToShow in wordConversion:
                for letterpos in wordConversion[wordToShow]:
                    self.layout.itemAt(letterpos[0] + 1, letterpos[1] + 1).childItems()[0].setDefaultTextColor(Qt.black)
    
    def timeToString(self, init = False):
        timestring = 'es ist '
        currentTime = time.localtime()
        if currentTime.tm_sec and not init:
            return
        hourint = currentTime.tm_hour % 12
        minremainder = currentTime.tm_min % 5
        if not minremainder:
            self.layout.itemAt(0, 12).childItems()[0].setBrush(Qt.white)
            self.layout.itemAt(11, 12).childItems()[0].setBrush(Qt.white)
            self.layout.itemAt(11, 0).childItems()[0].setBrush(Qt.white)
            self.layout.itemAt(0, 0).childItems()[0].setBrush(Qt.white)
        if minremainder > 0:
            self.layout.itemAt(0, 0).childItems()[0].setBrush(Qt.black)
        if minremainder > 1:
            self.layout.itemAt(0, 12).childItems()[0].setBrush(Qt.black)
        if minremainder > 2:
            self.layout.itemAt(11, 12).childItems()[0].setBrush(Qt.black)
        if minremainder > 3:
            self.layout.itemAt(11, 0).childItems()[0].setBrush(Qt.black)
        if currentTime.tm_min > 24:
            hourint += 1
        hour = {0: 'zwoelf', 1: 'eins', 2: 'zwei', 3: 'drei', 4: 'vier', 5: 'fuenf', 6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun', 10: 'zehn', 11: 'elf'}
        if currentTime.tm_min in [0,1,2,3,4]:
            if hourint == 1:
                timestring += 'ein uhr'
            else:
                timestring += hour[hourint] + ' uhr'
        if currentTime.tm_min in [5,6,7,8,9]:
            timestring += 'fuenfmin nach ' + hour[hourint]
        if currentTime.tm_min in [10,11,12,13,14]:
            timestring += 'zehnmin nach ' + hour[hourint]
        if currentTime.tm_min in [15,16,17,18,19]:
            timestring += 'viertel nach ' + hour[hourint]
        if currentTime.tm_min in [20,21,22,23,24]:
            timestring += 'zwanzig nach ' + hour[hourint]
        if currentTime.tm_min in [25,26,27,28,29]:
            timestring += 'fuenfmin vor halb ' + hour[hourint]
        if currentTime.tm_min in [30,31,32,33,34]:
            timestring += 'halb ' + hour[hourint]
        if currentTime.tm_min in [35,36,37,38,39]:
            timestring += 'fuenfmin nach halb ' + hour[hourint]
        if currentTime.tm_min in [40,41,42,43,44]:
            timestring += 'zehnmin nach halb ' + hour[hourint]
        if currentTime.tm_min in [45,46,47,48,49]:
            timestring += 'dreibruch viertel ' + hour[hourint]
        if currentTime.tm_min in [50,51,52,53,54]:
            timestring += 'zehnmin vor ' + hour[hourint]
        if currentTime.tm_min in [55,56,57,58,59]:
            timestring += 'fuenfmin vor ' + hour[hourint]
        self.showWords(timestring)
        
if __name__ == '__main__':
    
    app = QApplication([])
    clock = ClockApp()
    clock.show()
    app.processEvents()
    minInterval = QTimer()
    scenesize = clock.scene.sceneRect()
    clock.resize(int(scenesize.width()) - 35, int(scenesize.height()) - 35)
    clock.timeToString(True)
    minInterval.timeout.connect(clock.timeToString)
    minInterval.start(1000)
    sys.exit(app.exec_())