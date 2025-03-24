####################
# Wheather API App #
####################

from sys import argv
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WheatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityinput = QLineEdit(self)
        self.weatherbutton = QPushButton("Get Weather", self)
        self.temperature = QLabel(self)
        self.emoji = QLabel(self)
        self.description = QLabel(self)
        self.setWindowIcon(QIcon("weather.ico"))
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 600)
        self.setWindowTitle("Genco Weather API App")
        self.cityinput.setPlaceholderText("Enter a city")

        vbox = QVBoxLayout()
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.weatherbutton)
        vbox.addWidget(self.temperature)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description)

        self.setLayout(vbox)

        self.cityinput.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        self.succesfonts()

        self.weatherbutton.clicked.connect(self.getWeather)

    def succesfonts(self):
        self.weatherbutton.setObjectName("button")
        self.emoji.setObjectName("emoji")
        self.description.setStyleSheet("""
            color: black;
            font-size: 50px;
            """)
        self.temperature.setStyleSheet("""
            color: black;
            font-size: 80px;
            """)    
        self.setStyleSheet("""
            WheatherApp {
                background-color: #e9eba0;               
            }
    
            QLabel {
                font-weight: bold;
                font-family: calibri;              
            } 
                           
            QLabel#emoji {
                font-size: 110px;
                font-family: Segoe UI emoji;      
            }
                           
            QLineEdit {
                font-weight: bold;
                font-size: 30px;
                height: 50%;
                font-family: calibri;
                border: 10px solid;
                border-radius: 20px;
                margin-left: 30px;
                margin-right: 30px;           
            }
                               
            QPushButton {
                font-weight: bold;
                font-size: 30px;
                font-family: calibri;
                border: 10px solid;
                border-radius: 20px;
                margin-left: 30px;
                margin-right: 30px;         
            }
                               
            QPushButton#button {
                background-color: #6e6c3c;    
            }
                               
            QPushButton#button:hover {
                background-color: #91905a;
                color: white;               
            } 
            """)

    def getWeather(self):
        api_key = "" # Enter your unique API key here
        city = self.cityinput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200: # code: 200 -> response succesful
                self.displayWeather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400: # Bad Request
                    self.errorfonts()
                    self.emoji.setText("❔")
                    self.temperature.setText("Bad Request")
                    self.description.setText("Please check your input")
                case 401: #Unauthorized
                    self.errorfonts()
                    self.emoji.setText("❌")
                    self.temperature.setText("Unauthorized")
                    self.description.setText("Invalid API key")
                case 403: #Forbidden
                    self.errorfonts()
                    self.emoji.setText("🚫")
                    self.temperature.setText("Forbidden")
                    self.description.setText("Access denied")
                case 404: #Not Found
                    self.errorfonts()
                    self.emoji.setText("❔")
                    self.temperature.setText("Not Found")
                    self.description.setText("Please check your input")
                case 500: # Internal Server Error
                    self.errorfonts()
                    self.emoji.setText("🛑")
                    self.temperature.setText("Internal Server Error")
                    self.description.setText("Please try again later")
                case 502: # Bad Gateway
                    self.errorfonts()
                    self.emoji.setText("⭕")
                    self.temperature.setText("Bad Getway")
                    self.description.setText("Invalid response from server")
                case 503: # Service Unavailable
                    self.errorfonts()
                    self.emoji.setText("❗")
                    self.temperature.setText("Service Unavailable")
                    self.description.setText("Server is down")
                case 504: # Gateway Timeout
                    self.errorfonts()
                    self.emoji.setText("⏰")
                    self.temperature.setText("Gateway Timeout")
                    self.description.setText("No response from server")
                case _:
                    self.errorfonts()
                    self.emoji.setText("❓")
                    self.temperature.setText("Unknown HTTP Error")
                    self.description.setText(f"An HTTP error occured:\n{requests.exceptions.HTTPError}")
        except requests.exceptions.ConnectionError:
            self.errorfonts()
            self.emoji.setText("🛜")
            self.temperature.setText("Connection Error")
            self.description.setText("Please check your internet connection")
        except requests.exceptions.Timeout:
            self.errorfonts()
            self.emoji.setText("⏰")
            self.temperature.setText("Timeout Error")
            self.description.setText("The request timed out")
        except requests.exceptions.TooManyRedirects:
            self.errorfonts()
            self.emoji.setText("🏋🏻‍♂️")
            self.temperature.setText("Timeout Error")
            self.description.setText("The request timed out")
        except requests.exceptions.RequestException: # It can be any error of request process #4a1212
            self.errorfonts()
            self.emoji.setText("❗")
            self.temperature.setText("Unknown error")
            self.description.setText(f"An error occured:\n{requests.exceptions.RequestException}")

    def errorfonts(self):
        self.temperature.setStyleSheet("""
            color: #4a1212;
            font-size: 80px;
            """)
        self.description.setStyleSheet("""
            color: #4a1212;
            font-size: 30px;
            """)

    def displayWeather(self, data):
        self.succesfonts()
        temperature_kelvin = data["main"]["temp"] # {main: {'temp': >float<, 'feels_like': ...
        temperature_celcius = temperature_kelvin - 273.15
        #temperature_fahrenheit = (temperature_kelvin * 9/5) - 459.67
        weatherdescription = data["weather"][0]["description"]
        self.description.setText(weatherdescription)

        self.temperature.setText(f"{temperature_celcius:.1f}°C")

        wheaterid = data["weather"][0]["id"]
        self.emoji.setText(self.chooseEmoji(wheaterid))
    
    @staticmethod
    def chooseEmoji(weather_id: int) -> str:
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "☃️"
        elif 701 <= weather_id < 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🍃"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "❔"

if __name__ == "__main__":
    app = QApplication(argv)
    window = WheatherApp()
    window.show()
    app.exec_()