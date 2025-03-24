#####################
# Python Calculator #
#####################

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QMenu, QMenuBar, QAction, QStatusBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import random
choosebackgroundcolors = [  "#9eeb8d", "#f0e37f", "#eb958d", "#ebc78d", "#8debac", "#8debe9", "#8db7eb",
                            "#968deb", "#e38deb", "#eb8dc3", "#696969", "#bdbdbd", "#2e2e2e"]
backgroundcolors = {"#9eeb8d": "#c1f0b6",
                    "#f0e37f": "#f0eab9",
                    "#eb958d": "#f5c4bf",
                    "#ebc78d": "#f2dbb6",
                    "#8debac": "#bdf0ce",
                    "#8debe9": "#b0e8e7",
                    "#8db7eb": "#b0cff5", 
                    "#968deb": "#aea7f2", 
                    "#e38deb": "#ecaef2",
                    "#eb8dc3": "#f5c1df",
                    "#696969": "#808080",
                    "#bdbdbd": "#dbdbdb", 
                    "#2e2e2e": "#454545"}

class MainWindow(QMainWindow):
    choosencolor = random.choice(choosebackgroundcolors)
    fonttype = "Arial"
    operators = [" + ", " - ", " / ", " x "]
    calculation = 0
    inputslist = []
    showinputs = []
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Calculator")
        self.setWindowIcon(QIcon("zero.ico"))
        self.setGeometry(700, 100, 600, 800)
        self.initUI()

    def initUI(self):
        self.one = QPushButton("1", self)
        self.two = QPushButton("2", self)
        self.three = QPushButton("3", self)
        self.four = QPushButton("4", self)
        self.five = QPushButton("5", self)
        self.six = QPushButton("6", self)
        self.seven = QPushButton("7", self)
        self.eight = QPushButton("8", self)
        self.nine = QPushButton("9", self)
        self.zero = QPushButton("0", self)
        self.minus = QPushButton("-", self)
        self.plus = QPushButton("+", self)
        self.multi = QPushButton("x", self)
        self.divide = QPushButton("/", self)
        self.equal = QPushButton("=", self)
        self.clear = QPushButton("cc", self)
        self.delete = QPushButton("del", self)
        self.dot = QPushButton(".", self)
        self.total = QLabel(self)
        self.inputs = QLabel(self)
        self.nummode = QPushButton("pos nums", self)
        self.settings = QMenu("Settings", self)
        self.background = QAction("Change background color", self)
        self.fontt = QAction("Change font style", self)
        self.quit = QAction("Quit", self)
        self.bar = QStatusBar(self)
        self.setStatusBar(self.bar)

        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)

        vbox = QVBoxLayout()
        vbox.addWidget(self.total)
        vbox.addWidget(self.inputs)
        centralwidget.setLayout(vbox)

        gbox = QGridLayout()
        gbox.addWidget(self.one, 2, 0)
        gbox.addWidget(self.two, 2, 1)
        gbox.addWidget(self.three, 2, 2)
        gbox.addWidget(self.four, 3, 0)
        gbox.addWidget(self.five, 3, 1)
        gbox.addWidget(self.six, 3, 2)
        gbox.addWidget(self.seven, 4, 0)
        gbox.addWidget(self.eight, 4, 1)
        gbox.addWidget(self.nine, 4, 2)
        gbox.addWidget(self.plus, 5, 0)
        gbox.addWidget(self.zero, 5, 1)
        gbox.addWidget(self.dot, 5, 2)
        gbox.addWidget(self.minus, 6, 0)
        gbox.addWidget(self.divide, 6, 1)
        gbox.addWidget(self.multi, 6, 2)
        vbox.addLayout(gbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.clear)
        hbox.addWidget(self.delete)
        vbox.addLayout(hbox)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.nummode)
        vbox2.addWidget(self.equal)
        vbox.addLayout(vbox2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.nummode)
        hbox2.addWidget(self.equal)
        vbox.addLayout(hbox2)

        mbar = QMenuBar()
        mbar.addMenu(self.settings)
        self.settings.addAction(self.background)
        self.settings.addAction(self.fontt)
        self.settings.addSeparator()
        self.settings.addAction(self.quit)
        self.setMenuBar(mbar)

        self.total.setAlignment(Qt.AlignCenter)
        self.inputs.setAlignment(Qt.AlignCenter)

        self.bar.clearMessage()

        self.inputs.setObjectName("inputs")
        self.one.setObjectName("one")
        self.two.setObjectName("two")
        self.three.setObjectName("three")
        self.four.setObjectName("four")
        self.five.setObjectName("five")
        self.six.setObjectName("six")
        self.seven.setObjectName("seven")
        self.eight.setObjectName("eight")
        self.nine.setObjectName("nine")
        self.zero.setObjectName("zero")
        self.plus.setObjectName("plus")
        self.minus.setObjectName("minus")
        self.divide.setObjectName("divide")
        self.multi.setObjectName("multi")
        self.nummode.setObjectName("nummode")
        self.delete.setObjectName("delete")
        self.clear.setObjectName("clear")
        self.equal.setObjectName("equal")
        self.dot.setObjectName("dot")
        self.SetStyles(self.fonttype)

    def SetStyles(self, font):
        self.setStyleSheet(
            "QWidget {"
                f"background-color: {self.choosencolor};"  
            "}"
            "QLabel {"
                "font-size: 50px;"
                "font-weight: bold;"
                f"font-family: {font};"
                f"background-color: {backgroundcolors[self.choosencolor]};"
                "border-radius: 20px;"
            "}"

            "QMenuBar {"
                f"background-color: {self.choosencolor};"
                "font-size: 20px;"
                f"font-family: {font};"
                "font-weight: bold;"
            "}"

            "QMenu {"
                f"background-color: {self.choosencolor};"
                "font-size: 17px;"
                f"font-family: {font};"
                "font-weight: bold;"
            "}"
                
            "QLabel#inputs {"
                "color: #7a6e23;"
            "}"
            
            "QPushButton {"
                "width: 100%;"
                "height: 50%;"
                "font-size: 40px;"
                "font-weight: bold;"
                f"font-family: {font};"
             """border: 10px solid;
                border-radius: 20px;
            }
                
            QPushButton#one {
                background-color: #5c5c5c;
            }
                
            QPushButton#one:hover {
                background-color: #8a8a8a;
                color: white;               
            }
                           
            QPushButton#two {
                background-color: #5c5c5c;
            }
                
            QPushButton#two:hover {
                background-color: #8a8a8a;
                color: white;
            }
            
            QPushButton#three {
                background-color: #5c5c5c;
            }
                
            QPushButton#three:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#four {
                background-color: #5c5c5c;
            }
                
            QPushButton#four:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#five {
                background-color: #5c5c5c;
            }
                
            QPushButton#five:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#six {
                background-color: #5c5c5c;
            }
                
            QPushButton#six:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#seven {
                background-color: #5c5c5c;
            }
                
            QPushButton#seven:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#eight {
                background-color: #5c5c5c;
            }
                
            QPushButton#eight:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#nine {
                background-color: #5c5c5c;
            }
                
            QPushButton#nine:hover {
                background-color: #8a8a8a;
                color: white;
            }
                           
            QPushButton#zero {
                background-color: #5c5c5c;
            }
                
            QPushButton#zero:hover {
                background-color: #8a8a8a;
                color: white;
            }

            QPushButton#dot {
                background-color: #5c5c5c;
            }
                
            QPushButton#dot:hover {
                background-color: #8a8a8a;
                color: white;
            }

            QPushButton#plus {
                background-color: #879923;
            }

            QPushButton#plus:hover {
                background-color: #b9cf40;
                color: white;
            }

            QPushButton#minus {
                background-color: #879923;
            }

            QPushButton#minus:hover {
                background-color: #b9cf40;
                color: white;
            }

            QPushButton#divide {
                background-color: #879923;
            }

            QPushButton#divide:hover {
                background-color: #b9cf40;
                color: white;
            }

            QPushButton#multi {
                background-color: #879923;
            }

            QPushButton#multi:hover {
                background-color: #b9cf40;
                color: white;
            }

            QPushButton#nummode {
                background-color: #528f1d;
            }

            QPushButton#nummode:hover {
                background-color: #7ac23c;
                color: white;
            }

            QPushButton#delete {
                background-color: #693a34;
            }

            QPushButton#delete:hover {
                background-color: #a86058;
                color: white;
            }
                           
            QPushButton#clear {
                background-color: #662222;               
            }
            
            QPushButton#clear:hover {
                background-color: #9c3a3a;
                color: white;               
            }
                           
            QPushButton#equal {
                background-color: #916927;               
            }
                           
            QPushButton#equal:hover {
                background-color: #c28e3a;
                color: white;               
            }
            """)

        self.delete.clicked.connect(self.delchar)
        self.clear.clicked.connect(self.clearchars)
        self.one.clicked.connect(self.getinputs)
        self.two.clicked.connect(self.getinputs)
        self.three.clicked.connect(self.getinputs)
        self.four.clicked.connect(self.getinputs)
        self.five.clicked.connect(self.getinputs)
        self.six.clicked.connect(self.getinputs)
        self.seven.clicked.connect(self.getinputs)
        self.eight.clicked.connect(self.getinputs)
        self.nine.clicked.connect(self.getinputs)
        self.zero.clicked.connect(self.getinputs)
        self.plus.clicked.connect(self.getinputs)
        self.minus.clicked.connect(self.getinputs)
        self.multi.clicked.connect(self.getinputs)
        self.divide.clicked.connect(self.getinputs)
        self.equal.clicked.connect(self.getresult)
        self.nummode.clicked.connect(self.NegativeNums)
        self.dot.clicked.connect(self.getinputs)
        self.background.triggered.connect(self.changebackground)
        self.fontt.triggered.connect(self.changefont)
        self.quit.triggered.connect(self.quitapp)

        self.disableoperators()
        self.delete.setDisabled(True)
        self.clear.setDisabled(True)
        self.dot.setDisabled(True)
    
    def changebackground(self):
        self.green = QPushButton("Green", self)
        self.yellow = QPushButton("Yellow", self)
        self.red = QPushButton("Red", self)
        self.orange = QPushButton("Orange", self)
        self.lime = QPushButton("Lime", self)
        self.blue = QPushButton("Blue", self)
        self.navyblue = QPushButton("Navy Blue", self)
        self.unknown = QPushButton("don't know", self)
        self.pink = QPushButton("Pink", self)
        self.magneta = QPushButton("Magneta", self)
        self.grey = QPushButton("Grey", self)
        self.white = QPushButton("White", self)
        self.black = QPushButton("Black", self)
        self.back = QPushButton("Back", self)

        backgroundsettingwidget = QWidget()
        self.setCentralWidget(backgroundsettingwidget)

        gbox = QGridLayout()
        gbox.addWidget(self.green, 0, 0)
        gbox.addWidget(self.yellow, 0, 1)
        gbox.addWidget(self.red, 0, 2)
        gbox.addWidget(self.orange, 1, 0)
        gbox.addWidget(self.lime, 1, 1)
        gbox.addWidget(self.blue, 1, 2)
        gbox.addWidget(self.navyblue, 2, 0)
        gbox.addWidget(self.unknown, 2, 1)
        gbox.addWidget(self.pink, 2, 2)
        gbox.addWidget(self.magneta, 3, 0)
        gbox.addWidget(self.grey, 3, 1)
        gbox.addWidget(self.white, 3, 2)
        gbox.addWidget(self.black, 4, 1)
        gbox.addWidget(self.back, 4, 2)
        backgroundsettingwidget.setLayout(gbox)

        self.changingprocess(self.choosencolor, self.fonttype)

        self.green.clicked.connect(self.changecolor)
        self.yellow.clicked.connect(self.changecolor)
        self.red.clicked.connect(self.changecolor)
        self.orange.clicked.connect(self.changecolor)
        self.lime.clicked.connect(self.changecolor)
        self.blue.clicked.connect(self.changecolor)
        self.navyblue.clicked.connect(self.changecolor)
        self.unknown.clicked.connect(self.changecolor)
        self.pink.clicked.connect(self.changecolor)
        self.magneta.clicked.connect(self.changecolor)
        self.grey.clicked.connect(self.changecolor)
        self.white.clicked.connect(self.changecolor)
        self.black.clicked.connect(self.changecolor)
        self.back.clicked.connect(self.goback)
    
    def changefont(self):
        self.timesnewroman = QPushButton("Times New Roman", self)
        self.arial = QPushButton("Arial", self)
        self.calibri = QPushButton("Calibri", self)
        self.adlam = QPushButton("ADLam Display", self)
        self.algerian = QPushButton("Algerian", self)
        self.bernard = QPushButton("Bernard MT Condensed", self)
        self.duster = QPushButton("Chalkduster", self)
        self.back = QPushButton("Back", self)
        self.icon = QLabel(self)
        self.pixmap = QPixmap("face.ico")
        self.pixmapresized = self.pixmap.scaled(150, 150, Qt.KeepAspectRatio)
        self.icon.setPixmap(self.pixmapresized)

        fontwidget = QWidget()
        self.setCentralWidget(fontwidget)

        gbox = QGridLayout()
        fontwidget.setLayout(gbox)
        gbox.addWidget(self.timesnewroman, 0, 0)
        gbox.addWidget(self.arial, 0, 1)
        gbox.addWidget(self.calibri, 0, 2)
        gbox.addWidget(self.adlam, 1, 0)
        gbox.addWidget(self.algerian, 1, 1)
        gbox.addWidget(self.bernard, 1, 2)
        gbox.addWidget(self.duster, 2, 1)
        gbox.addWidget(self.icon, 3, 0)
        gbox.addWidget(self.back, 3, 2)

        self.timesnewroman.setObjectName("roman")
        self.arial.setObjectName("arial")
        self.calibri.setObjectName("calibri")
        self.adlam.setObjectName("adlam")
        self.algerian.setObjectName("algerian")
        self.bernard.setObjectName("bernard")
        self.duster.setObjectName("duster")
        self.back.setObjectName("back")
        self.stylee(self.fonttype)
    
    def stylee(self, font):
        self.setStyleSheet(""
           "QMainWindow {"
              f"background-color: {self.choosencolor};"              
           "}"
           "QPushButton {"
                "width: 100%;"
                "height: 50%;"
                "font-size: 40px;"
                "font-weight: bold;"
                f"font-family: {font};"
                "border: 10px solid;"
                "border-radius: 20px;"
                "background-color: #deda68;"            
            "}"
                           
            "QPushButton:hover {"
                "background-color: #e3e08a;"
                "color: white;"               
           "}"

            "QMenuBar {"
                f"background-color: {self.choosencolor};"
                "font-size: 20px;"
                f"font-family: {font};"
                "font-weight: bold;"
            "}"

            "QMenu {"
                f"background-color: {self.choosencolor};"
                "font-size: 17px;"
                f"font-family: {font};"
                "font-weight: bold;"
            "}"

            "QStatusBar {"
                f"font-family: {font};"
            "}"
        )
        
        self.timesnewroman.clicked.connect(self.setfont)
        self.arial.clicked.connect(self.setfont)
        self.calibri.clicked.connect(self.setfont)
        self.adlam.clicked.connect(self.setfont)
        self.algerian.clicked.connect(self.setfont)
        self.bernard.clicked.connect(self.setfont)
        self.duster.clicked.connect(self.setfont)
        self.back.clicked.connect(self.goback)

    def fontchangedmassage(self, font):
        self.bar.showMessage(f"The text has been changed to '{font}'")
        
    def backgroundchangedmassage(self, newchoosencolor):
        self.bar.showMessage(f"The background has been changed to {newchoosencolor}")

    def setfont(self):
        clickedbutton = self.sender().text()
        match clickedbutton:
            case "Times New Roman":
                self.fonttype = "Times New Roman"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "Arial":
                self.fonttype = "Arial"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "Calibri":
                self.fonttype = "Calibri"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "ADLam Display":
                self.fonttype = "ADLam Display"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "Algerian":
                self.fonttype = "Algerian"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "Bernard MT Condensed":
                self.fonttype = "Bernard MT Condensed"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)
            case "Chalkduster":
                self.fonttype = "Chalkduster"
                self.stylee(self.fonttype)
                self.fontchangedmassage(self.fonttype)

    def goback(self):
        self.initUI()
        self.clearchars()
    
    def changecolor(self):
        color = self.sender().text()
        match color:
            case "Green":
                self.choosencolor = "#9eeb8d"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Green')
            case "Yellow":
                self.choosencolor = "#f0e37f"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Yellow')
            case "Red":
                self.choosencolor = "#eb958d"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Red')
            case "Orange":
                self.choosencolor = "#ebc78d"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Orange')
            case "Lime":
                self.choosencolor = "#8debac"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage(self.choosencolor)
            case "Blue":
                self.choosencolor = "#8debe9"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Blue')
            case "Navy Blue":
                self.choosencolor = "#8db7eb"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Navy Blue')
            case "don't know":
                self.choosencolor = "#968deb"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.bar.showMessage("I do not know what this color named")
            case "Pink":
                self.choosencolor = "#e38deb"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Pink')
            case "Magneta":
                self.choosencolor = "#eb8dc3"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Magneta')
            case "Grey":
                self.choosencolor = "#696969"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Grey')
            case "White":
                self.choosencolor = "#bdbdbd"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('White')
            case "Black":
                self.choosencolor = "#2e2e2e"
                self.changingprocess(self.choosencolor, self.fonttype)
                self.backgroundchangedmassage('Black')

    def changingprocess(self, newchoosencolor, font):
        self.green.setObjectName("green")
        self.yellow.setObjectName("yellow")
        self.red.setObjectName("red")
        self.orange.setObjectName("orange")
        self.lime.setObjectName("lime")
        self.blue.setObjectName("blue")
        self.navyblue.setObjectName("navyblue")
        self.unknown.setObjectName("unknown")
        self.pink.setObjectName("pink")
        self.magneta.setObjectName("magneta")
        self.grey.setObjectName("grey")
        self.white.setObjectName("white")
        self.black.setObjectName("black")
        self.back.setObjectName("back")
        self.setStyleSheet(""
           "MainWindow {"
           f"   background-color: {newchoosencolor};"
           "}" 
           ""
           "QMenuBar {"
           f"   background-color: {newchoosencolor};"
               "font-size: 20px;"
               f"font-family: {font};"
               "font-weight: bold;"
           "}"

           "QMenu {"
          f"    background-color: {newchoosencolor};"
               "font-size: 17px;"
               f"font-family: {font};"
               "font-weight: bold;"
            "}"
            
            "QPushButton {"
                "width: 100%;"
                "height: 70%;"
                "font-size: 40px;"
                "font-weight: bold;"
                f"font-family: {font};"
                "border: 10px solid;"
                "border-radius: 20px;"
            "}"

            "QStatusBar {"
                f"font-family: {font};"
            "}"
            """
            QPushButton#green {
                background-color: #9eeb8d;
            }
            
            QPushButton#green:hover {
                background-color: #c1f0b6;
                color: white;
            }

            QPushButton#yellow {
                background-color: #f0e37f;
            }

            QPushButton#yellow:hover {
                background-color: #f0eab9;
                color: white;
            }

            QPushButton#red {
                background-color: #eb958d;
            }

            QPushButton#red:hover {
                background-color: #f5c4bf;
                color: white;
            }

            QPushButton#orange {
                background-color: #ebc78d;
            }

            QPushButton#orange:hover {
                background-color: #ebc78d;
                color: white;
            }

            QPushButton#orange {
                background-color: #ebc78d;
            }

            QPushButton#orange:hover {
                background-color: #f2dbb6;
                color: white;
            }

            QPushButton#lime {
                background-color: #8debac;
            }

            QPushButton#lime:hover {
                background-color: #bdf0ce;
                color: white;
            }

            QPushButton#blue {
                background-color: #8debe9;
            }

            QPushButton#blue:hover {
                background-color: #b0e8e7;
                color: white;
            }

            QPushButton#navyblue {
                background-color: #8db7eb;
            }

            QPushButton#navyblue:hover {
                background-color: #b0cff5;
                color: white;
            }

            QPushButton#unknown {
                background-color: #968deb;
            }

            QPushButton#unknown:hover {
                background-color: #aea7f2;
                color: white;
            }

            QPushButton#pink {
                background-color: #e38deb;
            }

            QPushButton#pink:hover {
                background-color: #ecaef2;
                color: white;
            }

            QPushButton#magneta {
                background-color: #eb8dc3;
            }

            QPushButton#magneta:hover {
                background-color: #f5c1df;
                color: white;
            }

            QPushButton#white {
                background-color: #bdbdbd;
            }

            QPushButton#white:hover {
                background-color: #dbdbdb;
                color: white;
            }

            QPushButton#grey {
                background-color: #696969;
            }

            QPushButton#grey:hover {
                background-color: #808080;
                color: white;
            }

            QPushButton#black {
                background-color: #2e2e2e;
            }

            QPushButton#black:hover {
                background-color: #454545;
                color: white;
            }
            """
            "QPushButton#back:hover {"
                f"background-color: {backgroundcolors[self.choosencolor]};"
                "color: white;"
            "}"
            "")

    def quitapp(self):
        sys.exit()
    
    def setbuttons(self):
        if len(self.inputslist) == 0:
            self.delete.setDisabled(True)
            self.dot.setDisabled(True)
            self.disableoperators()
            self.enableNums()
            self.zero.setEnabled(True)
            if len(self.total.text()) == 0:
                self.clear.setDisabled(True)
        elif len(self.inputslist) == 30:
            self.disableNums()
            self.zero.setDisabled(True)
            self.disableoperators()
            self.dot.setDisabled(True)
            self.total.setStyleSheet("""
                font-size: 45px;
                color: #7a1d1d;
                """)
            self.total.setText("Max 30 character")
        else:
            self.delete.setEnabled(True)
            self.clear.setEnabled(True)
            if self.inputslist[-1] == "." and self.nummode.text() == "neg nums":
                self.disableNums()
                self.zero.setEnabled(True)
                self.disableoperators()
                self.dot.setDisabled(True)
            elif (self.inputslist[-1] == "." and self.nummode.text() == "pos nums") or self.inputslist[-1] in self.operators:
                self.enableNums()
                self.zero.setEnabled(True)
                self.disableoperators()
                self.dot.setDisabled(True)
            elif (int(self.inputslist[-1]) < 0 or int(self.inputslist[-1]) >= 0) and self.nummode.text() == "pos nums":
                self.enableNums()
                self.zero.setEnabled(True)
                self.enableoperators()
                self.dot.setEnabled(True)
                for i in range(len(self.inputslist) - 1, 0, -1):
                    if self.inputslist[i] not in self.operators:
                        if self.inputslist[i] == ".":
                            self.dot.setDisabled(True)
                            break
                    else:
                        break
            elif (int(self.inputslist[-1]) < 0 or int(self.inputslist[-1]) >= 0) and self.nummode.text() == "neg nums":
                self.disableNums()
                self.zero.setEnabled(True)
                self.enableoperators()
                self.dot.setEnabled(True)
                for i in range(len(self.inputslist) - 1, 0, -1):
                    if self.inputslist[i] not in self.operators:
                        if self.inputslist[i] == ".":
                            self.dot.setDisabled(True)
                            break
                    else:
                        break
        
    
    def PositiveNums(self):
        self.one.setText("1")
        self.two.setText("2")
        self.three.setText("3")
        self.four.setText("4")
        self.five.setText("5")
        self.six.setText("6")
        self.seven.setText("7")
        self.eight.setText("8")
        self.nine.setText("9")
        self.nummode.setText("pos nums")
        self.nummode.setStyleSheet("""
            QPushButton#nummode {
                background-color: #528f1d;
            }

            QPushButton#nummode:hover {
                background-color: #7ac23c;
                color: white;
            }
        """)
        self.setbuttons()
    
    def NegativeNums(self):
        if self.nummode.text() == "pos nums":
            self.one.setText("-1")
            self.two.setText("-2")
            self.three.setText("-3")
            self.four.setText("-4")
            self.five.setText("-5")
            self.six.setText("-6")
            self.seven.setText("-7")
            self.eight.setText("-8")
            self.nine.setText("-9")
            self.nummode.setText("neg nums")
            self.nummode.setStyleSheet("""
            QPushButton#nummode {
                background-color: #852b21;
            }

            QPushButton#nummode:hover {
                background-color: #c2493c;
                color: white;
            }
            """)
            self.setbuttons()
        elif self.nummode.text() == "neg nums":
            self.PositiveNums()
            self.setbuttons()

    def disableoperators(self):
        self.plus.setDisabled(True)
        self.minus.setDisabled(True)
        self.multi.setDisabled(True)
        self.divide.setDisabled(True)
        self.equal.setDisabled(True)
    
    def enableoperators(self):
        self.plus.setEnabled(True)
        self.minus.setEnabled(True)
        self.multi.setEnabled(True)
        self.divide.setEnabled(True)
        self.equal.setEnabled(True)
    
    def disableNums(self):
        self.one.setDisabled(True)
        self.two.setDisabled(True)
        self.three.setDisabled(True)
        self.four.setDisabled(True)
        self.five.setDisabled(True)
        self.six.setDisabled(True)
        self.seven.setDisabled(True)
        self.eight.setDisabled(True)
        self.nine.setDisabled(True)
    
    def enableNums(self):
        self.one.setEnabled(True)
        self.two.setEnabled(True)
        self.three.setEnabled(True)
        self.four.setEnabled(True)
        self.five.setEnabled(True)
        self.six.setEnabled(True)
        self.seven.setEnabled(True)
        self.eight.setEnabled(True)
        self.nine.setEnabled(True)

    def getinputs(self):
        inputted = self.sender().text()
        match inputted:
            case "1":
                self.inputslist.append("1")
                self.inputs.setText("".join(self.inputslist))
            case "2":
                self.inputslist.append("2")
                self.inputs.setText("".join(self.inputslist))
            case "3":
                self.inputslist.append("3")
                self.inputs.setText("".join(self.inputslist))
            case "4":
                self.inputslist.append("4")
                self.inputs.setText("".join(self.inputslist))
            case "5":
                self.inputslist.append("5")
                self.inputs.setText("".join(self.inputslist))
            case "6":
                self.inputslist.append("6")
                self.inputs.setText("".join(self.inputslist))
            case "7":
                self.inputslist.append("7")
                self.inputs.setText("".join(self.inputslist))
            case "8":
                self.inputslist.append("8")
                self.inputs.setText("".join(self.inputslist))
            case "9":
                self.inputslist.append("9")
                self.inputs.setText("".join(self.inputslist))
            case "0":
                self.inputslist.append("0")
                self.inputs.setText("".join(self.inputslist))
            case "-1":
                self.inputslist.append("-1")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-2":
                self.inputslist.append("-2")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-3":
                self.inputslist.append("-3")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-4":
                self.inputslist.append("-4")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-5":
                self.inputslist.append("-5")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-6":
                self.inputslist.append("-6")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-7":
                self.inputslist.append("-7")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-8":
                self.inputslist.append("-8")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case "-9":
                self.inputslist.append("-9")
                self.inputs.setText("".join(self.inputslist))
                self.PositiveNums()
            case ".":
                self.inputslist.append(".")
                self.inputs.setText("".join(self.inputslist))
            case "+":
                self.inputslist.append(" + ")
                self.inputs.setText("".join(self.inputslist))
            case "-":
                self.inputslist.append(" - ")
                self.inputs.setText("".join(self.inputslist))
            case "x":
                self.inputslist.append(" x ")
                self.inputs.setText("".join(self.inputslist))
            case "/":
                self.inputslist.append(" / ")
                self.inputs.setText("".join(self.inputslist))
        self.setbuttons()

    def delchar(self):
        try:
            del self.inputslist[-1]
            self.inputs.setText("".join(self.inputslist))
            self.setbuttons()
        except IndexError:
            pass
    
    def clearchars(self):
        self.inputslist.clear()
        self.inputs.clear()
        self.clear.setDisabled(True)
        self.setbuttons()
    
    def getresult(self):
        try:
            str1 = "".join(list(map(lambda x: " * " if x == " x " else x, self.inputslist))).split(" ")
            answer = eval("".join((list(map(lambda x: x + ".0" if x.startswith("0") and "." not in x and len(x) > 1 else x, str1)))))
            if answer == 0:
                self.total.setStyleSheet("color: black;")
                self.total.setText(str(answer))
            elif answer < 0:
                self.total.setStyleSheet("color: #7a1d1d;")
                self.total.setText(str(answer))
            elif answer > 0:
                self.total.setStyleSheet("color: #215415;")
                self.total.setText(str(answer))
        except ZeroDivisionError:
            self.total.setStyleSheet("""
                font-size: 35px;
                color: #7a1d1d;
                """)
            self.total.setText("Invalid calculation: ZeroDivisionError")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()