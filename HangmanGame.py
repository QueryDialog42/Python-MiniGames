################
# Hangman Game #
################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QIcon
import random
from email.message import EmailMessage
import smtplib

hangman_art = {
    0:  "   \n"
        "   \n"
        "   \n",
    
    1:  " o \n"
        "   \n"
        "   \n",
    
    2:  " o \n"
        " | \n"
        "   \n",
    
    3:  " o \n"
        "/|\n"
        "   \n",
    
    4:  " o \n"
        " /|\\\n"
        "   \n",

    5:  " o \n"
        " /|\\\n"
        "/  \n",
    
    6:  ":-(\n"
        " /|\\\n"
        " / \\",
    
    7: ":-)\n"
        "/|\\\n"
        "/ \\"
}

class MainWindow(QMainWindow):
    words = ["apple", "orange", "strawberry", "banana", "kiwi", "carrot", "pie", "mortal kombat", "doctor", "oxygen", "glass", "sun",
    "brain", "person", "lahmacun", "hamburger", "chicken", "mandalina", "moon", "earth", "mars", "jupiter", "computer", "telephone",
    "jungle", "katastrophe", "book", "hammer", "dog", "cat", "fish", "goat", "call of duty", "spagetti", "soldier", "gun", "dad", "mom", "son",
    "brother", "sister", "uncle", "pen", "chess", "school", "business", "food", "mouse", "notebook", "bag", "sock"]
    choosenword = random.choice(words)

    wrong = 0
    ingame = False
    startblanks = list(map(lambda x: "_" if x != " " else " ", choosenword))
    guessedletterlist = []
    guessedwordlist = []
    rightletters = []
    start_screen = True
    message_sent = False
    sentmessage = []
    sentaddress = []
    sentapppass = []
    sentsubject = []

    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 500)
        self.setWindowTitle("Genco Hangman")
        self.setWindowIcon(QIcon("face.ico"))
        self.initUI()

    def initUI(self):
        self.hellolabel = QLabel("|-- GENCO HANGMAN --|", self)
        self.helloman = QLabel(hangman_art[7], self)
        self.start = QPushButton("Start", self)
        self.main = QPushButton("Main", self)
        self.quit = QPushButton("Quit", self)

        self.helloman.setObjectName("man")
        self.hellolabel.setObjectName("label")
        self.start.setObjectName("start")
        self.quit.setObjectName("quit")
        self.main.setObjectName("main")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #fbffa6;
            }
            QLineEdit {
                border: 10px solid;
                border-radius: 20px;
            }
                 
            QLabel {
                font-weight: bold;
                font-family: Arial;
            }               
            
            QLabel#man {
                font-size: 80px;
            }
            
            QLabel#label {
                font-size: 100px;              
            }
                           
            QPushButton {
                font-family: Arial;
                font-weight: bold;
                font-size: 45px;
                border: 10px solid;
                border-radius: 20px;
                margin: 10px;
            }
            
            QPushButton#start {
                background-color: #8aeb8a;
                width: 100%;
                height: 100%;
            }
            
            QPushButton#start:hover {
                background-color: #04AA6D;
                color: white;
            }
            
            QPushButton#quit {
                background-color: #f08989;
                width: 100%;
                height: 100%;  
            }
            
            QPushButton#quit:hover {
                background-color: #f44336;
                color: white;
            }
            
            QPushButton#main {
                background-color: #8ee0f5;
                width: 100%;
                height: 100%;                
           }
                
            QPushButton#main:hover {
                background-color: #66b1c4;
                color: white; 
            }
            """)

        start_widget = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.helloman)
        vbox.addWidget(self.hellolabel)
        vbox.addWidget(self.start)
        vbox.addWidget(self.quit)
        vbox.addWidget(self.main)
        start_widget.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start)
        hbox.addWidget(self.quit)
        hbox.addWidget(self.main)
        vbox.addLayout(hbox)

        self.hellolabel.setAlignment(Qt.AlignCenter)
        self.helloman.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(start_widget)

        self.quit.clicked.connect(self.QuitGame)
        self.start.clicked.connect(self.RestartGame)
        self.main.clicked.connect(self.MainPage)
    
    def MainPage(self):
        self.text = QTextEdit(self)
        self.man = QLabel(hangman_art[7], self)
        self.thanks = QLabel(self)
        self.back = QPushButton("Back", self)
        self.send = QPushButton("Send", self)
        self.timer = QTimer(self)
        self.timelabel = QLabel(self)
        self.address = QLineEdit(self)
        self.apppass = QLineEdit(self)
        self.subject = QLineEdit(self)

        link = "https://myaccount.google.com/u/0/apppasswords?continue=https://myaccount.google.com/u/1/?hl%3Den%26utm_source%3DOGB%26utm_medium%3Dact%26gar%3DWzEyMF0&rapt=AEjHL4NPHsAZ3JVgL1M_0Ksx83BZJYp4Z2ssEa498YyYTF-EFue4Lrhe7IAhR1D2t0LfuYPDJwS45UrHmfTxd95s9LXTWHD-UT_Ew0G4WOwYifwm90QJWc8&pageId=none"
        self.hint = QLabel(f'You can create an app password from <a href="{link}">here.</a><br>Please do not leave space in app password!')
        self.hint.setOpenExternalLinks(True)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        vbox = QVBoxLayout()
        main_widget.setLayout(vbox)
        vbox.addWidget(self.man)
        vbox.addWidget(self.thanks)
        vbox.addWidget(self.address)
        vbox.addWidget(self.apppass)
        vbox.addWidget(self.subject)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        hbox.addWidget(self.address)
        hbox.addWidget(self.apppass)

        vbox.addWidget(self.hint)
        vbox.addWidget(self.subject)
        vbox.addWidget(self.text)
        vbox.addWidget(self.timelabel)
        vbox.addWidget(self.back)

        hbox = QHBoxLayout()
        hbox.addWidget(self.back)
        hbox.addWidget(self.send)
        vbox.addLayout(hbox)
        
        self.text.setAcceptRichText(True)
        self.text.setPlaceholderText("Write something to us! :-)")
        self.text.setLineWrapColumnOrWidth(200)

        self.man.setAlignment(Qt.AlignCenter)
        self.timelabel.setAlignment(Qt.AlignCenter)
        self.thanks.setAlignment(Qt.AlignCenter)
        self.hint.setAlignment(Qt.AlignRight)

        self.text.setObjectName("text")
        self.man.setObjectName("man")
        self.thanks.setObjectName("thanks")
        self.back.setObjectName("back")
        self.timelabel.setObjectName("timelabel")
        self.send.setObjectName("send")
        self.subject.setObjectName("subject")
        self.hint.setObjectName("hint")
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #abe6f5;
                }

                QLabel {
                    font-weight: bold;
                    font-family: Arial;
                }
                           
                QLabel#hint {
                    font-weight: bold;
                    font-family: Arial;
                    font-size: 20px;
                    margin-right: 85px;        
                }

                QLineEdit {
                    background-color: #abe6f5;
                    font-weight: bold;
                    font-family: Arial;
                    font-size: 26px;
                    border: 10px solid;
                    border-radius: 20px;
                    margin: 10px;
                    margin-left: 30px;
                    margin-right: 30px;
                    width: 60%;
                    height: 60%; 
                }

                QPushButton {
                    font-family: Arial;
                    font-weight: bold;
                    font-size: 45px;
                    border: 10px solid;
                    border-radius: 20px;
                    margin: 10px;
                    width: 100%;
                    height: 100%; 
                }

                QLabel#man {
                    font-size: 80px;
                    margin-left: 300px;
                    margin-right: 300px;
                }

                QLabel#timelabel {
                    font-size: 30px;           
                }
                QTextEdit#text {
                    background-color: #abe6f5;
                    height: 100%;
                    width: 100%;
                    font-size: 30px;
                    font-family: Arial;
                    font-weight: bold;
                    border: 10px solid;
                    border-radius: 20px;
                    margin-left: 30px;
                    margin-right: 30px;
                }
                
                QPushButton#back {
                    background-color: #fbffa6;
                    margin-right: 30px;
                    margin-left: 30px;         
                }
                
                QPushButton#back:hover {
                    background-color: #c4b366;
                    color: white;
                }
                
                QPushButton#send {
                    background-color: #ef9af5;
                    margin-right: 30px;
                    margin-left: 30px;         
                }
                
                QPushButton#send:hover {
                    background-color: #ae54b8;
                    color: white;
                }
                
                QLabel#thanks {
                    font-size: 40px;
                }
                """)

        self.timer.timeout.connect(self.updatetime)
        self.timer.start(1000)
        self.updatetime()
        self.back.clicked.connect(self.Back)
        self.send.clicked.connect(self.Send)

        self.subject.setAlignment(Qt.AlignCenter)
        
        self.subject.setPlaceholderText("set your subject here")
        self.address.setPlaceholderText("youraddress@gmail.com")
        self.apppass.setPlaceholderText("App Password")

        if self.message_sent:
            self.text.setPlainText(self.sentmessage[0])
            self.apppass.setText(self.sentapppass[0])
            self.subject.setText(self.sentsubject[0])
            self.address.setText(self.sentaddress[0])
            self.text.setDisabled(True)
            self.send.setDisabled(True)
            self.address.setDisabled(True)
            self.subject.setDisabled(True)
            self.apppass.setDisabled(True)
            self.man.setText(hangman_art[7])
            self.thanks.setText("The man already thanked for your message!")
            self.thanks.setStyleSheet("color: #3d7d34;")

    def Send(self):
        blanksexist = False
        if len(self.text.toPlainText()) < 20:
            self.man.setText(hangman_art[6])
            self.thanks.setText("Please enter a text longer than 20 charachter.")
            self.thanks.setStyleSheet("color: #c75d46;")
        else:
            if self.address.text() == "" or self.apppass.text() == "":
                blanksexist = True
            gameaddress = "gencohangman@gmail.com"
            msg = EmailMessage()
            msg["Subject"] = self.subject.text()
            msg["From"] = self.address.text()
            msg["To"] = gameaddress
            msg.set_content(self.text.toPlainText())
            try:
                if blanksexist == True:
                    raise smtplib.SMTPException
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(self.address.text(), self.apppass.text())
                    smtp.send_message(msg)
                    self.sentaddress.append(self.address.text())
                    self.sentsubject.append(self.subject.text())
                    self.sentapppass.append(self.apppass.text())
                    self.sentmessage.append(self.text.toPlainText())  
                    self.text.setDisabled(True)
                    self.send.setDisabled(True)
                    self.address.setDisabled(True)
                    self.subject.setDisabled(True)
                    self.apppass.setDisabled(True)
                    self.man.setText(hangman_art[7])
                    self.thanks.setText("The man thanks you for your message!")
                    self.thanks.setStyleSheet("color: #3d7d34;")
                    self.message_sent = True
            except smtplib.SMTPException:
                if blanksexist == True:
                    self.man.setText(hangman_art[6])
                    self.thanks.setText("Please fill the address and app password blanks")
                    self.thanks.setStyleSheet("color: #c75d46;")
                else:
                    self.man.setText(hangman_art[6])
                    self.thanks.setText("Something went wrong while sending the message.\nPlease check your email address and app password")
                    self.thanks.setStyleSheet("color: #c75d46;")
                blanksexist = False
            
    def Back(self):
        self.timer.stop()
        self.initUI()

    def updatetime(self):
        now = QTime.currentTime().toString("hh:mm:ss")
        self.timelabel.setText(now)
        self.timelabel.setStyleSheet("color: #4fabc2;")

    def QuitGame(self):
        sys.exit()

    def GameStarted(self):
        self.hangman = QLabel(hangman_art[self.wrong], self)
        self.input = QLineEdit(self)
        self.blanks = QLabel(" ".join(self.startblanks), self)
        self.button = QPushButton("Guess", self)
        self.warning = QLabel(self)
        self.guessedletters = QLabel(f"Guessed letters: {" ".join(self.guessedletterlist)}", self)
        self.guessedwords = QLabel(f"Guessed words: {" ".join(self.guessedwordlist)}", self)

        self.input.setPlaceholderText("Enter a letter or word")
        self.hangman.setObjectName("hangman")
        self.blanks.setObjectName("blanks")
        self.button.setObjectName("button")
        self.warning.setObjectName("warning")
        self.input.setObjectName("input")
        self.guessedletters.setObjectName("guessedletters")
        self.guessedwords.setObjectName("guessedwords")
        self.setStyleSheet("""
            QLineEdit {
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
            }
                 
            QLabel {
                font-weight: bold;
                font-family: Arial;
            }
            
            QPushButton {
                font-family: Arial;
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
                margin: 30px;
            }
                           
            QLabel#hangman {
                font-size: 80px;            
            }
            
            QLabel#blanks {
                font-size: 60px; 
            }
            
            QLabel#warning {
                font-size: 40px;
                color: #e34236;
            }

            QPushButton#button {
                width: 200%;
                height: 70%;
                font-size: 25px;
                background-color: #f3ff52;          
            }
                
            QPushButton#button:hover {
                background-color: #b8b154;
                color: white;            
            }
            
            QLineEdit#input {
                width: 80%;
                height: 70%;
                font-size: 25px;
                background-color: #f3ff52;
                margin-left: 20px;
            }
            
            QLabel#guessedletters {
                font-size: 25px;
                margin-left: 40px;
            }
            
            QLabel#guessedwords {
                font-size: 25px;
                margin-left: 40px;               
            }
            
            QMainWindow {
                background-color: #fbffa6;
            }
            """)  
        game_widget = QWidget()

        vbox = QVBoxLayout()
        vbox.addWidget(self.hangman)
        vbox.addWidget(self.blanks)
        vbox.addWidget(self.warning)
        vbox.addWidget(self.input)
        vbox.addWidget(self.button)
        game_widget.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.input)
        hbox.addWidget(self.button)
        vbox.addLayout(hbox)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.guessedletters)
        vbox2.addWidget(self.guessedwords)
        vbox.addLayout(vbox2)

        self.hangman.setAlignment(Qt.AlignCenter)
        self.blanks.setAlignment(Qt.AlignCenter)
        self.warning.setAlignment(Qt.AlignCenter)
        self.input.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(game_widget)

        self.button.clicked.connect(self.control)
    
    def won(self):
        self.youwon = QLabel("YOU WON!", self)
        self.yihu = QLabel(f"Yihu! You save the man.\n\nYou found the word '{self.choosenword}'", self)
        self.restart = QPushButton("Restart", self)
        self.quit = QPushButton("Quit", self)
        self.hanged = QLabel(hangman_art[7], self)
        self.main = QPushButton("Main", self)

        won_widget = QWidget()

        vbox = QVBoxLayout()
        vbox.addWidget(self.hanged)
        vbox.addWidget(self.youwon)
        vbox.addWidget(self.yihu)
        vbox.addWidget(self.restart)
        vbox.addWidget(self.quit)
        vbox.addWidget(self.main)
        won_widget.setLayout(vbox)

        self.hanged.setAlignment(Qt.AlignCenter)
        self.youwon.setAlignment(Qt.AlignCenter)
        self.yihu.setAlignment(Qt.AlignCenter)

        self.youwon.setObjectName("youwon")
        self.yihu.setObjectName("yihu")
        self.restart.setObjectName("restart")
        self.quit.setObjectName("quit")
        self.hanged.setObjectName("hanged")
        self.main.setObjectName("main")
        self.hanged.setObjectName("hanged")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #8bd16b;
            }

            QPushButton {
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
                width: 80%;
                height: 60%;
                margin: 10px;
                margin-left: 120px;
                margin-right: 120px;
            }

            QLabel {
                font-family: Arial;
                font-weight: bold;
            }

            QPushButton#restart {
                background-color: #f3ff52;
                margin-top: 30px;
            }
            
            QPushButton#restart:hover {
                background-color: #c4b366;
                color: white;
            }

            QPushButton#quit {
                background-color: #f08989;
            }
            
            QPushButton#quit:hover {
                background-color: #f44336;
                color: white;
            }
            
            QPushButton#main {
                background-color: #8ee0f5;       
            }
            
            QPushButton#main:hover {
                background-color: #66b1c4;
                color: white; 
            }

            QLabel#hanged {
                font-size: 60px;
            }

             QLabel#youwon {
                font-size: 60px;
            }

            QLabel#yihu {
                font-size: 30px;
            }
                
            QLabel#hanged {
                font-size: 80px;               
            }
            """)

        self.restart.clicked.connect(self.RestartGame)
        self.quit.clicked.connect(self.QuitGame)
        self.main.clicked.connect(self.MainPage)

        self.setCentralWidget(won_widget)

    def lose(self):
        self.youlose = QLabel("YOU LOSE!", self)
        self.oh = QLabel(f"Oh! The man has been hanged.\n\nThe answer was '{self.choosenword}'", self)
        self.restart = QPushButton("Restart", self)
        self.quit = QPushButton("Quit", self)
        self.main = QPushButton("Main", self)
        self.hanged = QLabel(hangman_art[6], self)

        lose_widget = QWidget()

        vbox = QVBoxLayout()
        vbox.addWidget(self.hanged) 
        vbox.addWidget(self.youlose)
        vbox.addWidget(self.oh)
        vbox.addWidget(self.restart)
        vbox.addWidget(self.quit)
        vbox.addWidget(self.main)
        lose_widget.setLayout(vbox)

        self.hanged.setAlignment(Qt.AlignCenter)
        self.youlose.setAlignment(Qt.AlignCenter)
        self.oh.setAlignment(Qt.AlignCenter)

        self.hanged.setObjectName("hanged")
        self.youlose.setObjectName("youlose")
        self.oh.setObjectName("oh")
        self.restart.setObjectName("restart")
        self.quit.setObjectName("quit")
        self.main.setObjectName("main")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #cc6f68;
            }

            QPushButton {
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
                width: 80%;
                height: 60%;
                margin: 10px;
                margin-left: 120px;
                margin-right: 120px;
            }

            QLabel {
                font-family: Arial;
                font-weight: bold;
            }

            QPushButton#restart {
                background-color: #f3ff52;
                margin-top: 30px; 
            }
            
            QPushButton#restart:hover {
                background-color: #c4b366;
                color: white;
            }

            QPushButton#quit {
                background-color: #f08989;
            }
            
            QPushButton#quit:hover {
                background-color: #f44336;
                color: white;
            }
            
            QPushButton#main {
                background-color: #8ee0f5;       
            }
            
            QPushButton#main:hover {
                background-color: #66b1c4;
                color: white; 
            }

            QLabel#hanged {
                font-size: 80px;
            }

            QLabel#youlose {
                font-size: 60px;
            }

            QLabel#oh {
                font-size: 30px;
            }
        """)

        self.restart.clicked.connect(self.RestartGame)
        self.quit.clicked.connect(self.QuitGame)
        self.main.clicked.connect(self.MainPage)

        self.setCentralWidget(lose_widget)
    
    def RestartGame(self):
        self.choosenword = random.choice(self.words)
        self.wrong = 0
        self.founded = 0
        self.startblanks = list(map(lambda x: "_" if x != " " else " ", self.choosenword))
        self.guessedletterlist = []
        self.guessedwordlist = []
        self.rightletters = []
        self.GameStarted()

    def control(self):
        guess = self.input.text().lower()
        indexs = []
        if len(guess) == 1:
            if guess in self.choosenword and guess not in self.guessedletterlist and guess not in self.rightletters:
                i = 0
                self.rightletters.append(guess)
                self.warning.setText(" ")
                for x in self.choosenword:
                    if x == guess:
                        indexs.append(i)
                        i += 1
                        self.setStyleSheet("""
                            QLineEdit {
                                font-weight: bold;
                                border: 10px solid;
                                border-radius: 20px;
                            }
                            
                            QLabel {
                                font-weight: bold;
                                font-family: Arial;
                            }
                        
                            QPushButton {
                                font-family: Arial;
                                font-weight: bold;
                                border: 10px solid;
                                border-radius: 20px;
                                margin: 30px;
                            }
                                    
                            QLabel#hangman {
                                font-size: 80px;            
                            }
                            
                            QLabel#blanks {
                                font-size: 60px; 
                            }
                        
                            QLabel#warning {
                                font-size: 40px;
                                color: #e34236;
                            }

                            QPushButton#button {
                                width: 200%;
                                height: 70%;
                                font-size: 22px;
                                background-color: #f3ff52;          
                            }
                                        
                            QPushButton#button:hover {
                                background-color: #b8b154;
                                color: white;            
                            }
                            
                            QLineEdit#input {
                                width: 100%;
                                height: 70%;
                                font-size: 25px;
                                background-color: #f3ff52;
                                margin-left: 20px; 
                            }
                            
                            QLabel#guessedletters {
                                font-size: 25px;
                                margin-left: 40px;
                            }
                        
                            QLabel#guessedwords {
                                font-size: 25px;
                                margin-left: 40px;               
                            }
                        
                            QMainWindow {
                                background-color: #95f28d;
                            }
                            """)
                    elif x == " " or x != guess:
                        i += 1
            elif guess in self.guessedletterlist:
                self.warning.setText(f"'{guess}' is already guessed!")
            elif guess in self.rightletters:
                self.warning.setText(f"'{guess}' is already in word...")
            else:
                self.wrong += 1
                self.setStyleSheet("""
                    QLineEdit {
                        font-weight: bold;
                        border: 10px solid;
                        border-radius: 20px;
                    }
                 
                    QLabel {
                        font-weight: bold;
                        font-family: Arial;
                    }
            
                    QPushButton {
                        font-family: Arial;
                        font-weight: bold;
                        border: 10px solid;
                        border-radius: 20px;
                        margin: 30px;
                    }
                                
                    QLabel#hangman {
                        font-size: 80px;            
                    }
                    
                    QLabel#blanks {
                        font-size: 60px; 
                    }
            
                    QLabel#warning {
                        font-size: 40px;
                        color: #e34236;
                    }

                    QPushButton#button {
                        width: 200%;
                        height: 70%;
                        font-size: 22px;
                        background-color: #f3ff52;          
                    }
                            
                    QPushButton#button:hover {
                        background-color: #b8b154;
                        color: white;            
                    }
                    
                    QLineEdit#input {
                        width: 100%;
                        height: 70%;
                        font-size: 25px;
                        background-color: #f3ff52;
                        margin-left: 20px; 
                    }
            
                    QLabel#guessedletters {
                        font-size: 25px;
                        margin-left: 40px;
                    }
                    
                    QLabel#guessedwords {
                        font-size: 25px;
                        margin-left: 40px;               
                    }
                    
                    QMainWindow {
                        background-color: #f28d8d;
                    }
                    """)
                if self.wrong == 6:
                    self.lose()
                else:
                    self.warning.setText(" ")
                    self.guessedletterlist.append(guess)
                    self.guessedletters.setText(f"Guessed letters: {" ".join(self.guessedletterlist)}")
            for i in indexs:
                self.startblanks[i] = guess
                if "_" not in self.startblanks:
                    self.lose()
            self.blanks.setText(" ".join(self.startblanks))
            self.hangman.setText(hangman_art[self.wrong])
        elif len(guess) > 1:
            if guess == self.choosenword:
                self.warning.setText(" ")
                self.won()
            elif guess != self.choosenword and guess in self.guessedwordlist:
                self.warning.setText(f"'{guess}' is already guessed!")
            else:
                self.wrong += 1
                self.setStyleSheet("""
                    QLineEdit {
                        font-weight: bold;
                        border: 10px solid;
                        border-radius: 20px;
                    }
                 
                    QLabel {
                        font-weight: bold;
                        font-family: Arial;
                    }
            
                    QPushButton {
                        font-family: Arial;
                        font-weight: bold;
                        border: 10px solid;
                        border-radius: 20px;
                        margin: 30px;
                    }
                                
                    QLabel#hangman {
                        font-size: 80px;            
                    }
                    
                    QLabel#blanks {
                        font-size: 60px; 
                    }
            
                    QLabel#warning {
                        font-size: 40px;
                        color: #e34236;
                    }

                    QPushButton#button {
                        width: 200%;
                        height: 70%;
                        font-size: 22px;
                        background-color: #f3ff52;          
                    }
                            
                    QPushButton#button:hover {
                        background-color: #b8b154;
                        color: white;            
                    }
                    
                    QLineEdit#input {
                        width: 100%;
                        height: 70%;
                        font-size: 25px;
                        background-color: #f3ff52;
                        margin-left: 20px; 
                    }
            
                    QLabel#guessedletters {
                        font-size: 25px;
                        margin-left: 40px;
                    }
                    
                    QLabel#guessedwords {
                        font-size: 25px;
                        margin-left: 40px;               
                    }
                    
                    QMainWindow {
                        background-color: #f28d8d;
                    }
                    """)
                if self.wrong == 6:
                    self.lose()
                else:
                    self.warning.setText(" ")
                    self.guessedwordlist.append(guess)
                    self.guessedwords.setText(f"Guessed words: {" ".join(self.guessedwordlist)}")
                    self.hangman.setText(hangman_art[self.wrong])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    