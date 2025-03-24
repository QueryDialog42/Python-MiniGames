from random import choice, randint
from sys import argv, exit
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

playerships = []
enemyships = []
score = []
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Amiral")
        self.setWindowIcon(QIcon("square2.ico"))
        self.setGeometry(300, 100, 0, 0)
        self.setFixedHeight(800)
        self.setFixedWidth(800)
        self.StartWidgetUI()

    def StartWidgetUI(self):
        self.startlabel = QLabel("GENCO\nAMIRAL", self)
        self.start = QPushButton("Start", self, clicked=lambda: self.ChooseShipsWidgetUI())
        self.quit = QPushButton("Quit", self, clicked=lambda: exit())

        startwidget = QWidget()
        self.setCentralWidget(startwidget)

        vbox = QVBoxLayout()
        startwidget.setLayout(vbox)
        vbox.addWidget(self.startlabel)
        vbox.addWidget(self.start)
        vbox.addWidget(self.quit)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        hbox.addWidget(self.start)
        hbox.addWidget(self.quit)

        self.startlabel.setAlignment(Qt.AlignCenter)

        self.start.setObjectName("start")
        self.quit.setObjectName("quit")
        self.setstyle(radius="20")

        self.start.setStyleSheet("""
            QPushButton#start {
                background-color: #7aeb7e; 
            }

            QPushButton#start:hover {
                background-color: #b0f5ae;
                color: white;
            }   
        """)

        self.quit.setStyleSheet("""
            QPushButton#quit {
                background-color:rgb(234, 92, 92);
            }

            QPushButton#quit:hover {
                background-color:rgb(236, 136, 136);
                color: white;
            }   
        """)
    
    def setstyle(self, background="#6fd1f7", font="Arial", height="50", width="50", font_size="40", border="10", radius="20", margin="10",
                button_color="#9bdff2"):
        self.setStyleSheet(""
            "MainWindow {"
                f"background-color: {background};"
            "}"

            "QPushButton {"
                f"font-family: {font};"
                f"font-size: {font_size}px;"
                "font-weight: bold;"
                f"height: {height}%;"
                f"width: {width}%;"
                f"border: {border}px solid;"
                f"border-radius: {radius}px;"
                f"margin-left: {margin}px;"
                f"margin-right: {margin}px;"
            "}"

            "QPushButton:hover {"
                f"background-color: {button_color};"
                "color: white;"
            "}"

            "QLabel {"
                f"font-family: {font};"
                f"font-size: {font_size}px;"
                "font-weight: bold;"
            "}"
         "")

    def ChooseShipsWidgetUI(self):
        self.playerlabel = QLabel(self)
        self.block1 = QPushButton(self, clicked=lambda: self.addship())
        self.block2 = QPushButton(self, clicked=lambda: self.addship())
        self.block3 = QPushButton(self, clicked=lambda: self.addship())
        self.block4 = QPushButton(self, clicked=lambda: self.addship())
        self.block5 = QPushButton(self, clicked=lambda: self.addship())
        self.block6 = QPushButton(self, clicked=lambda: self.addship())
        self.block7 = QPushButton(self, clicked=lambda: self.addship())
        self.block8 = QPushButton(self, clicked=lambda: self.addship())
        self.block9 = QPushButton(self, clicked=lambda: self.addship())
        self.block10 = QPushButton(self, clicked=lambda: self.addship())
        self.block11 = QPushButton(self, clicked=lambda: self.addship())
        self.block12 = QPushButton(self, clicked=lambda: self.addship())
        self.block13 = QPushButton(self, clicked=lambda: self.addship())
        self.block14 = QPushButton(self, clicked=lambda: self.addship())
        self.block15 = QPushButton(self, clicked=lambda: self.addship())
        self.block16 = QPushButton(self, clicked=lambda: self.addship())
        self.block17 = QPushButton(self, clicked=lambda: self.addship())
        self.block18 = QPushButton(self, clicked=lambda: self.addship())
        self.block19 = QPushButton(self, clicked=lambda: self.addship())
        self.block20 = QPushButton(self, clicked=lambda: self.addship())
        self.block21 = QPushButton(self, clicked=lambda: self.addship())
        self.block22 = QPushButton(self, clicked=lambda: self.addship())
        self.block23 = QPushButton(self, clicked=lambda: self.addship())
        self.block24 = QPushButton(self, clicked=lambda: self.addship())
        self.block25 = QPushButton(self, clicked=lambda: self.addship())
        self.block26 = QPushButton(self, clicked=lambda: self.addship())
        self.block27 = QPushButton(self, clicked=lambda: self.addship())
        self.block28 = QPushButton(self, clicked=lambda: self.addship())
        self.block29 = QPushButton(self, clicked=lambda: self.addship())
        self.block30 = QPushButton(self, clicked=lambda: self.addship())
        self.block31 = QPushButton(self, clicked=lambda: self.addship())
        self.block32 = QPushButton(self, clicked=lambda: self.addship())
        self.block33 = QPushButton(self, clicked=lambda: self.addship())
        self.block34 = QPushButton(self, clicked=lambda: self.addship())
        self.block35 = QPushButton(self, clicked=lambda: self.addship())
        self.block36 = QPushButton(self, clicked=lambda: self.addship())
        self.block37 = QPushButton(self, clicked=lambda: self.addship())
        self.block38 = QPushButton(self, clicked=lambda: self.addship())
        self.block39 = QPushButton(self, clicked=lambda: self.addship())
        self.block40 = QPushButton(self, clicked=lambda: self.addship())
        self.block41 = QPushButton(self, clicked=lambda: self.addship())
        self.block42 = QPushButton(self, clicked=lambda: self.addship())
        self.block43 = QPushButton(self, clicked=lambda: self.addship())
        self.block44 = QPushButton(self, clicked=lambda: self.addship())
        self.block45 = QPushButton(self, clicked=lambda: self.addship())
        self.block46 = QPushButton(self, clicked=lambda: self.addship())
        self.block47 = QPushButton(self, clicked=lambda: self.addship())
        self.block48 = QPushButton(self, clicked=lambda: self.addship())
        self.block49 = QPushButton(self, clicked=lambda: self.addship())
        self.block50 = QPushButton(self, clicked=lambda: self.addship())
        self.block51 = QPushButton(self, clicked=lambda: self.addship())
        self.block52 = QPushButton(self, clicked=lambda: self.addship())
        self.block53 = QPushButton(self, clicked=lambda: self.addship())
        self.block54 = QPushButton(self, clicked=lambda: self.addship())
        self.delete = QPushButton("Delete", self, clicked=lambda: self.deleteship())
        self.fight = QPushButton("Fight", self, clicked=lambda: self.GameWidgetUI())

        self.allblocks = {0: self.block1, 1: self.block2, 2: self.block3, 3: self.block4, 4: self.block5, 5: self.block6, 6: self.block7, 7: self.block8, 8: self.block9,
                  9: self.block10, 10: self.block11, 11: self.block12, 12: self.block13, 13: self.block14, 14: self.block15, 15: self.block16, 16: self.block17, 17: self.block18,
                  18: self.block19, 19: self.block20, 20: self.block21, 21: self.block22, 22: self.block23, 23: self.block24, 24: self.block25, 25: self.block26, 26: self.block27,
                  27: self.block28, 28: self.block29, 29: self.block30, 30: self.block31, 31: self.block32, 32: self.block33, 33: self.block34, 34: self.block35, 35: self.block36,
                  36: self.block37, 37: self.block38, 38: self.block39, 39: self.block40, 40: self.block41, 41: self.block42, 42: self.block43, 43: self.block44, 44: self.block45,
                  45: self.block46, 46: self.block47, 47: self.block48, 48: self.block49, 49: self.block50, 50: self.block51, 51: self.block52, 52: self.block53, 53: self.block54}

        self.fight.setDisabled(True)
        self.delete.setDisabled(True)

        chooseshipswidget = QWidget()
        self.setCentralWidget(chooseshipswidget)

        vbox = QVBoxLayout()
        chooseshipswidget.setLayout(vbox)
        vbox.addWidget(self.playerlabel)

        gbox = QGridLayout()
        vbox.addLayout(gbox)
        gbox.addWidget(self.block1, 0, 0)
        gbox.addWidget(self.block2, 0, 1)
        gbox.addWidget(self.block3, 0, 2)
        gbox.addWidget(self.block4, 0, 3)
        gbox.addWidget(self.block5, 0, 4)
        gbox.addWidget(self.block6, 0, 5)
        gbox.addWidget(self.block7, 1, 0)
        gbox.addWidget(self.block8, 1, 1)
        gbox.addWidget(self.block9, 1, 2)
        gbox.addWidget(self.block10, 1, 3)
        gbox.addWidget(self.block11, 1, 4)
        gbox.addWidget(self.block12, 1, 5)
        gbox.addWidget(self.block13, 2, 0)
        gbox.addWidget(self.block14, 2, 1)
        gbox.addWidget(self.block15, 2, 2)
        gbox.addWidget(self.block16, 2, 3)
        gbox.addWidget(self.block17, 2, 4)
        gbox.addWidget(self.block18, 2, 5)
        gbox.addWidget(self.block19, 3, 0)
        gbox.addWidget(self.block20, 3, 1)
        gbox.addWidget(self.block21, 3, 2)
        gbox.addWidget(self.block22, 3, 3)
        gbox.addWidget(self.block23, 3, 4)
        gbox.addWidget(self.block24, 3, 5)
        gbox.addWidget(self.block25, 4, 0)
        gbox.addWidget(self.block26, 4, 1)
        gbox.addWidget(self.block27, 4, 2)
        gbox.addWidget(self.block28, 4, 3)
        gbox.addWidget(self.block29, 4, 4)
        gbox.addWidget(self.block30, 4, 5)
        gbox.addWidget(self.block31, 5, 0)
        gbox.addWidget(self.block32, 5, 1)
        gbox.addWidget(self.block33, 5, 2)
        gbox.addWidget(self.block34, 5, 3)
        gbox.addWidget(self.block35, 5, 4)
        gbox.addWidget(self.block36, 5, 5)
        gbox.addWidget(self.block37, 6, 0)
        gbox.addWidget(self.block38, 6, 1)
        gbox.addWidget(self.block39, 6, 2)
        gbox.addWidget(self.block40, 6, 3)
        gbox.addWidget(self.block41, 6, 4)
        gbox.addWidget(self.block42, 6, 5)
        gbox.addWidget(self.block43, 7, 0)
        gbox.addWidget(self.block44, 7, 1)
        gbox.addWidget(self.block45, 7, 2)
        gbox.addWidget(self.block46, 7, 3)
        gbox.addWidget(self.block47, 7, 4)
        gbox.addWidget(self.block48, 7, 5)
        gbox.addWidget(self.block49, 8, 0)
        gbox.addWidget(self.block50, 8, 1)
        gbox.addWidget(self.block51, 8, 2)
        gbox.addWidget(self.block52, 8, 3)
        gbox.addWidget(self.block53, 8, 4)
        gbox.addWidget(self.block54, 8, 5)

        vbox.addWidget(self.delete)
        vbox.addWidget(self.fight)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        hbox.addWidget(self.delete)
        hbox.addWidget(self.fight)

        self.setstyle(radius="0", margin="25", font_size="30")

        self.delete.setObjectName("delete")
        self.fight.setObjectName("fight")
        self.delete.setStyleSheet("""
        QPushButton#delete {
            background-color: #c96767;
            border-radius: 20px;
        }

        QPushButton#delete:hover {
            background-color: #d98f8f;
            color: white;
        }
        """)

        self.fight.setStyleSheet("""
        QPushButton#fight {
            background-color: #e3a446;
            border-radius: 20px;
        }

        QPushButton#fight:hover {
            background-color: #e3b97b;
            color: white;
        }
        """)
    
        self.ChooseEnemeyShips()
        self.playerlabel.setText(f"Your {len(enemyships)} block of territory is under siege by enemy!\nLocate {len(enemyships)} to attack enemy.")
    
    def GameWidgetUI(self):
        self.block1_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block2_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block3_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block4_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block5_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block6_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block7_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block8_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block9_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block10_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block11_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block12_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block13_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block14_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block15_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block16_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block17_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block18_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block19_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block20_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block21_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block22_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block23_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block24_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block25_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block26_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block27_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block28_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block29_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block30_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block31_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block32_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block33_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block34_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block35_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block36_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block37_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block38_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block39_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block40_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block41_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block42_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block43_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block44_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block45_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block46_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block47_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block48_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block49_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block50_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block51_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block52_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block53_2 = QPushButton(self, clicked=lambda: self.attack())
        self.block54_2 = QPushButton(self, clicked=lambda: self.attack())

        self.allblocks_2 = {0: self.block1_2, 1: self.block2_2, 2: self.block3_2, 3: self.block4_2, 4: self.block5_2, 5: self.block6_2, 6: self.block7_2, 7: self.block8_2, 8: self.block9_2,
                  9: self.block10_2, 10: self.block11_2, 11: self.block12_2, 12: self.block13_2, 13: self.block14_2, 14: self.block15_2, 15: self.block16_2, 16: self.block17_2, 17: self.block18_2,
                  18: self.block19_2, 19: self.block20_2, 20: self.block21_2, 21: self.block22_2, 22: self.block23_2, 23: self.block24_2, 24: self.block25_2, 25: self.block26_2, 26: self.block27_2,
                  27: self.block28_2, 28: self.block29_2, 29: self.block30_2, 30: self.block31_2, 31: self.block32_2, 32: self.block33_2, 33: self.block34_2, 34: self.block35_2, 35: self.block36_2,
                  36: self.block37_2, 37: self.block38_2, 38: self.block39_2, 39: self.block40_2, 40: self.block41_2, 41: self.block42_2, 42: self.block43_2, 43: self.block44_2, 44: self.block45_2,
                  45: self.block46_2, 46: self.block47_2, 47: self.block48_2, 48: self.block49_2, 49: self.block50_2, 50: self.block51_2, 51: self.block52_2, 52: self.block53_2, 53: self.block54_2}

        maingamewidget = QWidget()
        self.setCentralWidget(maingamewidget)

        vbox = QVBoxLayout()
        maingamewidget.setLayout(vbox)
        vbox.addWidget(self.playerlabel)

        self.playerlabel.setText("Let's defeat your enemy!")

        gbox = QGridLayout()
        vbox.addLayout(gbox)
        gbox.addWidget(self.block1_2, 0, 0)
        gbox.addWidget(self.block2_2, 0, 1)
        gbox.addWidget(self.block3_2, 0, 2)
        gbox.addWidget(self.block4_2, 0, 3)
        gbox.addWidget(self.block5_2, 0, 4)
        gbox.addWidget(self.block6_2, 0, 5)
        gbox.addWidget(self.block7_2, 1, 0)
        gbox.addWidget(self.block8_2, 1, 1)
        gbox.addWidget(self.block9_2, 1, 2)
        gbox.addWidget(self.block10_2, 1, 3)
        gbox.addWidget(self.block11_2, 1, 4)
        gbox.addWidget(self.block12_2, 1, 5)
        gbox.addWidget(self.block13_2, 2, 0)
        gbox.addWidget(self.block14_2, 2, 1)
        gbox.addWidget(self.block15_2, 2, 2)
        gbox.addWidget(self.block16_2, 2, 3)
        gbox.addWidget(self.block17_2, 2, 4)
        gbox.addWidget(self.block18_2, 2, 5)
        gbox.addWidget(self.block19_2, 3, 0)
        gbox.addWidget(self.block20_2, 3, 1)
        gbox.addWidget(self.block21_2, 3, 2)
        gbox.addWidget(self.block22_2, 3, 3)
        gbox.addWidget(self.block23_2, 3, 4)
        gbox.addWidget(self.block24_2, 3, 5)
        gbox.addWidget(self.block25_2, 4, 0)
        gbox.addWidget(self.block26_2, 4, 1)
        gbox.addWidget(self.block27_2, 4, 2)
        gbox.addWidget(self.block28_2, 4, 3)
        gbox.addWidget(self.block29_2, 4, 4)
        gbox.addWidget(self.block30_2, 4, 5)
        gbox.addWidget(self.block31_2, 5, 0)
        gbox.addWidget(self.block32_2, 5, 1)
        gbox.addWidget(self.block33_2, 5, 2)
        gbox.addWidget(self.block34_2, 5, 3)
        gbox.addWidget(self.block35_2, 5, 4)
        gbox.addWidget(self.block36_2, 5, 5)
        gbox.addWidget(self.block37_2, 6, 0)
        gbox.addWidget(self.block38_2, 6, 1)
        gbox.addWidget(self.block39_2, 6, 2)
        gbox.addWidget(self.block40_2, 6, 3)
        gbox.addWidget(self.block41_2, 6, 4)
        gbox.addWidget(self.block42_2, 6, 5)
        gbox.addWidget(self.block43_2, 7, 0)
        gbox.addWidget(self.block44_2, 7, 1)
        gbox.addWidget(self.block45_2, 7, 2)
        gbox.addWidget(self.block46_2, 7, 3)
        gbox.addWidget(self.block47_2, 7, 4)
        gbox.addWidget(self.block48_2, 7, 5)
        gbox.addWidget(self.block49_2, 8, 0)
        gbox.addWidget(self.block50_2, 8, 1)
        gbox.addWidget(self.block51_2, 8, 2)
        gbox.addWidget(self.block52_2, 8, 3)
        gbox.addWidget(self.block53_2, 8, 4)
        gbox.addWidget(self.block54_2, 8, 5)

        self.initUI2()
        
    def initUI2(self):
        self.enemy = EnemyWindow()
        self.enemy.show()

    def addship(self):
        ship = list(self.allblocks.values()).index(self.sender())
        playerships.append(ship)
        self.allblocks[playerships[-1]].setStyleSheet("background-color: #3f9c25;")
        self.allblocks[playerships[-1]].setDisabled(True)
        self.setbutton()
    
    def deleteship(self):
        self.allblocks[playerships[-1]].setStyleSheet("background-color: #6fd1f7;")
        self.allblocks[playerships[-1]].setEnabled(True)
        playerships.remove(playerships[-1])
        self.setbutton()
    
    def setbutton(self):
        if len(playerships) == 0:
            self.delete.setDisabled(True)
            self.fight.setDisabled(True)
            for i in range(len(self.allblocks)):
                if i not in playerships:
                    self.allblocks[i].setEnabled(True)
        elif len(playerships) > 0 and len(playerships) < len(enemyships):
            self.delete.setEnabled(True)
            self.fight.setDisabled(True)
            for i in range(len(self.allblocks)):
                if i not in playerships:
                    self.allblocks[i].setEnabled(True)
        elif len(playerships) == len(enemyships):
            self.fight.setEnabled(True)
            for i in range(len(self.allblocks)):
                self.allblocks[i].setDisabled(True)
    
    def ChooseEnemeyShips(self):
        sides = ["up", "front"]
        self.limit = 53
        for i in range(6):
            choosenblock = randint(0, self.limit)
            if choosenblock not in enemyships:
                enemyships.append(choosenblock)
            else:
                i -= 1
                continue
            shiplong = randint(1, 3)
            side = choice(sides)
            try:
                if side == "front":
                    match shiplong:
                        case 1:
                            continue
                        case 2:
                            if choosenblock + 1 not in enemyships:
                                if choosenblock + 1 > self.limit:
                                    raise IndexError
                                enemyships.append(choosenblock + 1)
                            else:
                                continue
                        case 3:
                            if choosenblock + 1 not in enemyships and choosenblock + 2 not in enemyships:
                                if choosenblock + 1 > self.limit or choosenblock + 2 > self.limit:
                                    raise IndexError
                                enemyships.append(choosenblock + 1)
                                enemyships.append(choosenblock + 2)
                            else: continue
                elif side == "up":
                    match shiplong:
                        case 1:
                            continue
                        case 2:
                            if choosenblock + 6 not in enemyships:
                                if choosenblock + 6 > self.limit:
                                    raise IndexError
                                enemyships.append(choosenblock + 6)
                            else: continue
                        case 3:
                            if choosenblock + 6 not in enemyships and choosenblock + 12 not in enemyships:
                                if choosenblock + 6 > self.limit or choosenblock + 12 > self.limit:
                                    raise IndexError
                                enemyships.append(choosenblock + 6)
                                enemyships.append(choosenblock + 12)
                            else: continue
            except IndexError:
                continue
    
    def attack(self):
        
        access = self.getloseorwin()

        if access: 
            attackedblock = self.sender()
            attackblockindex = list(self.allblocks_2.values()).index(attackedblock)
            if attackblockindex in enemyships:
                enemyships.remove(attackblockindex)
                self.playerlabel.setStyleSheet("color: #128a48;")
                self.playerlabel.setText(f"You hit the part of enemy ship! {len(enemyships)} block remained.")
                attackedblock.setDisabled(True)
                attackedblock.setStyleSheet("background-color: red;")
            else:
                self.playerlabel.setText("You missed it!")
                self.playerlabel.setStyleSheet("color: #8a1226;")
                attackedblock.setDisabled(True)
                attackedblock.setStyleSheet("background-color: #3948ed;")
            
            if len(enemyships) == 0:
                score.append("win")
            else:
                EnemyWindow.enemyattack(self.enemy)
            
            self.getloseorwin()
    
    def getloseorwin(self):
        try:
            if score[0] == "win" or score[0] == "lose":
                self.close()
                try:
                    self.enemy.close()
                except AttributeError:
                    pass
                self.loseorwin = LoseOrWinWindow()
                self.loseorwin.show()
                return False
        except IndexError:
            return True

class EnemyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Amiral")
        self.setGeometry(1120, 550, 0, 0)
        self.setFixedHeight(350)
        self.setFixedWidth(350)
        self.EnemyUI()

    def EnemyUI(self):
        self.block1_3 = QPushButton(self)
        self.block2_3 = QPushButton(self)
        self.block3_3 = QPushButton(self)
        self.block4_3 = QPushButton(self)
        self.block5_3 = QPushButton(self)
        self.block6_3 = QPushButton(self)
        self.block7_3 = QPushButton(self)
        self.block8_3 = QPushButton(self)
        self.block9_3 = QPushButton(self)
        self.block10_3 = QPushButton(self)
        self.block11_3 = QPushButton(self)
        self.block12_3 = QPushButton(self)
        self.block13_3 = QPushButton(self)
        self.block14_3 = QPushButton(self)
        self.block15_3 = QPushButton(self)
        self.block16_3 = QPushButton(self)
        self.block17_3 = QPushButton(self)
        self.block18_3 = QPushButton(self)
        self.block19_3 = QPushButton(self)
        self.block20_3 = QPushButton(self)
        self.block21_3 = QPushButton(self)
        self.block22_3 = QPushButton(self)
        self.block23_3 = QPushButton(self)
        self.block24_3 = QPushButton(self)
        self.block25_3 = QPushButton(self)
        self.block26_3 = QPushButton(self)
        self.block27_3 = QPushButton(self)
        self.block28_3 = QPushButton(self)
        self.block29_3 = QPushButton(self)
        self.block30_3 = QPushButton(self)
        self.block31_3 = QPushButton(self)
        self.block32_3 = QPushButton(self)
        self.block33_3 = QPushButton(self)
        self.block34_3 = QPushButton(self)
        self.block35_3 = QPushButton(self)
        self.block36_3 = QPushButton(self)
        self.block37_3 = QPushButton(self)
        self.block38_3 = QPushButton(self)
        self.block39_3 = QPushButton(self)
        self.block40_3 = QPushButton(self)
        self.block41_3 = QPushButton(self)
        self.block42_3 = QPushButton(self)
        self.block43_3 = QPushButton(self)
        self.block44_3 = QPushButton(self)
        self.block45_3 = QPushButton(self)
        self.block46_3 = QPushButton(self)
        self.block47_3 = QPushButton(self)
        self.block48_3 = QPushButton(self)
        self.block49_3 = QPushButton(self)
        self.block50_3 = QPushButton(self)
        self.block51_3 = QPushButton(self)
        self.block52_3 = QPushButton(self)
        self.block53_3 = QPushButton(self)
        self.block54_3 = QPushButton(self)
        self.enemylabel = QLabel(self)

        self.allblocks_3 = {0: self.block1_3, 1: self.block2_3, 2: self.block3_3, 3: self.block4_3, 4: self.block5_3, 5: self.block6_3, 6: self.block7_3, 7: self.block8_3, 8: self.block9_3,
                  9: self.block10_3, 10: self.block11_3, 11: self.block12_3, 12: self.block13_3, 13: self.block14_3, 14: self.block15_3, 15: self.block16_3, 16: self.block17_3, 17: self.block18_3,
                  18: self.block19_3, 19: self.block20_3, 20: self.block21_3, 21: self.block22_3, 22: self.block23_3, 23: self.block24_3, 24: self.block25_3, 25: self.block26_3, 26: self.block27_3,
                  27: self.block28_3, 28: self.block29_3, 29: self.block30_3, 30: self.block31_3, 31: self.block32_3, 32: self.block33_3, 33: self.block34_3, 34: self.block35_3, 35: self.block36_3,
                  36: self.block37_3, 37: self.block38_3, 38: self.block39_3, 39: self.block40_3, 40: self.block41_3, 41: self.block42_3, 42: self.block43_3, 43: self.block44_3, 44: self.block45_3,
                  45: self.block46_3, 46: self.block47_3, 47: self.block48_3, 48: self.block49_3, 49: self.block50_3, 50: self.block51_3, 51: self.block52_3, 52: self.block53_3, 53: self.block54_3}
        self.limit2 = 53
        self.blockindexs = [i for i in range(0, self.limit2 + 1)]  

        gamewidget = QWidget()
        self.setCentralWidget(gamewidget)

        vbox = QVBoxLayout()
        gamewidget.setLayout(vbox)
        vbox.addWidget(self.enemylabel)
        
        gbox = QGridLayout()
        vbox.addLayout(gbox)
        gbox.addWidget(self.block1_3, 0, 0)
        gbox.addWidget(self.block2_3, 0, 1)
        gbox.addWidget(self.block3_3, 0, 2)
        gbox.addWidget(self.block4_3, 0, 3)
        gbox.addWidget(self.block5_3, 0, 4)
        gbox.addWidget(self.block6_3, 0, 5)
        gbox.addWidget(self.block7_3, 1, 0)
        gbox.addWidget(self.block8_3, 1, 1)
        gbox.addWidget(self.block9_3, 1, 2)
        gbox.addWidget(self.block10_3, 1, 3)
        gbox.addWidget(self.block11_3, 1, 4)
        gbox.addWidget(self.block12_3, 1, 5)
        gbox.addWidget(self.block13_3, 2, 0)
        gbox.addWidget(self.block14_3, 2, 1)
        gbox.addWidget(self.block15_3, 2, 2)
        gbox.addWidget(self.block16_3, 2, 3)
        gbox.addWidget(self.block17_3, 2, 4)
        gbox.addWidget(self.block18_3, 2, 5)
        gbox.addWidget(self.block19_3, 3, 0)
        gbox.addWidget(self.block20_3, 3, 1)
        gbox.addWidget(self.block21_3, 3, 2)
        gbox.addWidget(self.block22_3, 3, 3)
        gbox.addWidget(self.block23_3, 3, 4)
        gbox.addWidget(self.block24_3, 3, 5)
        gbox.addWidget(self.block25_3, 4, 0)
        gbox.addWidget(self.block26_3, 4, 1)
        gbox.addWidget(self.block27_3, 4, 2)
        gbox.addWidget(self.block28_3, 4, 3)
        gbox.addWidget(self.block29_3, 4, 4)
        gbox.addWidget(self.block30_3, 4, 5)
        gbox.addWidget(self.block31_3, 5, 0)
        gbox.addWidget(self.block32_3, 5, 1)
        gbox.addWidget(self.block33_3, 5, 2)
        gbox.addWidget(self.block34_3, 5, 3)
        gbox.addWidget(self.block35_3, 5, 4)
        gbox.addWidget(self.block36_3, 5, 5)
        gbox.addWidget(self.block37_3, 6, 0)
        gbox.addWidget(self.block38_3, 6, 1)
        gbox.addWidget(self.block39_3, 6, 2)
        gbox.addWidget(self.block40_3, 6, 3)
        gbox.addWidget(self.block41_3, 6, 4)
        gbox.addWidget(self.block42_3, 6, 5)
        gbox.addWidget(self.block43_3, 7, 0)
        gbox.addWidget(self.block44_3, 7, 1)
        gbox.addWidget(self.block45_3, 7, 2)
        gbox.addWidget(self.block46_3, 7, 3)
        gbox.addWidget(self.block47_3, 7, 4)
        gbox.addWidget(self.block48_3, 7, 5)
        gbox.addWidget(self.block49_3, 8, 0)
        gbox.addWidget(self.block50_3, 8, 1)
        gbox.addWidget(self.block51_3, 8, 2)
        gbox.addWidget(self.block52_3, 8, 3)
        gbox.addWidget(self.block53_3, 8, 4)
        gbox.addWidget(self.block54_3, 8, 5)

        self.enemylabel.setText("The enemy is ready to defeat you!")

        self.setstyle(font_size="17", height="20", width="20", border="5")
    
    def setstyle(self, background="#6fd1f7", font="Arial", height="50", width="50", font_size="40", border="10", radius="20", margin="10",
        button_color="#9bdff2"):
        self.setStyleSheet(""
            "QMainWindow {"
                f"background-color: {background};"
            "}"

            "QPushButton {"
                f"font-family: {font};"
                "font-weight: bold;"
                f"height: {height}%;"
                f"width: {width}%;"
                f"border: {border}px solid;"
                f"border-radius: {radius}px;"
                f"margin-left: {margin}px;"
                f"margin-right: {margin}px;"
            "}"

            "QPushButton:hover {"
                f"background-color: {button_color};"
                "color: white;"
            "}"

            "QLabel {"
                f"font-family: {font};"
                f"font-size: {font_size}px;"
                "font-weight: bold;"
            "}"
         "")

        for block in playerships:
            self.allblocks_3[block].setStyleSheet("background-color: #3f9c25;")
    
    def enemyattack(self):
            attackedblockindex = choice(self.blockindexs)
            if attackedblockindex in playerships:
                self.blockindexs.remove(attackedblockindex)
                playerships.remove(attackedblockindex)
                self.enemylabel.setText(f"Enemy hitted you! {len(playerships)} blocks remained.")
                self.enemylabel.setStyleSheet("color: #8a1226;")
                self.allblocks_3[attackedblockindex].setStyleSheet("background-color: purple;")
            else:
                self.enemylabel.setText("Enemy missed it!")
                self.enemylabel.setStyleSheet("color: #128a48;")
                self.allblocks_3[attackedblockindex].setStyleSheet("background-color: #3948ed;")
                self.blockindexs.remove(attackedblockindex)
            
            if len(playerships) == 0:
                score.append("lose")
                self.close()

class LoseOrWinWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Amiral")
        self.setGeometry(300, 100, 0, 0)
        self.setFixedHeight(800)
        self.setFixedWidth(800)
        self.chooseloseorwin()

    def chooseloseorwin(self):   
        if score[0] == "lose":
            self.loseUI()
        elif score[0] == "win":
            self.winUI()

    def setstyle(self, background="#6fd1f7", font="Arial", height="50", width="50", font_size="40", border="10", radius="20", margin="10",
        button_color="#9bdff2"):
        self.setStyleSheet(""
            "QMainWindow {"
                f"background-color: {background};"
            "}"

            "QPushButton {"
                f"font-family: {font};"
                "font-weight: bold;"
                f"font-size: {font_size}px;"
                f"height: {height}%;"
                f"width: {width}%;"
                f"border: {border}px solid;"
                f"border-radius: {radius}px;"
                f"margin-left: {margin}px;"
                f"margin-right: {margin}px;"
            "}"

            "QPushButton:hover {"
                f"background-color: {button_color};"
                "color: white;"
            "}"

            "QLabel {"
                f"font-family: {font};"
                f"font-size: {font_size}px;"
                "font-weight: bold;"
            "}"
         "")
    
    def loseUI(self):
        self.loselabel = QLabel("You lose!", self)
        self.restartbutton = QPushButton("Restart", self, clicked=lambda: self.restart())
        self.quit = QPushButton("Quit", self, clicked=lambda: exit())
        
        losewidget = QWidget()
        self.setCentralWidget(losewidget)

        vbox = QVBoxLayout()
        losewidget.setLayout(vbox)
        vbox.addWidget(self.loselabel)
        vbox.addWidget(self.restartbutton)
        vbox.addWidget(self.quit)

        self.loselabel.setAlignment(Qt.AlignCenter)

        self.setstyle(background="#e8667c", font_size="30")

        self.restartbutton.setObjectName("restart")
        self.quit.setObjectName("quit")
        self.restartbutton.setStyleSheet("""
            QPushButton#restart {
                background-color: #d9d95f;
            }

            QPushButton#restart:hover {
                background-color: #d9d98b;
                color: white;
            }
        """)
        self.quit.setStyleSheet("""
            QPushButton#quit {
                background-color:rgb(234, 92, 92);
            }

            QPushButton#quit:hover {
                background-color:rgb(236, 136, 136);
                color: white;
            }   
        """)
        self.loselabel.setStyleSheet("font-size: 70px;")

    def winUI(self):
        self.winlabel = QLabel("You win!", self)
        self.restartbutton = QPushButton("Restart", self, clicked=lambda: self.restart())
        self.quit = QPushButton("Quit", self, clicked=lambda: exit())

        winwidget = QWidget()
        self.setCentralWidget(winwidget)

        vbox = QVBoxLayout()
        winwidget.setLayout(vbox)
        vbox.addWidget(self.winlabel)
        vbox.addWidget(self.restartbutton)
        vbox.addWidget(self.quit)

        self.winlabel.setAlignment(Qt.AlignCenter)
        self.setstyle(background="#7ce35f", font_size="30")

        self.restartbutton.setObjectName("restart")
        self.quit.setObjectName("quit")
        self.restartbutton.setStyleSheet("""
            QPushButton#restart {
                background-color: #d9d95f;
            }

            QPushButton#restart:hover {
                background-color: #d9d98b;
                color: white;
            }
        """)
        self.quit.setStyleSheet("""
            QPushButton#quit {
                background-color:rgb(234, 92, 92);
            }

            QPushButton#quit:hover {
                background-color:rgb(236, 136, 136);
                color: white;
            }   
        """)
        self.winlabel.setStyleSheet("font-size: 70px;")

    def restart(self):
        playerships.clear()
        enemyships.clear()
        score.clear()
        self.close()
        self.main = MainWindow()
        self.main.ChooseShipsWidgetUI()
        self.main.show()

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()