######################
# Cronometer Program #
######################

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTime, QTimer

class Cronometer(QWidget):
    isrunning = False
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Cronometer")
        self.setWindowIcon(QIcon("digital.png"))
        self.setGeometry(700, 300, 500, 600)
        self.timelabel = QLabel("00:00:00.000", self)
        self.massage = QLabel("Welcome to Genco Cronometer!", self)
        self.button = QPushButton("start", self)
        self.restartbutton = QPushButton("restarted", self)
        self.restartbutton.setDisabled(True)
        self.quitbutton = QPushButton("quit", self)
        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0, 0)
        self.initUI()
    
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.massage)
        vbox.addWidget(self.timelabel)
        vbox.addWidget(self.button)
        vbox.addWidget(self.restartbutton)
        vbox.addWidget(self.quitbutton)
        self.setLayout(vbox)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.restartbutton)
        hbox.addWidget(self.quitbutton)
        vbox.addLayout(hbox) # !!

        self.timelabel.setAlignment(Qt.AlignCenter)
        self.massage.setAlignment(Qt.AlignCenter)
        self.button.setObjectName("button")
        self.restartbutton.setObjectName("restartbutton")
        self.quitbutton.setObjectName("quit")
        self.massage.setObjectName("massage")
        self.timelabel.setObjectName("timelabel")
        self.setStyleSheet("""
            Cronometer {
               background-color: #aaf0ed;            
            }
                           
            QLabel#timelabel {
                font-size: 150px;
                font-family: Arial;
                background-color: #c8f7f5;
                border-radius: 50px;
            }
            
            QLabel#massage {
                font-size: 70px;
            }
            QPushButton {
                font-size: 60px;
                font-family: Arial;
                border: 10px solid;
                border-radius: 20px;
            }
                           
            QPushButton#button {
                background-color: #95eda3;
            }
            
            QPushButton#restartbutton {
                background-color: #def099;
            }
                           
            QPushButton#quit {
                background-color: red;
            }
        """)

        self.button.clicked.connect(self.onclicked)
        self.restartbutton.clicked.connect(self.onclicked)
        self.quitbutton.clicked.connect(self.onclicked)
        
        self.timer.timeout.connect(self.displaytime)

    def displaytime(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        miliseconds = self.time.msec()
        self.timelabel.setText(f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:03}")
        self.updatetime()
    
    def updatetime(self):
        self.time = self.time.addMSecs(1) # +1 miliseconds

    def onclicked(self):
        clicked = self.sender() 
        if clicked == self.button:
            if self.isrunning == False:
                self.isrunning = True 
                self.button.setText("stop")
                self.massage.setText("Cronometer started...")
                self.button.setStyleSheet("background-color: #f76d6d;")
                self.restartbutton.setText("restart")
                self.restartbutton.setDisabled(True)
                self.timer.start()
                self.displaytime()
            else:
                self.timer.stop()
                self.isrunning = False
                self.restartbutton.setDisabled(False)
                self.button.setText("start")
                self.massage.setText("Cronometer stoped!")
                self.button.setStyleSheet("background-color: #95eda3;")
        elif clicked == self.restartbutton:
            self.timelabel.setText("00:00:00.000")
            self.time = QTime(0, 0, 0, 0)
            self.restartbutton.setText("restarted")
            self.massage.setText("Cronometer restarted.")
            self.restartbutton.setDisabled(True)
        elif clicked == self.quitbutton:
            exit()

if __name__ == "__main__":
    app = QApplication(argv)
    window = Cronometer()
    window.show()
    exit(app.exec_())