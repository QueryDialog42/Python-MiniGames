#################
# Digital Clock #
#################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QWidget):
    clock_running = True
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.button = QPushButton("Stop", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Genco Digital Clock")
        self.setWindowIcon(QIcon("digital.png"))
        self.timer = QTimer(self)
        self.setGeometry(700, 300, 600, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        
        self.time_label.setObjectName("time_label")
        self.button.setObjectName("button")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            DigitalClock {
                background-color: #33322d;
            }

            QLabel#time_label {
                font-size: 150px;
                color: #ffec70;
                
            }
            
            QPushButton#button {
                font-size: 100px;
                border: 10px solid;
                border-radius: 20px;
                background-color: #ff7e75;               
            }
        """)

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        digit_font = QFont(font_family, 150)
        self.time_label.setFont(digit_font)
        self.button.setFont(digit_font)

        self.button.clicked.connect(self.button_changed)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # miliseconds
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)
    
    def button_changed(self):
        if self.clock_running == True:
            self.timer.stop()
            self.button.setText("Start")
            self.button.setStyleSheet("background-color: #95fa8c;")
            self.clock_running = False
        else:
            self.timer.start(1000)
            self.button.setText("Stop")
            self.button.setStyleSheet("background-color: #ff7e75;")
            self.clock_running = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())