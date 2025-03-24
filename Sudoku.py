from sys import argv, exit
from random import randint, choice
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QGridLayout, QGroupBox, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genco Sudoku")
        self.setWindowIcon(QIcon("sudoku.ico"))
        self.setGeometry(700, 300, 600, 500)
        self.startPageUI()
    
    def startPageUI(self):
        startwidget = QWidget()
        self.setCentralWidget(startwidget)

        self.start = QPushButton("start", clicked=lambda: self.Difficulty())
        self.quit = QPushButton("quit", clicked=lambda: exit())
        self.label = QLabel("Genco\nSudoku")

        self.label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        startwidget.setLayout(vbox)
        vbox.addWidget(self.label)
        vbox.addWidget(self.start)
        vbox.addWidget(self.quit)

        self.start.setObjectName("start")
        self.quit.setObjectName("quit")
        self.setStyleSheet("""
            MainWindow {
                background-color: #a3f7ba;               
            }
                
            QPushButton {
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
                margin-left: 30px;
                margin-right: 30px;
                height: 50px;               
            }
                           
            QPushButton#start {
                background-color: #8ce670;               
            }
        
            QPushButton#start:hover {
                background-color: #bfed8e;
                color: white;                
            }
                
            QPushButton#quit {
                background-color: #e67086;               
            }

            QPushButton#quit:hover {
                background-color: #ed8ea0;
                color: white;        
            }          
                           
            QLabel {            
                font-size: 40px;
                font-family: Arial;
                font-weight: bold;               
            }
        """)

    def Difficulty(self):
        diffwidget = QWidget()
        self.setCentralWidget(diffwidget)

        self.level = 0

        self.difflabel = QLabel("Choose difficulty")
        self.easy = QPushButton("Easy (30 hint)", clicked=lambda: self.setDifficulty())
        self.normal = QPushButton("Normal (20 hint)", clicked=lambda: self.setDifficulty())
        self.hard = QPushButton("Hard (10 hint)", clicked=lambda: self.setDifficulty())
        self.insane = QPushButton("Insane (No hint)", clicked=lambda: self.setDifficulty())

        self.difflabel.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        diffwidget.setLayout(vbox)
        vbox.addWidget(self.difflabel)
        vbox.addWidget(self.easy)
        vbox.addWidget(self.normal)
        vbox.addWidget(self.hard)
        vbox.addWidget(self.insane)

        self.easy.setObjectName("easy")
        self.normal.setObjectName("normal")
        self.hard.setObjectName("hard")
        self.insane.setObjectName("insane")
        self.setStyleSheet("""
            MainWindow {
                background-color: #a3f7ba;               
            }
                
            QPushButton {
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
                border: 10px solid;
                border-radius: 20px;
                margin-left: 30px;
                margin-right: 30px;
                height: 50px;               
            }

            QLabel {
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
            }

            QPushButton#easy {
                background-color: #7ce051;
            }

            QPushButton#easy:hover {
                background-color: #a4ed85;
                color: white;
            }

            QPushButton#normal {
                background-color: #edb753;
            }

            QPushButton#normal:hover {
                background-color: #e8c179;
                color: white;
            }

            QPushButton#hard {
                background-color: #e88079;
            }

            QPushButton#hard:hover {
                background-color: #eb9c96;
                color: white;
            }

            QPushButton#insane {
                background-color: #e368dd;
            }

            QPushButton#insane:hover {
                background-color: #e38fdf;
                color: white;
            }
        """)
    
    def setDifficulty(self):
        if self.sender().text() == "Easy (30 hint)":
            self.level = 1
            self.initUI(self.level)
        elif self.sender().text() == "Normal (20 hint)":
            self.level = 2
            self.initUI(self.level)
        elif self.sender().text() == "Hard (10 hint)":
            self.level = 3
            self.initUI(self.level)
        elif self.sender().text() == "Insane (No hint)":
            self.level = 4
            self.initUI(self.level)
    
    def initUI(self, level):
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        self.control = QPushButton("Control", clicked=lambda: self.checkblocks())
        self.cleartable = QPushButton("Clear", clicked=lambda: self.clearboard())
        self.level = level

        self.lines = [[QLineEdit() for _ in range(9)] for _ in range(9)]

        for lists in self.lines:
            for line in lists:
                line.setFixedHeight(60)
                line.setFixedWidth(60)
                line.setMaxLength(1)
                line.setAlignment(Qt.AlignCenter)

        self.cleartable.setObjectName("clear")
        self.control.setObjectName("control")
        self.setStyleSheet("""
            MainWindow {
                background-color: #fadf7d;                   
            }
                
            QLineEdit {
                border: 5px solid;
                border-radius: 7px;
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
                background-color: #f7f48d;
                color: black;
                text-align: center;
            }
            
            QPushButton#control {
                background-color: #90f060;
                border: 5px solid;
                border-radius: 7px;
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;                 
            }
                
            QPushButton#control:hover {
                background-color: #98f294;
                color: white;
            }
                           
            QPushButton#clear {
                background-color: #f06060;
                border: 5px solid;
                border-radius: 7px;
                font-size: 30px;
                font-family: Arial;
                font-weight: bold;
            }
                           
            QPushButton#clear:hover {
                background-color: #f29494;
                color: white;               
            }
                
            QGroupBox {
                border: 0px;               
            }
        """)
        
        vbox = QVBoxLayout()
        centralwidget.setLayout(vbox)

        grid = QGridLayout()
        vbox.addLayout(grid)

        self.group1 = QGroupBox()
        gbox = QGridLayout()
        self.group1.setLayout(gbox)

        gbox.addWidget(self.lines[0][0], 0, 0)
        gbox.addWidget(self.lines[0][1], 0, 1)
        gbox.addWidget(self.lines[0][2], 0, 2)
        gbox.addWidget(self.lines[1][0], 1, 0)
        gbox.addWidget(self.lines[1][1], 1, 1)
        gbox.addWidget(self.lines[1][2], 1, 2)
        gbox.addWidget(self.lines[2][0], 2, 0)
        gbox.addWidget(self.lines[2][1], 2, 1)
        gbox.addWidget(self.lines[2][2], 2, 2)

        self.group1lines = [self.lines[0][0], self.lines[0][1], self.lines[0][2],
                            self.lines[1][0], self.lines[1][1], self.lines[1][2],
                            self.lines[2][0], self.lines[2][1], self.lines[2][2]]

        self.group2 = QGroupBox()
        gbox = QGridLayout()
        self.group2.setLayout(gbox)

        gbox.addWidget(self.lines[0][3], 0, 0)
        gbox.addWidget(self.lines[0][4], 0, 1)
        gbox.addWidget(self.lines[0][5], 0, 2)
        gbox.addWidget(self.lines[1][3], 1, 0)
        gbox.addWidget(self.lines[1][4], 1, 1)
        gbox.addWidget(self.lines[1][5], 1, 2)
        gbox.addWidget(self.lines[2][3], 2, 0)
        gbox.addWidget(self.lines[2][4], 2, 1)
        gbox.addWidget(self.lines[2][5], 2, 2)

        self.group2lines = [self.lines[0][3], self.lines[0][4], self.lines[0][5],
                            self.lines[1][3], self.lines[1][4], self.lines[1][5],
                            self.lines[2][3], self.lines[2][4], self.lines[2][5]]

        self.group3 = QGroupBox()
        gbox = QGridLayout()
        self.group3.setLayout(gbox)

        gbox.addWidget(self.lines[0][6], 0, 0)
        gbox.addWidget(self.lines[0][7], 0, 1)
        gbox.addWidget(self.lines[0][8], 0, 2)
        gbox.addWidget(self.lines[1][6], 1, 0)
        gbox.addWidget(self.lines[1][7], 1, 1)
        gbox.addWidget(self.lines[1][8], 1, 2)
        gbox.addWidget(self.lines[2][6], 2, 0)
        gbox.addWidget(self.lines[2][7], 2, 1)
        gbox.addWidget(self.lines[2][8], 2, 2)

        self.group3lines = [self.lines[0][6], self.lines[0][7], self.lines[0][8],
                            self.lines[1][6], self.lines[1][7], self.lines[1][8],
                            self.lines[2][6], self.lines[2][7], self.lines[2][8]]

        self.group4 = QGroupBox()
        gbox = QGridLayout()
        self.group4.setLayout(gbox)

        gbox.addWidget(self.lines[3][0], 0, 0)
        gbox.addWidget(self.lines[3][1], 0, 1)
        gbox.addWidget(self.lines[3][2], 0, 2)
        gbox.addWidget(self.lines[4][0], 1, 0)
        gbox.addWidget(self.lines[4][1], 1, 1)
        gbox.addWidget(self.lines[4][2], 1, 2)
        gbox.addWidget(self.lines[5][0], 2, 0)
        gbox.addWidget(self.lines[5][1], 2, 1)
        gbox.addWidget(self.lines[5][2], 2, 2)

        self.group4lines = [self.lines[3][0], self.lines[3][1], self.lines[3][2],
                            self.lines[4][0], self.lines[4][1], self.lines[4][2],
                            self.lines[5][0], self.lines[5][1], self.lines[5][2]]

        self.group5 = QGroupBox()
        gbox = QGridLayout()
        self.group5.setLayout(gbox)

        gbox.addWidget(self.lines[3][3], 0, 0)
        gbox.addWidget(self.lines[3][4], 0, 1)
        gbox.addWidget(self.lines[3][5], 0, 2)
        gbox.addWidget(self.lines[4][3], 1, 0)
        gbox.addWidget(self.lines[4][4], 1, 1)
        gbox.addWidget(self.lines[4][5], 1, 2)
        gbox.addWidget(self.lines[5][3], 2, 0)
        gbox.addWidget(self.lines[5][4], 2, 1)
        gbox.addWidget(self.lines[5][5], 2, 2)

        self.group5lines = [self.lines[3][3], self.lines[3][4], self.lines[3][5],
                            self.lines[4][3], self.lines[4][4], self.lines[4][5],
                            self.lines[5][3], self.lines[5][4], self.lines[5][5]]

        self.group6 = QGroupBox()
        gbox = QGridLayout()
        self.group6.setLayout(gbox)

        gbox.addWidget(self.lines[3][6], 0, 0)
        gbox.addWidget(self.lines[3][7], 0, 1)
        gbox.addWidget(self.lines[3][8], 0, 2)
        gbox.addWidget(self.lines[4][6], 1, 0)
        gbox.addWidget(self.lines[4][7], 1, 1)
        gbox.addWidget(self.lines[4][8], 1, 2)
        gbox.addWidget(self.lines[5][6], 2, 0)
        gbox.addWidget(self.lines[5][7], 2, 1)
        gbox.addWidget(self.lines[5][8], 2, 2)

        self.group6lines = [self.lines[3][6], self.lines[3][7], self.lines[3][8],
                            self.lines[4][6], self.lines[4][7], self.lines[4][8],
                            self.lines[5][6], self.lines[5][7], self.lines[5][8]]

        self.group7 = QGroupBox()
        gbox = QGridLayout()
        self.group7.setLayout(gbox)

        gbox.addWidget(self.lines[6][0], 0, 0)
        gbox.addWidget(self.lines[6][1], 0, 1)
        gbox.addWidget(self.lines[6][2], 0, 2)
        gbox.addWidget(self.lines[7][0], 1, 0)
        gbox.addWidget(self.lines[7][1], 1, 1)
        gbox.addWidget(self.lines[7][2], 1, 2)
        gbox.addWidget(self.lines[8][0], 2, 0)
        gbox.addWidget(self.lines[8][1], 2, 1)
        gbox.addWidget(self.lines[8][2], 2, 2)

        self.group7lines = [self.lines[6][0], self.lines[6][1], self.lines[6][2],
                            self.lines[7][0], self.lines[7][1], self.lines[7][2],
                            self.lines[8][0], self.lines[8][1], self.lines[8][2]]

        self.group8 = QGroupBox()
        gbox = QGridLayout()
        self.group8.setLayout(gbox)

        gbox.addWidget(self.lines[6][3], 0, 0)
        gbox.addWidget(self.lines[6][4], 0, 1)
        gbox.addWidget(self.lines[6][5], 0, 2)
        gbox.addWidget(self.lines[7][3], 1, 0)
        gbox.addWidget(self.lines[7][4], 1, 1)
        gbox.addWidget(self.lines[7][5], 1, 2)
        gbox.addWidget(self.lines[8][3], 2, 0)
        gbox.addWidget(self.lines[8][4], 2, 1)
        gbox.addWidget(self.lines[8][5], 2, 2)

        self.group8lines = [self.lines[6][3], self.lines[6][4], self.lines[6][5],
                            self.lines[7][3], self.lines[7][4], self.lines[7][5],
                            self.lines[8][3], self.lines[8][4], self.lines[8][5]]

        self.group9 = QGroupBox()
        gbox = QGridLayout()
        self.group9.setLayout(gbox)

        gbox.addWidget(self.lines[6][6], 0, 0)
        gbox.addWidget(self.lines[6][7], 0, 1)
        gbox.addWidget(self.lines[6][8], 0, 2)
        gbox.addWidget(self.lines[7][6], 1, 0)
        gbox.addWidget(self.lines[7][7], 1, 1)
        gbox.addWidget(self.lines[7][8], 1, 2)
        gbox.addWidget(self.lines[8][6], 2, 0)
        gbox.addWidget(self.lines[8][7], 2, 1)
        gbox.addWidget(self.lines[8][8], 2, 2)

        self.group9lines = [self.lines[6][6], self.lines[6][7], self.lines[6][8],
                            self.lines[7][6], self.lines[7][7], self.lines[7][8],
                            self.lines[8][6], self.lines[8][7], self.lines[8][8]]

        grid.addWidget(self.group1, 0, 0)
        grid.addWidget(self.group2, 0, 1)
        grid.addWidget(self.group3, 0, 2)
        grid.addWidget(self.group4, 1, 0)
        grid.addWidget(self.group5, 1, 1)
        grid.addWidget(self.group6, 1, 2)
        grid.addWidget(self.group7, 2, 0)
        grid.addWidget(self.group8, 2, 1)
        grid.addWidget(self.group9, 2, 2)

        self.groups = [ self.group1lines, self.group2lines, self.group3lines,
                        self.group4lines, self.group5lines, self.group6lines,
                        self.group7lines, self.group8lines, self.group9lines]

        vbox.addWidget(self.control)
        vbox.addWidget(self.cleartable)

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        hbox.addWidget(self.control)
        hbox.addWidget(self.cleartable) 

        self.createsudokuboard()
    
    def checkblocks(self):
        wrongnumbers = []
        self.emptyline = False
        for row in range(9):
            rownumbers = []
            samenumbers = []
            for col in range(9):
                if self.lines[row][col].text().isdigit() == False:
                    self.lines[row][col].clear()
                elif self.lines[row][col].text() == "":
                    self.lines[row][col].setStyleSheet("background-color: #f7f48d;")
                    self.emptyline = True
                elif self.lines[row][col].text() not in rownumbers:
                    if self.lines[row][col].isEnabled():
                        self.lines[row][col].setStyleSheet("background-color: #a3f7ba;")
                    rownumbers.append(self.lines[row][col].text())
                else:
                    samenumbers.append(self.lines[row][col].text())
            for col in range(9):
                if self.lines[row][col].isEnabled():
                    if self.lines[row][col].text() in samenumbers:
                        self.lines[row][col].setStyleSheet("background-color: #f7aea3;")
                        wrongnumbers.append(self.lines[row][col])
        
        for row in range(9):
            colnumbers = []
            samenumbers = []
            for col in range(9):                
                if self.lines[col][row].text() == "":
                    self.lines[col][row].setStyleSheet("background-color: #f7f48d;")
                    self.emptyline = True
                elif self.lines[col][row].text() not in colnumbers and self.lines[col][row] not in wrongnumbers:
                    if self.lines[col][row].isEnabled():
                        self.lines[col][row].setStyleSheet("background-color: #a3f7ba;")
                    colnumbers.append(self.lines[col][row].text())
                else:
                    samenumbers.append(self.lines[col][row].text())
            for col in range(9):
                if self.lines[col][row].text() in samenumbers:
                    if self.lines[col][row].isEnabled(): 
                        self.lines[col][row].setStyleSheet("background-color: #f7aea3;")
                        wrongnumbers.append((self.lines[col][row]))
        
        for group in self.groups:
            groupnumbers = []
            samenumbers = []
            for line in group:                  
                if line.text() == "":
                    line.setStyleSheet("background-color: #f7f48d;")
                    self.emptyline = True
                elif line.text() not in groupnumbers and line not in wrongnumbers:
                    if line.isEnabled():
                        line.setStyleSheet("background-color: #a3f7ba;")
                    groupnumbers.append(line.text())
                else:
                    samenumbers.append(line.text())
            for line in group:
                if line.isEnabled():
                    if line.text() in samenumbers:
                        line.setStyleSheet("background-color: #f7aea3;")
                        wrongnumbers.append(line)
        if len(wrongnumbers) == 0 and self.emptyline == False:
                QMessageBox.information(self, "You Win!", "You solved the table!")
    
    def createsudokuboard(self):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for col in range(9):
            choosen = choice(numbers)
            self.lines[0][col].setText(choosen)
            numbers.remove(choosen)

        def is_valid(row, col, num):
            # Check the row
            for i in range(9):
                if self.lines[row][i].text() == str(num):
                    return False

            # Check the column
            for i in range(9):
                if self.lines[i][col].text() == str(num):
                    return False

            # Check the 3x3 grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if self.lines[start_row + i][start_col + j].text() == str(num):
                        return False
            return True

        def solve_sudoku(row, col):
            if row == 9:
                return True  # Sudoku is solved

            if col == 9:
                return solve_sudoku(row + 1, 0)

            if self.lines[row][col].text() != "":
                return solve_sudoku(row, col + 1)

            for num in range(1, 10):
                if is_valid(row, col, num):
                    self.lines[row][col].setText(str(num))
                    if solve_sudoku(row, col + 1):
                        return True
                    self.lines[row][col].setText("")  # Backtrack

            return False

        solve_sudoku(0, 0)

        if self.level == 1:
            choosenlines = []
            for i in range(30):
                while True:
                    choosenline = self.lines[randint(0, 8)][randint(0, 8)]
                    if choosenline not in choosenlines:
                        choosenlines.append(choosenline)
                        break
        
        elif self.level == 2:
            choosenlines = []
            for i in range(20):
                while True:
                    choosenline = self.lines[randint(0, 8)][randint(0, 8)]
                    if choosenline not in choosenlines:
                        choosenlines.append(choosenline)
                        break
        
        elif self.level == 3:
            choosenlines = []
            for i in range(10):
                while True:
                    choosenline = self.lines[randint(0, 8)][randint(0, 8)]
                    if choosenline not in choosenlines:
                        choosenlines.append(choosenline)
                        break
        
        elif self.level == 4:
            choosenlines = []
        
        for line in choosenlines:
            line.setDisabled(True)
            line.setStyleSheet("background-color: #dffa7d;")
        
        for row in range(9):
                for col in range(9):
                    self.lines[row][col].clear() if self.lines[row][col].isEnabled() else None
    
    def clearboard(self):
        if QMessageBox.warning(self, "Warning", "Are you sure want to clear the table?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            for row in range(9):
                for col in range(9):
                    if self.lines[row][col].isEnabled():
                        self.lines[row][col].clear()

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()